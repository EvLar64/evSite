import os
from nltk.corpus import wordnet as wn
cwd = os.getcwd()
print()
print("Python/NLTK Assignment (w/ POS) - EL")
print()
print("Sample of Synsets on the word 'take' (smoke test)")
print()
for synset in wn.synsets('take'):
    print(synset.lemma_names(), len(synset.lemma_names()))

filepath = '../breakfast.txt'
print(filepath)
f = open(filepath, 'r', encoding='utf8').read()
print(f)

os.listdir(cwd)
coll = os.path.join(cwd, 'hughesColl')
os.listdir(coll)

from nltk.corpus import PlaintextCorpusReader
corpus_root = 'hughesColl'
corpus = PlaintextCorpusReader(corpus_root, '.*')
corpus.fileids()