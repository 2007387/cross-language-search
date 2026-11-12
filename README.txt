Cross-Language Search (English / Hindi / Telugu)

Run:
1. python3 -m pip install -r requirements.txt
2. python3 -m streamlit run app.py

Works offline. Answers come from the small built-in database in data.py
(15 topics, each stored in Hindi, Telugu and English).

How it works:
1. Query words are looked up in a bilingual dictionary (LEXICON in data.py).
2. Every topic is scored by how many of the query's keywords it contains.
3. Only strong matches are shown (best match first, up to 3).

To add content: add lines to DOCS (in Hindi/Telugu pairs) and LEXICON in data.py.
