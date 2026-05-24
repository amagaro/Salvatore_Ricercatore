---
tags:
  - moc
  - index
taccuino: "[[Notebook - Realtà Aumentata Patrimonio]]"
---

# 🗺️ MOC - Realtà Aumentata Museale

## 🌟 Visione d'Insieme
Questa mappa aggrega la ricerca sull'applicazione della **Realtà Aumentata (AR)** e delle tecnologie immersive nel contesto dei Beni Culturali, con un focus particolare sull'**inclusività** e l'accessibilità museale per persone con disabilità.

## 📚 Fonti di Ricerca (Sources)
*Analisi sistematica dei paper e documenti processati.*

```dataview
TABLE autore as "Autore", anno as "Anno", titolo as "Titolo"
WHERE contains(file.folder, "Realtà Aumentata Patrimonio") AND contains(tags, "source")
SORT anno DESC
```

## 💡 Framework Concettuale (Concepts)
*Note atomiche che definiscono i pilastri teorici.*

```dataview
LIST 
WHERE contains(file.folder, "Realtà Aumentata Patrimonio") AND contains(tags, "concept")
SORT file.name ASC
```

## 🏗️ Casi di Studio (Case Studies)
*Analisi di implementazioni reali e sperimentazioni tecnologiche.*

```dataview
TABLE progetto as "Progetto", localizzazione as "Luogo", tecnologia as "Tecnologia"
WHERE contains(file.folder, "Realtà Aumentata Patrimonio") AND contains(tags, "casestudy")
SORT file.name ASC
```

## 🎯 Categorizzazione & Target
- **Inclusività Sensoriale:** [[Casestudy - AR4VI]], [[Casestudy - NAVIG]], [[Casestudy - Google Glass_4_Lis (progetto ATLAS)]]
- **Patrimonio Archeologico:** [[Casestudy - Valorizzazione dell'Anfiteatro romano di Catania]], [[Casestudy - Pompei per Tutti e progetto Con-me (Smart Pompei)]]
- **Gamification/Edutainment:** [[Casestudy - Castello Reale del Wawel - Accessibilità Digitale]], [[Casestudy - C[AR]ds™ Prototype]]

---
**Ultimo aggiornamento:** 2026-05-12
**Stato della Ricerca:** In corso.
