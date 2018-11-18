import nltk
from nltk.tokenize import word_tokenize
from nltk.chunk import conlltags2tree, tree2conlltags
from nltk.tag import pos_tag
from collections import defaultdict
from bs4 import BeautifulSoup
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
import pprint

f = open("test.htm")
content = f.read()

soup = BeautifulSoup(content)

divs = soup.find_all("div")
p = soup.find_all("p")

text_div = []
p_div = []


for d in divs:
    text = d.text
    if text == '':
        continue

    if '\xa0' in text:
        text = text.replace('\xa0', ' ')

    text = ' '.join(text.split())
    text_div.append(text)

for d in p:
    p_div.append(d.text)

full_text = text_div + p_div

full_text3 = " ".join(full_text)

nlp = en_core_web_sm.load()
doc = nlp(full_text3)

# ner = defaultdict(list)
# for X in doc.ents:
    # ner[X.label_].append(X.text)

ner = defaultdict(lambda: defaultdict(int))
for X in doc.ents:
    ner[X.label_][X.text] += 1

import pdb; pdb.set_trace()
