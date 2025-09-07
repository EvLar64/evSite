import os
from nltk import pos_tag
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
print()
print("Python/NLTK Assignment (w/ POS) - EL")
print()
print("Sample of Synsets on the word 'take' (smoke test):")
for synset in wn.synsets('take'):
    print(synset.lemma_names(), len(synset.lemma_names()))
cwd = os.getcwd()
filepath = 'hughesColl/breakfast.txt'
f = open(filepath, 'r', encoding='utf8').read()
print()
print("Short sample output from script using directory:")
print(f[:100])
print()

os.listdir(cwd)
coll = os.path.join(cwd, 'hughesColl')
os.listdir(coll)

print("Successfully able to find multiple filepaths from one collection")
print()
for file in os.listdir(coll):
   if file.endswith(".txt"):
        filepath = f"{coll}/{file}"
        print(filepath)
print()
from nltk.corpus import PlaintextCorpusReader
corpus_root = 'hughesColl'
corpus = PlaintextCorpusReader(corpus_root, '.*')
corpus.fileids()

# adjective counter and adjective list variables created
# (which will get added upon as the scripts are passed through)
adjective_count = 0
adjectives = []

for file in corpus.fileids():
    hughesContent = corpus.raw(file)
    words = word_tokenize(hughesContent)
    tagged_words = pos_tag(words)
    for word, tag in tagged_words:
        # adjective codes sourced from the internet
        if tag in ['JJ', 'JJR', 'JJS']:
            adjective_count += 1
            adjectives.append(word)


adjective_freq = FreqDist(adjectives)
print(f"Total number of adjectives in the corpus (all three scripts): {adjective_count} ")
print("The 50 most common adjectives used in the three screenplays are:")
hughes_common_adj = adjective_freq.most_common(50)
print(hughes_common_adj)
print()