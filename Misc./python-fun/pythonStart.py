
for line in open("Truman_1950.txt"):
     for word in line.split():
         if word.endswith('ing'):
             print(word)