import requests
import os
from bs4 import BeautifulSoup

# Webscraping exercise - EL

url = 'https://en.wikipedia.org/wiki/List_of_Modern_Family_episodes'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print( )
print("'Modern Family' Episode Titles (Sourced from Wikipedia)")
print( )
print("Season 1:")

# Finding all tables on the wikipedia page and designating each one to a season of the show
table = soup.find_all('table', {'class': 'wikitable plainrowheaders wikiepisodetable'})
season_1_table = table[0]
season_2_table = table[1]
season_3_table = table[2]
season_4_table = table[3]
season_5_table = table[4]
season_6_table = table[5]
season_7_table = table[6]
season_8_table = table[7]
season_9_table = table[8]
season_10_table = table[9]
season_11_table = table[10]
# Takes in the row containing the titles of each episode (for each season)
rows1 = season_1_table.find_all('tr')
for row in rows1:
    columns = row.find_all('td')
    # Not exactly sure why this next part was necessary (didn't work otherwise), some kind of indexing thing that I'm not familiar with yet, but that was a solution I found on the web
    if len(columns) > 1:
        title = columns[1].get_text(strip=True)
        print(title)
print( )
print("Season 2:")
rows2 = season_2_table.find_all('tr')
for row in rows2:
    columns = row.find_all('td')
    if len(columns) > 1:
        title = columns[1].get_text(strip=True)
        print(title)
print( )
print("Season 3:")
rows3 = season_3_table.find_all('tr')
for row in rows3:
    columns = row.find_all('td')
    if len(columns) > 1:
        title = columns[1].get_text(strip=True)
        print(title)
print( )
print("Season 4:")
rows4 = season_4_table.find_all('tr')
for row in rows4:
    columns = row.find_all('td')
    if len(columns) > 1:
        title = columns[1].get_text(strip=True)
        print(title)
print( )
print("Season 5:")
rows5 = season_5_table.find_all('tr')
for row in rows5:
    columns = row.find_all('td')
    if len(columns) > 1:
        title = columns[1].get_text(strip=True)
        print(title)
print( )
print("Season 6:")
rows6 = season_6_table.find_all('tr')
for row in rows6:
    columns = row.find_all('td')
    if len(columns) > 1:
        title = columns[1].get_text(strip=True)
        print(title)
print( )
print("Season 7:")
rows7 = season_7_table.find_all('tr')
for row in rows7:
    columns = row.find_all('td')
    if len(columns) > 1:
        title = columns[1].get_text(strip=True)
        print(title)
print( )
print("Season 8:")
rows8 = season_8_table.find_all('tr')
for row in rows8:
    columns = row.find_all('td')
    if len(columns) > 1:
        title = columns[1].get_text(strip=True)
        print(title)
print( )
print("Season 9:")
rows9 = season_9_table.find_all('tr')
for row in rows9:
    columns = row.find_all('td')
    if len(columns) > 1:
        title = columns[1].get_text(strip=True)
        print(title)
print( )
print("Season 10:")
rows10 = season_10_table.find_all('tr')
for row in rows10:
    columns = row.find_all('td')
    if len(columns) > 1:
        title = columns[1].get_text(strip=True)
        print(title)
print( )
print("Season 11:")
rows11 = season_11_table.find_all('tr')
for row in rows11:
    columns = row.find_all('td')
    if len(columns) > 1:
        title = columns[1].get_text(strip=True)
        # This is a specific requirement for the last table only, as it seems (probably by simple human error), that that cell was incorrectly coded and was getting included with the rest of the titles originally
        if title != "Gail Mancuso":
            print(title)

