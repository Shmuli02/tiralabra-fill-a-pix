# Käyttöohje

Ennen aloittamista täytyy asentaa tarvittavat riippuvuuden. Asenna riippuvuuden komennolla ```poetry install```

Ratkaistavat pelit tulee lisätä kansioon src/games.
Hakemistosta löytyy valmiita Fill-a-pix pelejä testaamista varten.

Ohjelman voi suorittaa juurihakemuksessa komennolla ```poetry run invoke start``` tai käynnisämällä tiedoston solver.py
Ohjelma käynnistää komentorivikäyttöliittymän. Ohjelma etsii kaikki pelit kansioista src/games ja antaa jokaiselle tiedostolla numeron.

Syötä se numeron mihinkä peliin haluat ratkaisu.

Ohjelman saa sammutettua syöttämällä 'exit'

Excel tulostamista varten tulee asentaa xlwings-kirjasto. Tämän saa asennettua komennolla ```pip install xlwings```
