---
tags:
  - moc
  - index
taccuino: "[[Notebook - giardini terapeutici]]"
---

# 🗺️ MOC - Giardini Terapeutici

## 🌟 Visione d'Insieme
Questa Mappa del Contenuto (MOC) organizza la ricerca multidisciplinare sui **Giardini Terapeutici (Healing Gardens)**, integrando evidenze cliniche, architettura del paesaggio, psicologia ambientale e rigenerazione urbana.

## 📚 Fonti di Ricerca (Sources)
*Analisi sistematica dei paper e tesi processati tramite NotebookLM.*

```dataview
TABLE autore as "Autore", anno as "Anno", titolo as "Titolo"
WHERE contains(file.folder, "giardini-terapeutici") AND contains(tags, "source")
SORT anno DESC
```

## 💡 Framework Concettuale (Concepts)
*Note atomiche che definiscono i pilastri teorici della disciplina.*

```dataview
LIST 
WHERE contains(file.folder, "giardini-terapeutici") AND contains(tags, "concept")
SORT file.name ASC
```

## 🏗️ Casi di Studio (Case Studies)
*Analisi di implementazioni reali, progetti ospedalieri e rigenerazioni urbane.*

```dataview
TABLE progetto as "Progetto", localizzazione as "Luogo", tecnologia as "Tecnologia"
WHERE contains(file.folder, "giardini-terapeutici") AND contains(tags, "casestudy")
SORT file.name ASC
```

## 🎯 Target & Vulnerabilità
*Categorizzazione manuale degli interventi in base alla coorte di riferimento.*
- **Pediatria:** [[Casestudy - Ospedale Meyer (Firenze)]], [[Casestudy - Ospedale Cà Foncello (Treviso)]], [[Casestudy - Royal Children’s Hospital (Melbourne)]], [[Casestudy - Comer Children’s Hospital Play Garden]], [[Casestudy - Hospital La Fe (Jardín Terapéutico)]]
- **Alzheimer/Demenza:** [[Casestudy - RAF Casa Protetta (Bellinzago Novarese)]], [[Casestudy - Alzheimer Sensory Garden (Balerna)]], [[Casestudy - Fondazione Grimani Butteri (Osimo)]], [[Casestudy - Le Village Landais Alzheimer]]
- **Oncologia/Supporto:** [[Casestudy - Ospedale Carrara (Terrazze Oncologiche)]], [[Casestudy - La Casa-ONLUS (Quercianella)]], [[Casestudy - Maggie's Centres (UK)]], [[Casestudy - Maggie’s Centre Barcelona]]
- **Geriatria:** [[Casestudy - Santa Rita Geriatric Center]]
- **Salute Mentale:** [[Casestudy - Comunidad Terapéutica Can Zariquiey]]
- **Disabilità Sensoriale/Cognitiva:** [[Casestudy - Istituto Rittmeyer per ciechi (Trieste)]], [[Casestudy - Centro di Psiconeurologia NIKI Detstva]], [[Casestudy - Royal Talbot Rehabilitation Centre]]
- **Ospedali Generalisti/Acuti:** [[Casestudy - Legacy Emanuel Medical Center (The Terrace Garden)]], [[Casestudy - Singapore General Hospital (Healing Gardens)]], [[Casestudy - Freiburg University Hospital (Healing Environment)]], [[Casestudy - Chelsea and Westminster Hospital (Indoor Gardens)]], [[Casestudy - Friluftssykehuset Outdoor Care Retreat]]
- **Caregiver:** [[Casestudy - Programma GAP D-University (Corea)]]

---

## 📑 Sintesi Avanzate & Insights
*Documenti di sintesi, analisi comparativa e linee guida operative prodotte.*

- [[Insight - Giardini Terapeutici]] — *Sintesi evolutiva degli insight trasversali.*
- [[Sintesi - Linee Guida Operative per i Giardini Terapeutici]] — *Linee guida operative e checklist per operatori e progettisti (Modalità 6).*
- [[Sintesi - Confronto Framework Descalzo vs Beh]] — *Confronto metodologico e modello di design cognitivo-sensoriale integrato (Modalità 5).*

---
**Ultimo aggiornamento:** 2026-05-23
**Stato della Ricerca:** 16/16 fonti processate.
