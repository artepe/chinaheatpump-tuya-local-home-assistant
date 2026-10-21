> **Huom:** 770 raakareitin dokumentointi ei tarkoita, että kaikkien parametrien
> fyysinen merkitys tai asteikko olisi vahvistettu. Automaattista AI-kirjoittamista
> varten katso [turvallisuus- ja varmennusohje](docs/AI_SAFETY.md).

# Mango Tuya Local

Home Assistant -integraation versio 0.2.1 beta sisaltaa kaikki **770
parametrireittia**, myos kaikki **46 WorkingFreq-kenttaa**. Yhteys on
paikallinen, Tuya 3.5. Asetusmuutoksia ei tehda kaynnistyksessa tai
tavallisessa lukemisessa.

Cool Ctrl Cpst naytetaan vahvistetulla desimaalilla: raaka 1 = 0.1.
Alarm Sound Set tarjoaa tunnetut Sound On- ja Once 10sec -valinnat.
Muiden kenttien arvot ovat raaka-arvoja, kunnes yksikot, desimaalit ja
valintakoodit on varmistettu. Kaikkien kenttien kirjoitusoikeutta ei ole
vielakaan osoitettu; laite ratkaisee, hyvaksytaanko muutos.

## Dashboard

**Mango Control** ilmestyy sivupalkkiin integraation paivityksen ja HA:n
uudelleenkaynnistyksen jalkeen. Paivita myos selaimen sivu. Kaikki 770
parametria ovat 17 kategoriassa, ja jokaisen alla on lyhyt englanninkielinen
selitys. WorkingFreq:ssa on omat lammitys- ja jaahdytystaulukoiden suodattimet.
Haku toimii kaikkien kategorioiden yli.

Arvo lahetetaan vasta oman kentan **Apply**-painikkeesta. Nimen perusteella
paatellyt selitykset on merkitty Inferred; tuntematon toiminto on Unverified.
Lisaosia tai kasin arvattuja entiteettitunnuksia ei tarvita.

[Dashboardin ohje ja esikatselu](docs/DASHBOARD.md).

## Asennus

HACS: lisaa tama repo omaksi **Integration**-repoksi, lataa integraatio ja
kaynnista Home Assistant uudestaan. Manuaalisesti kopioi
`custom_components/mango_tuya_local` HA:n `custom_components`-kansioon.

Nykyisen Pi:n tutkimusistunnon voi kayttaa tunnusten tuontiin. Aja
ladatun repon kansiosta samoissa Terminal & SSH -olosuhteissa kuin kokeet:

```bash
python3 tools/install_local.py
/tmp/mango-tuya/bin/python tools/import_pi_session.py --host 192.168.10.174
ha core restart
```

Lisaa sitten **Asetukset > Laitteet ja palvelut > Lisaa integraatio >
Mango Tuya Local**. Valitse **Kayta Pi:n istunnosta tuotuja tunnuksia**.
Tunnuksia ei tulosteta, eika niita ole GitHubissa. Onnistunut lisays
poistaa valiaikaisen paikallisen tunnustiedoston.

Vaihtoehtoinen manuaalinen lisays kysyy pumpun IP:n, device ID:n ja
local keyn. Yhteyden voi paivittaa integraation uudelleenmaarityksessa.

## Kaytto

Integraatio luo 769 numerokenttaa, yhden valintakentan, kolme anturia
ja paivityspainikkeen. Yhteensa 774 entiteettia. SYS Para 2:n 34 bak-rivia
eivat kuulu saatokenttiin.

Ensimmainen koko parametriluku tapahtuu taustalla. Kentta on
unavailable, kunnes sen kokonainen oikean osion vastaus on saatu.
Hae laitesivulta esimerkiksi WorkingFreq tai SYS Para.

Jokaisen kirjoituksen edella osio luetaan uudestaan. ID, paikka ja
laitteen tuoreet raakarajat tarkistetaan. Uusi arvo vahvistetaan erillisella
lukupyynnolla. Jos vahvistus puuttuu, alkuarvoa yritetaan palauttaa.
Jos palautusta ei voida vahvistaa, virhe kertoo kentan ja alkuarvon.
Kiintea raja, esimerkiksi 3..3, ei salli muiden arvojen kirjoittamista.

Normaali lukuvalli on 30 sekuntia, ja osioita luetaan vuorotellen.
Muutos paivittaa oman osionsa heti. **Refresh all parameters** kaynnistaa
koko parametrikartan uuden lukemisen. Valitse pidempi lukuvalli asetuksista
tarvittaessa. Ala muuta samaa kenttaa samaan aikaan toisesta sovelluksesta.

Tama on versio 0.2.1 beta. Parametriprotokolla on testattu valituilla oikean
laitteen kentilla. Home Assistant -osa on testattu HA 2026.10.1:ssa
simuloidulla yhteydella; taman paivityksen toimivuus oikeassa HA:ssa on viela
varmistettava. Kopioitava asennusohjelma sailyttaa aiemman komponentin ennen
paivitysta, eika kaynnista HA:ta itsestaan uudestaan.

Tarkemmat tiedot ja vahvistuksen rajat: [README.md](README.md).

## Yhteyskorjaus 0.2.1

Tilakysely odottaa varsinaista dataa kuittauksen jalkeen ja kayttaa kolmen
sekunnin vastausaikaa. Epaonnistunut kysely yritetaan kerran uudella yhteydella.
Lyhyessa katkossa viimeiset vahvistetut arvot sailyvat enintaan
`min(120, lukuvalli * 3 + 10)` sekuntia viimeisesta yhteydesta.
Dashboard kertoo Reconnecting / last confirmed values. Pitka katkos ja
vanhentuneet lampotilat naytetaan edelleen unavailable-tilassa.
Epaonnistunutta parametriryhmaa yritetaan uudelleen seuraavalla lukukierroksella.
