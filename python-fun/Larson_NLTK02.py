#
# Python NLTK, NLP, Wordnet Assignment Part II (Additions for second part below) - EL
#

import os
from nltk import pos_tag
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
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
print()
print("The 50 most common adjectives used in the three screenplays are:")
hughes_common_adj = adjective_freq.most_common(50)
print(hughes_common_adj)
print()

# End of first assignment
#-----------------------------
# Second part

print("Part II of Assignment:")
print()
print("Example of Morphy Used on the Word 'Churches'")
print(wn.morphy('churches'))
print()

# does a similar thing to the adjectives above, but this time it also sorts them and creates
# a unique set with them
verb_count = 0
verbs = []
for file in corpus.fileids():
    hughesContent = corpus.raw(file)
    hughesWords = word_tokenize(hughesContent)
    tagged_words = pos_tag(hughesWords)
    for word, tag in tagged_words:
        if tag in ['VB'] :
            # special circumstance because capital words (even non-verbs) were
            # also being included
            if word.islower() :
                verb_count += 1
                verbs.append(word)

print("The total verb count across all three screenplays:")
print(verb_count)
print("The set of unique verbs present throughout all of the three project screenplays:")
print(sorted(set(verbs)))

# found bigram function from nltk book online
print("Most frequent bigrams:")
print()
# needs a little editing to account for punctuation and those types of things
for file in corpus.fileids():
    hughesContent = corpus.raw(file)
    words = word_tokenize(hughesContent)
    # takes in tokenized screenplay words again, and then runs them through the bigram function
    bigramFinder = BigramCollocationFinder.from_words(words)
    bigrams = bigramFinder.nbest(BigramAssocMeasures.likelihood_ratio, 10)
    for bigram in bigrams:
        print(bigram)

# attempted to make a similarity comparison between two of the screenplays,
# however I couldn't iron it out and get it to work based on the sources I found
filepath1 = 'hughesColl/sixteen.txt'
sixteen = open(filepath1, 'r', encoding='utf8').read()
filepath2 = 'hughesColl/ferris.txt'
ferris = open(filepath2, 'r', encoding='utf8').read()

# sixteenwords = word_tokenize(sixteen)
# ferriswords = word_tokenize(ferris)
# sixteenSynset = wn.synset(sixteenwords)
# ferrisSynset = wn.synset(ferriswords)
# similarity = sixteenSynset.path_similarity(ferrisSynset)
# print(similarity)

