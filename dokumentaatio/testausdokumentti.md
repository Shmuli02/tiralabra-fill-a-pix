# Testausdokumentti

## Automaattitestit
Ohjelman yksikkötestaus on toteutettu pythonin pytest kirjaston avulla. Automaattitestit voit ajaa komennolla ```poetry run invoke test``` Ensimmäisellä kerralla täytyy asentaa poetry asetukset ja riippuvuudet. Nämä saa asennettua komennolla  ```poetry install```


Testikattavuus sekä raportit löytyvät codecov palvelusta johon pääset [tästä](https://app.codecov.io/gh/Shmuli02/tiralabra-fill-a-pix). README tiedostossa näkyy myös testikattavuus.

## Koodin laatu
Koodin laadun analysointia varten käytetään pythonin pylint kirjastoa. Koodin laatu raportin saa komennolla ```poetry run invoke lint```