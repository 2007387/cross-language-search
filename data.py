# Each document: (language, text, english meaning). Documents come in Hindi/Telugu pairs per topic.
DOCS = [
 ("Hindi", "भारतीय क्रिकेट टीम ने मैच जीतकर सीरीज़ अपने नाम कर ली।", "The Indian cricket team won the match and took the series."),
 ("Telugu", "భారత క్రికెట్ జట్టు మ్యాచ్ గెలిచి సిరీస్ గెలుచుకుంది.", "The Indian cricket team won the match and took the series."),
 ("Hindi", "हैदराबाद में आज भारी बारिश हुई और सड़कों पर पानी भर गया।", "Heavy rain fell in Hyderabad today and water filled the roads."),
 ("Telugu", "హైదరాబాద్ నగరంలో ఈరోజు భారీ వర్షం కురిసింది, రోడ్లపై నీరు నిలిచింది.", "Heavy rain fell in Hyderabad today and water filled the roads."),
 ("Hindi", "किसानों को इस साल अच्छी फसल की उम्मीद है क्योंकि बारिश समय पर हुई।", "Farmers expect a good crop this year as the rain came on time."),
 ("Telugu", "ఈ ఏడాది వర్షాలు సకాలంలో కురవడంతో రైతులు మంచి పంట ఆశిస్తున్నారు.", "Farmers expect a good crop this year as the rain came on time."),
 ("Hindi", "विद्यार्थियों की परीक्षा अगले सप्ताह शुरू होगी और परिणाम अगले महीने आएंगे।", "Students' exams begin next week and results will come next month."),
 ("Telugu", "విద్యార్థుల పరీక్షలు వచ్చే వారం ప్రారంభమవుతాయి, ఫలితాలు వచ్చే నెల వస్తాయి.", "Students' exams begin next week and results will come next month."),
 ("Hindi", "सरकारी अस्पताल में मरीजों के लिए मुफ्त इलाज और दवाइयाँ उपलब्ध हैं।", "Free treatment and medicines are available for patients in the government hospital."),
 ("Telugu", "ప్రభుత్వ ఆసుపత్రిలో రోగులకు ఉచిత చికిత్స మరియు మందులు అందుబాటులో ఉన్నాయి.", "Free treatment and medicines are available for patients in the government hospital."),
 ("Hindi", "कंपनियाँ कृत्रिम बुद्धिमत्ता और नई तकनीक से मोबाइल ऐप बना रही हैं।", "Companies are building mobile apps with artificial intelligence and new technology."),
 ("Telugu", "కంపెనీలు కృత్రిమ మేధ మరియు కొత్త సాంకేతికతతో మొబైల్ యాప్స్ తయారు చేస్తున్నాయి.", "Companies are building mobile apps with artificial intelligence and new technology."),
 ("Hindi", "चुनाव में मतदान शुरू हो गया है और लोग सुबह से कतार में खड़े हैं।", "Voting has started in the election and people have been standing in queues since morning."),
 ("Telugu", "ఎన్నికల్లో పోలింగ్ ప్రారంభమైంది, ప్రజలు ఉదయం నుంచి క్యూలో నిలబడ్డారు.", "Voting has started in the election and people have been standing in queues since morning."),
 ("Hindi", "हैदराबाद मेट्रो में रोज़ हज़ारों यात्री सफ़र करते हैं और नई लाइन जल्द खुलेगी।", "Thousands of passengers travel daily on the Hyderabad Metro and a new line will open soon."),
 ("Telugu", "హైదరాబాద్ మెట్రోలో రోజూ వేలాది ప్రయాణికులు ప్రయాణిస్తారు, కొత్త లైన్ త్వరలో ప్రారంభమవుతుంది.", "Thousands of passengers travel daily on the Hyderabad Metro and a new line will open soon."),
 ("Hindi", "हैदराबादी बिरयानी अपने स्वाद और मसालों के लिए दुनिया भर में मशहूर है।", "Hyderabadi biryani is famous worldwide for its taste and spices."),
 ("Telugu", "హైదరాబాదీ బిర్యానీ తన రుచి మరియు మసాలాలకు ప్రపంచవ్యాప్తంగా ప్రసిద్ధి చెందింది.", "Hyderabadi biryani is famous worldwide for its taste and spices."),
 ("Hindi", "दिवाली के त्योहार पर लोग घरों में दीये जलाते हैं और मिठाइयाँ बाँटते हैं।", "On Diwali, people light lamps at home and share sweets."),
 ("Telugu", "దీపావళి పండుగ సందర్భంగా ప్రజలు ఇళ్లలో దీపాలు వెలిగించి మిఠాయిలు పంచుతారు.", "On Diwali, people light lamps at home and share sweets."),
 ("Hindi", "इसरो ने नया उपग्रह सफलतापूर्वक अंतरिक्ष में भेजा और वैज्ञानिकों को बधाई मिली।", "ISRO successfully sent a new satellite into space and the scientists were congratulated."),
 ("Telugu", "ఇస్రో కొత్త ఉపగ్రహాన్ని విజయవంతంగా అంతరిక్షంలోకి పంపింది, శాస్త్రవేత్తలకు అభినందనలు అందాయి.", "ISRO successfully sent a new satellite into space and the scientists were congratulated."),
 ("Hindi", "शेयर बाज़ार में तेज़ी रही और सोने के दाम में गिरावट आई।", "The share market rose and the price of gold fell."),
 ("Telugu", "షేర్ మార్కెట్లో పెరుగుదల కనిపించింది, బంగారం ధర తగ్గింది.", "The share market rose and the price of gold fell."),
 ("Hindi", "नई फ़िल्म सिनेमाघरों में रिलीज़ हुई और दर्शकों को अभिनेता का अभिनय बहुत पसंद आया।", "The new film was released in theatres and the audience loved the actor's performance."),
 ("Telugu", "కొత్త సినిమా థియేటర్లలో విడుదలైంది, ప్రేక్షకులకు నటుడి నటన చాలా నచ్చింది.", "The new film was released in theatres and the audience loved the actor's performance."),
 ("Hindi", "शहर में प्रदूषण बढ़ रहा है, इसलिए सरकार ने पेड़ लगाने का अभियान शुरू किया।", "Pollution is rising in the city, so the government started a tree-planting campaign."),
 ("Telugu", "నగరంలో కాలుష్యం పెరుగుతోంది, అందుకే ప్రభుత్వం మొక్కలు నాటే కార్యక్రమం ప్రారంభించింది.", "Pollution is rising in the city, so the government started a tree-planting campaign."),
 ("Hindi", "आईटी कंपनियों में नई नौकरियाँ निकली हैं और युवाओं को रोज़गार मिलेगा।", "New jobs have opened up in IT companies and young people will get employment."),
 ("Telugu", "ఐటీ కంపెనీల్లో కొత్త ఉద్యోగాలు వచ్చాయి, యువతకు ఉపాధి లభిస్తుంది.", "New jobs have opened up in IT companies and young people will get employment."),
]

# Bilingual dictionary. Format:  english words | hindi words | telugu words   ("/" separates synonyms)
LEXICON = """
cricket | क्रिकेट | క్రికెట్
team | टीम | జట్టు
match | मैच | మ్యాచ్
series | सीरीज़ | సిరీస్
win/won/victory/winning | जीत | గెలి/గెలు
india/indian | भारतीय | భారత
rain/rains/rainfall/raining | बारिश | వర్ష
heavy | भारी | భారీ
hyderabad | हैदराबाद | హైదరాబాద్
road/roads | सड़क | రోడ్ల
water | पानी | నీరు
today | आज | ఈరోజు
farmer/farmers/farming | किसान | రైతు
crop/crops/harvest | फसल | పంట
exam/exams/examination/examinations/test | परीक्षा | పరీక్ష
student/students | विद्यार्थ | విద్యార్థ
result/results | परिणाम | ఫలిత
hospital/hospitals | अस्पताल | ఆసుపత్రి
patient/patients | मरीज | రోగ
treatment/cure | इलाज | చికిత్స
medicine/medicines/drug/drugs | दवा | మందు
free | मुफ्त | ఉచిత
government | सरकार | ప్రభుత్వ
technology/tech | तकनीक | సాంకేతిక
artificial | कृत्रिम | కృత్రిమ
intelligence/ai | बुद्धिमत्ता | మేధ
mobile | मोबाइल | మొబైల్
app/apps | ऐप | యాప్
company/companies | कंपन | కంపెనీ
election/elections | चुनाव | ఎన్నిక
vote/votes/voting/polling | मतदान | పోలింగ్
people/public | लोग | ప్రజలు
metro | मेट्रो | మెట్రో
passenger/passengers/commuter/commuters | यात्री | ప్రయాణికు
travel/travelling/traveling/journey | सफ़र | ప్రయాణ
line | लाइन | లైన్
biryani | बिरयानी | బిర్యానీ
taste/flavour/flavor | स्वाद | రుచి
spice/spices | मसाल | మసాలా
famous/popular | मशहूर | ప్రసిద్ధి
diwali | दिवाली | దీపావళి
festival | त्योहार | పండుగ
lamp/lamps | दीये | దీపాలు
sweet/sweets | मिठा | మిఠాయి
isro | इसरो | ఇస్రో
satellite | उपग्रह | ఉపగ్రహ
space | अंतरिक्ष | అంతరిక్ష
scientist/scientists | वैज्ञानिक | శాస్త్రవేత్త
market | बाज़ार | మార్కెట్
share/shares/stock/stocks | शेयर | షేర్
gold | सोने | బంగారం
price/prices/rate/rates | दाम | ధర
fall/fell/drop/decline | गिरावट | తగ్గ
rise/rose/growth/increase | तेज़ी | పెరుగుదల
film/movie/movies/cinema | फ़िल्म | సినిమా
theatre/theater/theatres/theaters | सिनेमाघर | థియేటర్
actor | अभिनेता | నటుడ
audience/viewers | दर्शक | ప్రేక్షకు
pollution | प्रदूषण | కాలుష్యం
tree/trees/plant/plants | पेड़ | మొక్క
campaign | अभियान | కార్యక్రమం
city | शहर | నగరం
job/jobs/work | नौकर | ఉద్యోగ
youth/young | युवा | యువత
employment | रोज़गार | ఉపాధి
new | नई | కొత్త
good | अच्छी | మంచి
start/started/begin/begins/begun/starts | शुरू | ప్రారంభ
release/released/releases | रिलीज़ | విడుదల
week | सप्ताह | వారం
month | महीने | నెల
morning | सुबह | ఉదయం
home/homes/house/houses | घर | ఇళ్ల
world/worldwide | दुनिया | ప్రపంచ
send/sent/launch/launched | भेजा | పంప
build/building/built | बना | తయారు
available | उपलब्ध | అందుబాటు
queue/queues | कतार | క్యూ
expect/expects/expected | उम्मीद | ఆశి
success/successful/successfully | सफल | విజయవంతం
like/liked/love/loved | पसंद | నచ్చ
performance/acting | अभिनय | నటన
light/lit | जला | వెలిగ
"""
