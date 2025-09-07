import nltk
from nltk import FreqDist

# Python Assignment - EL
# Using Truman's speeches, it takes in each file and print their length, lexical diversity, and 20 most common words.

with open("Truman_1950.txt",'r') as file:
    text1=file.read()

with open("Truman_1951.txt",'r') as file:
    text2=file.read()

with open("Truman_1952.txt",'r') as file:
    text3=file.read()

with open("Truman_1953.txt",'r') as file:
    text4=file.read()

print("The length of Truman's 1950 speech:")
print(len(text1))

print("The length of Truman's 1951 speech:")
print(len(text2))

print("The length of Truman's 1952 speech:")
print(len(text3))

print("The length of Truman's 1953 speech:")
print(len(text4))

def lexical_diversity(text):
    words=text.split()
    return len(set(words)) / len(words)

print("Lexical diversity of 1950 speech:")
print(lexical_diversity(text1))

print("Lexical diversity of 1951 speech:")
print(lexical_diversity(text2))

print("Lexical diversity of 1952 speech:")
print(lexical_diversity(text3))

print("Lexical diversity of 1953 speech:")
print(lexical_diversity(text4))

fdist1=FreqDist(text1.split())
fdist2=FreqDist(text2.split())
fdist3=FreqDist(text3.split())
fdist4=FreqDist(text4.split())

print("Most common words of 1950 speech:")
print(fdist1.most_common(20))

print("Most common words of 1951 speech:")
print(fdist2.most_common(20))

print("Most common words of 1952 speech:")
print(fdist3.most_common(20))

print("Most common words of 1953 speech:")
print(fdist4.most_common(20))
