import csv
#import os
from pathlib import Path

#from collections import namedtuple
#
#Song = namedtuple('Song', ['Position', 'Artist', 'Name'])
#Songlist = []

# Maak vanuit de CSV een dict met nummer:naam
# en een dict met naam:nummer
with open('20 Jaar Top 2000 Dossier 2018.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    songs_num = dict()
    for row in csv_reader:
        if 0 < line_count: # < 11:
            songs_num[int(row[0])] = row[1] + ' - ' + row[2]
        line_count += 1
songs_name = dict((v,k) for k,v in songs_num.items())

'''
Per flac file:
   strip 'nummer' van het bestand en bewaar 'nummer' en 'naam' (oud)
   zoek deze 'naam' in de dict_naam (nieuw)
   als gevonden:  
       maak een lijst van wijzigingen: oud_nummer wordt nieuw_nummer.
   anders:
       print de niet gevonden bestandsnaam '''

path = Path('.').glob('*.flac')
for f in sorted(path):
    t = f.name.split(' - ') #[0]
    nummer_oud = t[0]
    song = t[1] + ' - ' + t[2].split('.')[0] # Exlusief .flac
    
    if song in songs_name:
        print(f"Gevonden         : {song}")
        print(f"Nummer oud (file): {nummer_oud}")
        print(f"Moet zijn (2018) : {songs_name[song]}")
    else:
        print(f"Niet gevonden: {song}")
        print(f"Filenaam: {f.name}")
    print()
