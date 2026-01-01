# Õigusloome AI Sandbox → Piloot

## 1. Eesmärk
Sandbox on kontrollitud keskkond, mille eesmärk on hinnata,
kas ja millistel tingimustel saab AI toetada õigusloomet
ilma õigusliku otsustamise või spekuleerimiseta.

## 2. Kasutusala
Lubatud:
- avalik, kehtiv õigusmaterjal (Riigi Teataja)
- informatiivne analüüs ja kokkuvõte

Välistatud:
- õiguslikud hinnangud
- otsuste tegemine
- mittekehtiv või ebaselge allikas

## 3. Tehniline arhitektuur
- LibreChat (kasutajaliides ja agendid)
- RAG (pgvector + embeddings)
- Kogumite filtreerimine (ainult RT kehtiv)
- Küsimuste gate (enne vastamist)

## 4. Turvamehhanismid
- RAG kogumipiirangud
- Metadata valideerimine
- Küsimuste klassifitseerimine
- CI-kontroll (automaatne)

## 5. Auditeeritavus
- Iga dokument on allikaga
- Iga kogum on valideeritud
- Reeglite rikkumine ei läbi CI-d

## 6. Piloodi eeltingimused
- laiendatud testkasutajad
- kasutuslogid
- tagasiside kogumine
- eraldi API-võtmed (soovituslik)

## 7. Edasine tee
Sandbox ei ole lõpp-eesmärk, vaid kontrollitud vaheaste:

**Sandbox → piiratud piloot → hinnang → võimalik tootmine**

Iga etapp eeldab eraldi otsust ja riskihinnangut.


## 8. Tehniline valideerimine
Sandboxi tehnilist seisukorda kontrollitakse automaatselt.

### Kontrolli käivitamine
```bash
py notebooks/sandbox_checks.py