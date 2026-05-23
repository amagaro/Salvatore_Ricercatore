---
tags:
  - moc
  - index
taccuino: "[[Notebook - Spazi Aperti Neuroinclusivi]]"
---

# 🗺️ MOC - Spazi Aperti Neuroinclusivi

## 🌟 Visione d'Insieme
Questa Mappa del Contenuto (MOC) organizza e struttura la ricerca interdisciplinare relativa alla progettazione di **Spazi Aperti Neuroinclusivi**. L'obiettivo è analizzare e sistematizzare le relazioni tra lo spazio fisico (parchi, giardini, piazze e contesti urbani) e il benessere cognitivo, sensoriale e sociale delle persone neurodivergenti (nello spettro autistico, ADHD, DSA, e con fragilità cognitive o demenze).

---

## 📚 Fonti di Ricerca (Sources)
*Analisi sistematica dei paper e saggi scientifici processati.*

```dataview
TABLE autore as "Autore", anno as "Anno", titolo as "Titolo"
WHERE contains(file.folder, "Spazi Aperti Neuroinclusivi") AND contains(tags, "source")
SORT anno DESC
```

---

## 💡 Framework Concettuale (Concepts)
*Note atomiche che definiscono i pilastri teorici della neuroinclusione e del design sensoriale.*

```dataview
LIST 
WHERE contains(file.folder, "Spazi Aperti Neuroinclusivi") AND contains(tags, "concept")
SORT file.name ASC
```

---

## 🏗️ Casi di Studio (Case Studies)
*Analisi di progetti reali, infrastrutture urbane, installazioni e sperimentazioni sul campo.*

```dataview
TABLE progetto as "Progetto", localizzazione as "Luogo", caratteristiche as "Caratteristiche"
WHERE contains(file.folder, "Spazi Aperti Neuroinclusivi") AND contains(tags, "casestudy")
SORT file.name ASC
```

---

## 🎯 Categorizzazione & Target
*Organizzazione mirata dei casi di studio per coorti e ambiti applicativi.*

- **Pediatria/Infanzia:**
  - [[Casestudy - ASD Publics Barcelona]]
  - [[Casestudy - Play AUT the Box]]
  - [[Casestudy - DIY Play and Neuro-Non-Typical Urbanism (Auckland)]]
- **Adulti e Studenti Neurodivergenti:**
  - [[Casestudy - Kingwood College]]
  - [[Casestudy - BeSENSHome]]
- **Urbano, Infrastrutture e Spazi Pubblici:**
  - [[Casestudy - The Neurodiverse City]]
  - [[Casestudy - MPK Krakow]]
  - [[Casestudy - Tauron Arena Krakow]]
  - [[Casestudy - PEBA e UDL]]
  - [[Casestudy - Towards Neuroinclusive Public Open Spaces (Sydney)]]
- **Demenza, Alzheimer e RSA (Healing Gardens):**
  - [[Casestudy - CIDAS Ferrara]]
  - [[Casestudy - Centro Diurno La Baracca]]
  - [[Casestudy - Sedgewood Commons]]
  - [[Casestudy - Giardino Terapeutico Hampshire]]
  - [[Casestudy - Giardino Terapeutico e Sensoriale RSA Ad Maiores]]
- **Inclusione Sociale ed Etnometodologia:**
  - [[Casestudy - Condominio Intergenerazionale a Campagnuzza]]
  - [[Casestudy - Interazione di Chil]]

---

## 📑 Sintesi Avanzate & Insights
*Documenti di sintesi, analisi comparativa e linee guida strategiche prodotte.*

- [[Insight - Spazi Aperti Neuroinclusivi]] — *Sintesi evolutiva degli insight trasversali.*
- [[Sintesi - Confronto Metodologico e Integrazione Biofilia vs Smart]] — *Confronto tra framework ed integrazione di soluzioni.*
- [[Sintesi - Linee Guida Operative per lo Spazio Pubblico Neuroinclusivo]] — *Linee guida strategiche e checklist operative per progettisti (Modalità 6).*
- [[Sintesi - Trend Temporale ed Evoluzione della Co-creazione]] — *Analisi storica del trend evolutivo della progettazione partecipata (2021-2026) (Modalità 9).*
- [[Sintesi - Sinergia tra Giustizia Spaziale e Urbanismo Neuro-Non-Tipico]] — *Mappatura delle sinergie e traduzione pratica della giustizia sensoriale (Modalità 10).*

---
**Ultimo aggiornamento:** 2026-05-23
**Stato della Ricerca:** 13/13 fonti processate.
