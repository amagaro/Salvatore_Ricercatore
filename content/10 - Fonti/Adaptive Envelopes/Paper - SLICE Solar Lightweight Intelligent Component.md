---
tags:
  - source
  - pdf
autore: N/A
anno: 2021
titolo: "SLICE: Solar Lightweight Intelligent Component for Envelopes"
---

# 📄 Fonte: SLICE Solar Lightweight Intelligent Component

## Metadati
- **Titolo:** SLICE: An Innovative Photovoltaic Solution for Adaptive Envelope Prototyping and Testing (sustainability-13-08701.pdf)
- **Autori:** N/A
- **Anno:** 2021
- **Notebook Originale:** [[Notebook - Adaptive Envelopes]]

## Sintesi Estesa

### 1. Obiettivi
La ricerca mira a sviluppare SLICE (Solar Lightweight Intelligent Component for Envelopes), un innovativo componente adattivo e autosufficiente. L'obiettivo è superare le barriere dei dispositivi dinamici tradizionali (pesanti, costosi, energivori) progettando un modulo di facciata leggero e stand-alone. Integrando materiali compositi flessibili con celle fotovoltaiche ad alta efficienza (BIPV), il sistema deve auto-alimentare i propri movimenti per gestire il guadagno solare e mitigare il fabbisogno di raffrescamento negli edifici mediterranei.

### 2. Metodologia
La metodologia multidisciplinare unisce scienza dei materiali, meccatronica e architettura, sviluppando due prototipi fisici (SLICE 1.0 e 2.0). Materiali: termoformatura di composito flessibile (lino e TPE) in configurazione a soffietto con integrazione BIPV. Meccanica: guide lineari e pulegge comandate da motore. Logica: Arduino Mega 2560 collegato a sensori ambientali (luce, IR, pioggia/neve). Testbed: test funzionale in condizioni reali a Catania su finestre a Sud/Ovest, valutando Comfort Mode, Energy Mode e Manual Mode.

### 3. Limiti della Ricerca (Limitations)
Il limite principale risiede nell'algoritmo di Energy Mode: la scheda Arduino e il codice mancano della capacità di tracciare le variazioni degli angoli zenit e azimut del sole. Questo impedisce il corretto tracciamento solare, riducendo l'efficienza massima teorica di generazione PV in tempo reale.

### 4. KPI e Risultati Misurati
- Specifiche (SLICE 2.0): 100x68 cm, peso 1.5 kg, batteria 8.33 Wh.
- KPI Elettrico: tensione operativa misurata stabilmente a 1.8V (come atteso per 3 celle in serie).
- KPI Software: attuazione Energy Mode esatta a 45 secondi dal rilevamento di assenza umana; Comfort Mode si arresta esattamente alla soglia visiva di 500 lux.
- Risultati Qualitativi: coerente risposta del codice Java/C++ alle variabili atmosferiche, dimostrando assoluta affidabilità della piattaforma.

### 5. Sviluppi Futuri
Migliorare operativamente l'Energy Mode tramite l'implementazione di algoritmi matematici supplementari in Arduino in grado di elaborare la traiettoria solare dinamica (sun-tracking) e ottimizzare l'angolo di incidenza.

### 6. Conclusioni
SLICE è una prova di concetto pienamente riuscita. Ha dimostrato che le cerniere meccaniche possono essere sostituite da piegature intrinseche di compositi tessili. Tramite integrazione fotovoltaica, la facciata è in grado di agire passivamente e pro-attivamente (autonoma energeticamente) bilanciando generazione solare e comfort dell'utente.

## Concetti Chiave
- [[BIPV Flessibile e Stand-alone]]

## Bibliografia Rilevante
1. Nel testo non vengono citate altre fonti bibliografiche specifiche.

---
[[Casestudy - SLICE 2.0]]
