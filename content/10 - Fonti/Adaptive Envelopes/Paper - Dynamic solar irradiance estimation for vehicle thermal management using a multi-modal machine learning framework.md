---
tags:
  - source
  - paper
autore: Rial A. Rajagukguk, Hoseong Lee, Hyunjin Lee
anno: 2026
titolo: "Dynamic solar irradiance estimation for vehicle thermal management using a multi-modal machine learning framework"
---

# 📄 Fonte: Dynamic solar irradiance estimation for vehicle thermal management using a multi-modal machine learning framework

## Metadati
- **Titolo:** Dynamic solar irradiance estimation for vehicle thermal management using a multi-modal machine learning framework
- **Autori:** Rial A. Rajagukguk, Hoseong Lee, Hyunjin Lee
- **Anno:** 2026
- **Notebook Originale:** [[Notebook - Adaptive Envelopes]]

## Sintesi Estesa

### 1. Obiettivi
La ricerca si propone di risolvere il problema critico della gestione termica negli abitacoli dei veicoli (con particolare focus sui veicoli elettrici, EV), un fattore che incide pesantemente sui consumi della batteria e sull'autonomia complessiva del mezzo. A differenza dei sistemi stazionari o degli edifici convenzionali, i veicoli operano in condizioni di movimento continuo attraverso paesaggi urbani complessi, dove la radiazione solare varia repentinamente a causa di ombreggiamenti dinamici (edifici, alberi, infrastrutture). L'obiettivo primario dello studio è quindi lo sviluppo di un framework basato sul machine learning multi-modale in grado di stimare con precisione la radiazione solare incidente su un veicolo in movimento in tempo reale. Questo approccio è pensato per abilitare strategie di gestione termica proattive e "location-aware" (sensibili alla posizione), regolando il controllo climatico in base all'esposizione solare anticipata e ottimizzando il bilancio energetico senza compromettere il comfort dei passeggeri. Questo approccio ha implicazioni dirette sul design degli involucri adattivi per l'automotive e per la domotica mobile, superando le sfide poste dalla stima dell'irraggiamento negli ambienti urbani.

### 2. Metodologia
La validazione metodologica dello studio si basa sulla fusione avanzata di dati ambientali provenienti da diverse fonti eterogenee, colmando il divario tra risoluzione spaziale macroscopica e condizioni a livello stradale. Il framework integra:
1. **Dati Satellitari (Remote Sensing):** Immagini spettrali acquisite dal satellite geostazionario GK2A (Advanced Meteorological Imager - AMI). Questo sensore fornisce dati su sedici canali a diverse lunghezze d'onda (visibile, infrarosso vicino, medio e lungo) con risoluzione spaziale di 0.5 km e risoluzione temporale di 10 minuti, permettendo la stima della nuvolosità globale (Cloud Index) e delle componenti macroscopiche del clima.
2. **Immagini Ground-Based (Sky Camera):** Dati visivi in tempo reale acquisiti da una telecamera industriale fisheye (U3-3280CP) montata sul tetto del veicolo sperimentale (un EV IONIQ-5). L'obiettivo fisheye (185° di campo visivo) consente di mappare ostacoli urbani immediati e condizioni nuvolose locali che sfuggono all'osservazione satellitare.
3. **Modellazione AI Multi-Modale:** L'estrazione della stima dell'irraggiamento globale orizzontale (GHI) e delle sue componenti diffusa e diretta viene operata da avanzati algoritmi basati su alberi decisionali, nello specifico XGBoost, LightGBM e CatBoost. Tali modelli sono stati addestrati per riconoscere pattern complessi nei dati fusi e sono stati confrontati contro i tradizionali modelli di decomposizione solare e approcci semi-empirici.
4. **KPI Misurati:** Il sistema è stato valutato tramite l'errore quadratico medio normalizzato (nRMSE), l'errore medio di bias normalizzato (nMBE) e i valori del coefficiente di correlazione per valutare sia in scenari di cielo sereno che coperto, con testing in diversi periodi stagionali (estate e inverno) lungo un tracciato di 7 km a Seoul.

### 3. Conclusioni
I risultati dimostrano prestazioni eccellenti del framework proposto rispetto ai metodi convenzionali basati esclusivamente su GIS o dati storici. L'errore quadratico medio normalizzato (nRMSE) ha raggiunto livelli notevolmente bassi: 14.61% durante il periodo estivo e 17.10% nel periodo invernale, a testimonianza di una notevole robustezza previsionale anche in condizioni di basso irraggiamento solare. 
**Limiti:** Tra le limitazioni evidenziate figura la dipendenza dalla qualità della connettività per la trasmissione in tempo reale di immagini satellitari ad alta risoluzione e la latenza potenziale introdotta dall'elaborazione in tempo reale di immagini visive ad alta risoluzione in sistemi embedded sui veicoli. Inoltre, la risoluzione spaziale del dato satellitare (0.5 km) richiede un processamento molto spinto delle immagini ground-based per risolvere le ostruzioni urbane minori. 
**Sviluppi Futuri:** Si prevede di espandere questo framework verso applicazioni di "smart skin" (pelli adattive) o finestrature elettrocromiche per i veicoli del futuro, nonché all'integrazione di pannelli fotovoltaici (VIPV) che possono adattare l'angolazione in base all'irraggiamento stimato, gettando le basi per un'autentica autonomia climatica e un'efficienza energetica su vasta scala per il settore dei trasporti elettrici.

## Concetti Chiave
- [[ML Multi-Modale per Irraggiamento Solare Dinamico]]
- [[Gestione Termica Location-Aware]]

## Bibliografia Rilevante
1. Paletta, Q. et al. Omnivision forecasting: combining satellite and Sky images for improved deterministic and probabilistic intra-hour solar energy predictions. (2023)
2. Penning, A. K. Assessing the influence of glass properties on cabin solar heating and range of an electric vehicle using a comprehensive system model. (2023)

---
[[Casestudy - IONIQ-5 Thermal Management Evaluation]]
