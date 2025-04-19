import nltk
import nltk.corpus
import matplotlib
import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from nltk.draw import dispersion_plot
from nltk.text import Text
from nltk import word_tokenize
from nltk.corpus import PlaintextCorpusReader
import numpy as np

with open("ferris.txt",'r') as file:
    ferris=file.read()
with open("sixteen.txt",'r') as file:
    sixteen=file.read()
with open("breakfast.txt",'r') as file:
    breakfast=file.read()

# tokenizes and creates a text object with each script
ferris1 = word_tokenize(ferris)
text_ferris1 = Text(ferris1)
sixteen1 = word_tokenize(sixteen)
text_sixteen1 = Text(sixteen1)
breakfast1 = word_tokenize(breakfast)
text_breakfast1 = Text(breakfast1)

# Lexical Dispersion for words pertaining to identity or belonging in the three movies
identityWords = ["jock","nerd","geek","princess",
                 "basket case","brain","athlete",
                 "popular","freak",
                 "belong", "fit in"]

ferrisEXT = 'EXT.'
ferrisINT = 'INT.'
ferris_int_count = ferris.count(ferrisINT)
ferris_ext_count = ferris.count(ferrisEXT)
breakfastEXT = 'EXT.'
breakfastINT = 'INT.'
breakfast_int_count = breakfast.count(breakfastINT)
breakfast_ext_count = breakfast.count(breakfastEXT)
sixteenEXT = 'EXT.'
sixteenINT = 'INT.'
sixteen_int_count = sixteen.count(sixteenINT)
sixteen_ext_count = sixteen.count(sixteenEXT)

colors1 = ['#FF6EC7', '#00FFFF']
colors2 = ['#FF00FF', '#98FF98']
colors3 = ['#FFFF66', '#9B30FF']

plt.figure(1)
plt.title('Interior vs. Exterior Locations in Ferris Bueller',  fontweight='bold')
y = np.array([ferris_int_count, ferris_ext_count])
loclabels = ["Interior Locations", "Exterior Locations"]
plt.pie(y, labels = loclabels, colors=colors1, wedgeprops={'edgecolor': 'orange', 'linewidth': 1.5})

plt.figure(2)
plt.title('Interior vs. Exterior Locations in Breakfast Club', fontweight='bold')
y = np.array([breakfast_int_count, breakfast_ext_count])
loclabels = ["Interior Locations", "Exterior Locations"]
plt.pie(y, labels = loclabels, colors=colors2, wedgeprops={'edgecolor': 'red', 'linewidth': 1.5})

plt.figure(3)
plt.title('Interior vs. Exterior Locations in Sixteen Candles', fontweight='bold')
y = np.array([sixteen_int_count, sixteen_ext_count])
loclabels = ["Interior Locations", "Exterior Locations"]
plt.pie(y, labels = loclabels, colors=colors3, wedgeprops={'edgecolor': 'green', 'linewidth': 1.5})

breakfast_characters = ['Allison', 'Andrew', 'Vernon', 'Bender', 'Brian', 'Claire']
name_counts = {name: breakfast1.count(name) for name in breakfast_characters}
plt.figure(4)
plt.bar(name_counts.keys(), name_counts.values(), color=colors2, edgecolor='black', linewidth=2)
plt.xlabel('Characters')
plt.ylabel('Screenplay Mentions')
plt.title('Frequency of Main Character Mentions in Breakfast Club', fontweight='bold')
plt.show()