# KOKEILUT JA TESTAUKSET
# ======================

# KIRJASTOT JA MODUULIT
# ---------------------

import json # Mahdollistaa json-muunnokset

# Tiedoston käsittely: avaaminen ja sulkeminen

"""
Asetukset
Palvelin: 127.0.0.1
Portti: 5432
Käyttäjätunnus: Villi
Salasana: Kissa123
Tietokanta: Autolainaus
"""

"""
# Avataan tiedosto lukua varten
settingsFile = open('settings.txt', 'rt')
fileContent = settingsFile.read() # Luetaan tiedosto
print(fileContent) # Tulostetaan se

# Avataan kirjoitusta varten
settingsFile2 = open('settings.txt', 'wt')
uudetAsetukset = 'Asetukset\nPalvelin: 10.66.0.3\n'
settingsFile2.write("Tyhjät asetukset:") # Kirjoitetaan uudet tiedostot
settingsFile2.close() # Suljettava kirjoituksen jälkeen

# Avataan uudelleen kirjoituksen jällkeen
settingsFile3 = open('settings.txt', 'rt')
print(settingsFile3.read())
"""

"""
asetukset = {} # Luodaan muuttuja sanakirjaa varten, tyhjä dict
# Luetaan tiedosto with-rakenteen avulla. Tiedosto suljetaan ja muisti tyhjennetään operaation päätteeksi
with open('settings.txt', 'rt') as settingsFile4:
    rawData = settingsFile4.read() # Luetaan tiedosto tekstinä
    asetukset = json.loads(rawData) # Muunnetaan json muotoinen teksti Python-sanakirjaksi

print('Tietokanta on', asetukset['Tietokanta'])
print('Se sijaitsee palvelimella', asetukset['Palvelin'])
"""


"""
with open('settings.txt', 'at') as settingsFile5:
    settingsFile5.write('\nSkeema: public')

with open('settings.txt', 'rt') as settingsFile6:
    print(settingsFile6.read())


asetuksetDict = {
    'server': 'autolaina.raseko.fi',
    'port': 5432,
    'database': 'autolainaus',
    'userName': "postgres",
    'password': "Qwerty"
    }

asetuksetJson = json.dumps(asetuksetDict)
print(asetuksetJson)

# Kirjoitetaan asetukset tiedostoon ja luodaan se tarvittaessa
with open('asetukset.json', 'wt') as settingsFile:
    settingsFile.write(asetuksetJson)
    print("Asetukset tallennettu")
"""