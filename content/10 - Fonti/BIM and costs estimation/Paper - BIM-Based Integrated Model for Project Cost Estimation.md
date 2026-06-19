---
tags:
  - source
  - paper
autore: Asser Elsheikh, Abdullah Saqr, Ibrahim Motawa
anno: 2025
titolo: "BIM-Based Integrated Model for Project Cost Estimation: A Case Study for Concrete Elements"
---

# 📄 Fonte: BIM-Based Integrated Model for Project Cost Estimation: A Case Study for Concrete Elements

## Metadati
- **Titolo:** BIM-Based Integrated Model for Project Cost Estimation: A Case Study for Concrete Elements
- **Autori:** Asser Elsheikh, Abdullah Saqr, Ibrahim Motawa
- **Anno:** 2025
- **Notebook Originale:** [[Notebook - BIM and costs estimation]]

## Sintesi Estesa

### 1. Obiettivi
Lo studio mira a sviluppare un modello 5D BIM integrato che collega senza interruzioni il modello dell'edificio 3D con le informazioni di programmazione temporale (scheduling) e dei costi in maniera automatizzata. L'obiettivo è generare stime di tempo e costo più accurate tenendo conto dei metodi di costruzione specifici per ciascun elemento BIM, delle risorse necessarie e dei dati sulle performance storiche.

### 2. Metodologia
La ricerca adotta una prospettiva basata sulle attività (Activity-based) in cui le quantità del modello 3D fungono da indice primario per collegare tempo e costo. Viene utilizzato un sistema di codifica unificato (ECode per l'elemento, LCode per la localizzazione, MCode per i materiali, TCode per i task e ACode per l'attività finale). Il flusso di lavoro integra Autodesk Revit per la modellazione, Navisworks per le QTO, un database relazionale (SQL) orientato agli oggetti per l'archiviazione di produttività storiche e metodi costruttivi, e Primavera P6 per la schedulazione. Il modello è stato validato attraverso un caso di studio su un edificio residenziale a sei piani in cemento armato.

### 3. Limiti della Ricerca (Limitations)
Il caso di studio è limitato esclusivamente ai lavori strutturali in calcestruzzo di un singolo progetto di medie dimensioni, limitando la generalizzabilità dei risultati. Inoltre, la trasferibilità tra diversi appaltatori o regioni geografiche richiede la mappatura di metodi locali, codici e strutture di costi unitari nel medesimo schema. Anche il database prototipale disponeva di campioni storici limitati per alcune attività.

### 4. KPI e Risultati Misurati
- **Cost Performance Index (CPI):** Utilizzando il modello proposto, il CPI per tutte le attività si è attestato in una fascia ristretta compresa tra 0.91 e 1.08 (scostamento del ±8% rispetto ai costi effettivi). In confronto, il metodo di stima tradizionale aveva generato un CPI instabile, compreso tra 0.60 e 1.25.
- **Accuratezza della Schedulazione:** La durata totale prevista per i lavori strutturali coincideva quasi perfettamente (differenza di pochi giorni) con la durata effettiva eseguita in cantiere (circa 4 mesi per la struttura in calcestruzzo).
- **Riduzione degli sforzi:** È stata osservata una sostanziale riduzione del lavoro manuale per le fasi di integrazione e riconciliazione tra stima dei costi e programmazione, generando un "resource-loaded schedule" in modo quasi istantaneo.

### 5. Sviluppi Futuri
Gli autori suggeriscono di estendere il modello includendo mestieri (trades) e materiali aggiuntivi (attualmente il focus è sul calcestruzzo) e di applicarlo a un ventaglio più ampio di scenari costruttivi. Tra gli sviluppi futuri viene proposta l'integrazione del framework 5D BIM con i flussi di approvvigionamento (procurement) e con le previsioni del flusso di cassa. Viene anche proposta l'applicazione di simulazioni Monte Carlo complete per gestire in modo più robusto l'incertezza, al fine di produrre modelli di rischio più affidabili.

### 6. Conclusioni
Il modello 5D BIM proposto unifica le fasi di progettazione, stima dei costi e programmazione temporale in un unico framework automatizzato. La connessione dinamica ai dati storici di produttività consente stime altamente realistiche ed elimina la frammentazione tipica dei metodi tradizionali, riducendo gli errori umani e allineando rigorosamente i budget con i tempi effettivi di cantiere. Si riscontra espressamente come l'elaborazione dei dati di questa ricerca confermi e consolidi scoperte precedenti: questo framework rappresenta non solo uno strumento di pianificazione, ma un "digital backbone" in tempo reale per le fasi esecutive.

## Concetti Chiave
- [[5D BIM]]
- [[Database-driven estimating]]
- [[Automated Scheduling]]

## Bibliografia Rilevante
1. Pal, A., et al. (2024). Activity-level construction progress monitoring through semantic segmentation... Automation in Construction, 157.
2. Al-Sinan, M. A., et al. (2024). Generation of Construction Scheduling through Machine Learning and BIM... Buildings, 14(4).
3. Pishdad, P., & Onungwa, I. O. (2024). Analysis of 5D Bim for Cost Estimation, Cost Control, and Payments. ITcon, 29.

---
[[Casestudy - Six-story reinforced concrete building]]
