import re, unicodedata
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data import DOCS, LEXICON

st.set_page_config(page_title="Cross-Language Search", page_icon="🌐")

def norm(s):  # lowercase + remove nukta/zero-width marks so spelling variants match
    s = unicodedata.normalize("NFC", s).lower()
    return s.replace("\u093c", "").replace("\u200c", "").replace("\u200d", "")

def words(s):
    return re.findall(r"[^\s.,!?।;:()\"'-]+", norm(s))

# ---------- Bilingual dictionary: English <-> Hindi <-> Telugu ----------
ENTRIES, INDEX = [], {}
for line in LEXICON.strip().splitlines():
    en, hi, te = [p.strip().split("/") for p in line.split("|")]
    ENTRIES.append({"label": en[0], "hi_show": hi, "te_show": te,
                    "hi": [norm(w) for w in hi], "te": [norm(w) for w in te]})
    for w in en + hi + te:
        INDEX[norm(w)] = len(ENTRIES) - 1

# Filler words (English, Hindi, Telugu) that carry no search meaning
STOP = set("""in for the a an of on to and is are was were be been at with from about who what where when
why how which whom did does do has have had will can me my i you it this that
में का की के को से पर और है हैं ने లో ని ను కు కి మరియు""".split())
GENERIC = {"today", "new", "good"}  # very common words count less than topic words

def weight(c):
    return 0.3 if c["label"] in GENERIC else 1

DOCW = [words(d[1]) for d in DOCS]  # words of every document

# ---------- Search ----------
def understand(query):
    """Step 1: turn the query into dictionary 'concepts' (plus words we could not understand)."""
    concepts, ignored = [], []
    for w in words(query):
        if w in STOP:
            continue
        for v in (w, w[:-1], w[:-2]):  # also try without plural / small suffix
            if v in INDEX:
                if ENTRIES[INDEX[v]] not in concepts:
                    concepts.append(ENTRIES[INDEX[v]])
                break
        else:
            if w.isascii():
                ignored.append(w)
            else:  # unknown Hindi/Telugu word: match it as typed
                concepts.append({"label": w, "hi_show": [w], "te_show": [w], "hi": [w], "te": [w]})
    return concepts, ignored

def hits(c, i):
    """Does document i contain a word that starts with one of the concept's terms?"""
    terms = c["hi"] if DOCS[i][0] == "Hindi" else c["te"]
    return any(w.startswith(t) for t in terms for w in DOCW[i])

@st.cache_resource
def build():
    vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), preprocessor=norm)
    return vec, vec.fit_transform([d[1] for d in DOCS])

vec, X = build()

def search(query):
    """Step 2: score every topic by how many query concepts it covers; keep only strong matches."""
    concepts, ignored = understand(query)
    if not concepts:
        return [], concepts, ignored
    total = sum(weight(c) for c in concepts)
    text = " ".join(t for c in concepts for t in c["hi"] + c["te"])
    sims = cosine_similarity(vec.transform([text]), X)[0]  # used only to break ties
    rows = []
    for t in range(len(DOCS) // 2):  # DOCS come in (Hindi, Telugu) pairs: one pair per topic
        got = [c for c in concepts if hits(c, 2 * t) or hits(c, 2 * t + 1)]
        cov = sum(weight(c) for c in got) / total
        rows.append((cov + 0.1 * max(sims[2 * t], sims[2 * t + 1]), cov, t, got))
    rows.sort(reverse=True)
    best = rows[0][1]
    keep = [r for r in rows if r[1] >= max(0.5, 0.6 * best)][:3]  # drop weak / unrelated topics
    return keep, concepts, ignored

# ---------- Screen ----------
EXAMPLES = ["heavy rain in Hyderabad", "who won today?", "gold price", "exam results"]
st.session_state.setdefault("q", "")

def pick(text):
    st.session_state.q = text

st.title("Cross-Language Search")
q = st.text_input("Search", key="q", placeholder="Type a query, e.g. heavy rain in Hyderabad", label_visibility="collapsed")
cols = st.columns(len(EXAMPLES))
for col, ex in zip(cols, EXAMPLES):
    col.button(ex, on_click=pick, args=(ex,), use_container_width=True)
lang = st.radio("Show results in", ["Both", "Hindi", "Telugu"], horizontal=True)

if q.strip():
    keep, concepts, ignored = search(q)
    if keep:
        for _, cov, t, got in keep:
            with st.container(border=True):
                for i in (2 * t, 2 * t + 1):
                    if lang in ("Both", DOCS[i][0]):
                        st.write(f"**{DOCS[i][0]}:** {DOCS[i][1]}")
                st.write(f"**English:** {DOCS[2 * t][2]}")
    else:
        st.info("No result found. Try other words, for example: rain, cricket, gold price, biryani.")
    with st.expander("How was this matched?"):
        for c in concepts:
            st.write(f"**{c['label']}** → Hindi: {', '.join(c['hi_show'])} | Telugu: {', '.join(c['te_show'])}")
        if ignored:
            st.write("Not in the dictionary (ignored): " + ", ".join(ignored))
