# Määrittelydokumentaatio

## Sovelluksen tarkoitus
Sovelluksen avulla käyttäjä voi ratkaista fill-a-pix pelejä.

## Ohjelman toteutus
**Algoritmit**
- peruuttava haku
- muita algoritmeja

**Syöte**

Ohjelma saa syötteeksi csv muodossa olevan taulun joka kuvaa haluttua fill-a-pix taulua jolle halutaan ratkaisu. CSV muoto on valittu siksi, että excelillä tai muulla vastaavalla taulukkolaskentaohjelmalla käyttäjä voi luoda syötteen. csv muotoista taulukkoa on helppo käsitellä ohjelmassa.

**Tuloste**

Lopputulosta voi olla haastava näyttää käyttäjälle terminaalissa riippuen syötteen koosta, joten ohjelma tallentaa lopuksi csv muotoon tehtävän vastauksen. csv sisältää värejä vastaavia numeroita 0 ja 1 sen mukaan onko ruutu musta vai valkoinen. Käyttäjä voi halutessaan katsoa lopputulosta taulukkolaskentaohjelmassa jossa lopputuloksen näyttäminen on fiksumpaa.

**Tavoite aika-ja tilavaatimuus**

Tavoite olisi tehdä ohjelmasta mahdollisimman nopea.
Pienet (noin 20x20) kokoiset fill-a-pix olisi tavoite saada ratkaistua 1 sekunnissa. 
Isommat (esim. 100x60) tavoite olisi ratkaista alle 10 sekunnissa.
Tavoitteita tilavaatimukselle ei ole. 

**Käytettävä kieli**

Tämän projektin kieleksi on valittu suomi. Dokumentaatioden tekeminen on helpompaa suomeksi. Ohjelmoinnissa käytettävä kieli on kuitenkin englanti, sillä ohjelmoinissa englanti sopii paremmin kuin suomi. Ääköset saattavat aiheuttaa ongelmia ja ohjelmoinnissa yleensä käytetään englantia.

Ohjelmointikieli on python.

**Lähteet**
- Tirakirja algoritmeihin
- https://www.conceptispuzzles.com valmiiden fill-a-pix saamiseen
- ja muita kurssin aikana



## Opintoohjelma
tietojenkäsittelytieteen kandidaatti (TKT)