from collections import Counter
import spacy
from spacy.lang.en import English

import os
nlp = spacy.load('en_core_web_lg')

collection = 'hughesColl'

def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        readFile = f.read()
        # print(readFile)
        stringFile = str(readFile)
        lengthFile = len(readFile)
        print(lengthFile)

for file in os.listdir(collection):
    if file.endswith(".txt"):
        filepath = f"{collection}/{file}"
        print(filepath)
        readTextFiles(filepath)

def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        readFile = f.read()
        # print(readFile)
        stringFile = str(readFile)

        tokens = nlp(stringFile)
        # playing with vectors here
        vectors = tokens.vector
        # print(vectors)

        wordOfInterest = nlp(u'love')

        highSimilarityDict = {}
        sorted_similarity = sorted(highSimilarityDict.items(), key=lambda item: item[1], reverse=True)
        wordCounts = Counter()

        for token in tokens:
            if (token and token.vector_norm):
                if wordOfInterest.similarity(token) > .4:
                    wordCounts[token.text] += 1
                    highSimilarityDict[token] = wordOfInterest.similarity(token)
                    # print(token.text, "about this much similar to", wordOfInterest, ": ", wordOfInterest.similarity(token))
        # for word, count in list(wordCounts.items())[:5]:
        #    print(f"'{word}': {count}")
        print(f'This is a dictionary of words most similar to the word "{wordOfInterest.text}" in "{file}".')
        for word, similarity in highSimilarityDict.items():
            count = wordCounts[word.text]
            print(f"{word}: similarity={similarity:.3f}, count={count}")
            # print(f"{word}: similarity={similarity}, count={count}")
        print('\n')


for file in os.listdir(collection):
    if file.endswith(".txt"):
        filepath = f"{collection}/{file}"
        readTextFiles(filepath)