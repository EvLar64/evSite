import os
from nltk.corpus import wordnet as wn
print()
print("Python/NLTK Assignment (w/ POS) - EL")
print()
print("Sample of Synsets on the word 'take' (smoke test)")
print()
for synset in wn.synsets('take'):
    print(synset.lemma_names(), len(synset.lemma_names()))
cwd = os.getcwd()
filepath = '/evSite/hughesColl/breakfast.txt'
f = open(filepath, 'r', encoding='utf8').read()
print(f)

os.listdir(cwd)
coll = os.path.join(cwd, 'hughesColl')
os.listdir(coll)

for file in os.listdir(coll):
   if file.endswith(".txt"):
        filepath = f"{coll}/{file}"
        print(filepath)
from nltk.corpus import PlaintextCorpusReader
corpus_root = 'hughesColl'
corpus = PlaintextCorpusReader(corpus_root, '.*')
corpus.fileids()