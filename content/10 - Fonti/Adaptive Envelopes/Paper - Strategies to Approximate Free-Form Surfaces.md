---
tags:
  - source
  - pdf
autore: Moritz Koegel
anno: N/A
titolo: "Strategies to Approximate Free-Form Surfaces for the Development of a New Control System for CNC Cutting Machines to Manufacture Them"
---

# 📄 Fonte: Strategies to Approximate Free-Form Surfaces for CNC

## Metadati
- **Titolo:** Strategies to Approximate Free-Form Surfaces for the Development of a New Control System for CNC Cutting Machines to Manufacture Them (Koegel Moritz - 2026 - Strategies to Approximate Free-Form Surfaces for the.pdf)
- **Autori:** Moritz Koegel
- **Anno:** N/A
- **Notebook Originale:** [[Notebook - Adaptive Envelopes]]

## Sintesi Estesa

### 1. Obiettivi
Lo scopo principale della ricerca presentata è esplorare e sviluppare strategie per l'approssimazione di superfici architettoniche a forma libera (freeform) utilizzando superfici rigate (ruled surfaces), al fine di consentirne la fabbricazione ottimizzata attraverso una macchina per il taglio a filo caldo a due portali (TPHWC). Il problema centrale che l'autore intende risolvere è il divario tecnologico esistente tra la capacità dei moderni strumenti di progettazione computazionale di generare forme iper-complesse e la difficoltà di tradurle in processi di fabbricazione efficienti, a causa di rigorose restrizioni cinematiche e geometriche. Di conseguenza, l'obiettivo si articola su due fronti: da un lato, creare un framework algoritmico che automatizzi l'analisi geometrica e la scomposizione della superficie in strisce di taglio fattibili; dall'altro, modernizzare l'infrastruttura di una macchina legacy sostituendone l'obsoleto sistema di controllo basato su MS-DOS con una nuova architettura hardware e software, capace di eseguire istruzioni in tempo reale direttamente dall'ambiente CAD.

### 2. Metodologia
La ricerca adotta una metodologia ibrida che integra lo sviluppo di algoritmi geometrici avanzati con l'implementazione pratica a livello elettronico. A livello computazionale, l'autore ha implementato una pipeline in Rhinoceros 3D e Grasshopper (utilizzando script Python personalizzati) che analizza le superfici NURBS tramite la distribuzione di punti di campionamento. L'algoritmo valuta la curvatura locale per individuare le direzioni asintotiche ottimali e integra un'analisi preventiva delle auto-intersezioni per garantire che i percorsi del filo siano globalmente esenti da collisioni ("globally cuttable"). Dal punto di vista dell'ingegneria hardware, l'autore ha eseguito il "reverse engineering" della scheda di controllo originale della macchina, decodificando i segnali dell'interfaccia parallela LPT attraverso test con multimetro e un analizzatore logico (DSView). Sulla base di questa analisi, è stato costruito un nuovo array di microcontrollori basato su schede ESP32 (con firmware FluidNC) e Arduino Micro Pro. Infine, per colmare il divario di comunicazione, è stato sviluppato un layer basato su protocollo WebSocket che invia comandi G-code in streaming continuo da Grasshopper alla macchina, generando un "Digital Twin" (gemello digitale) per il monitoraggio operativo bidirezionale.

### 3. Limiti della Ricerca (Limitations)
L'autore dichira esplicitamente diverse limitazioni cinematiche, geometriche e metodologiche. Cinematicamente, la macchina non può realizzare tagli verticali o quasi verticali, poiché richiederebbero posizioni del filo al di fuori dei domini fisicamente raggiungibili dai portali. A livello differenziale-geometrico, la macchina non può fabbricare regioni ellittiche concave ("valli" chiuse), in quanto il filo rettilineo, essendo ininterrotto e in tensione, intersecherebbe inevitabilmente il materiale circostante per raggiungerle. Dal punto di vista dell'algoritmo sviluppato, il pathfinding attualmente è limitato all'analisi di singole superfici e non è in grado di propagare fluidamente i percorsi di taglio attraverso i bordi condivisi di polysurfaces. Infine, vi è una limitazione fisica intrinseca legata al processo termico: l'eccessivo scioglimento del materiale polistirenico causato dal calore in tagli ripetuti altera progressivamente la forma reale del manufatto.

### 4. KPI e Risultati Misurati
- Prestazioni Algoritmiche (KPI): Il tempo di calcolo complessivo per 1000 punti è di 5 secondi, con 0,5s dedicati al pathfinding (miglioramento drastico rispetto ai 50s iniziali).
- Precisione Macchina (KPI): Convalidata una risoluzione meccanica di 0,025 mm e un'accuratezza di ripetibilità di 0,015 mm.
- Reverse Engineering: Individuati pacchetti temporali stabili a 5 ms e 9 ms.

### 5. Sviluppi Futuri
- Integrazione del Quinto Asse per tagli rotazionali.
- Automazione della regolazione di tensione e potenza nel G-code.
- Transizione Software verso C/C++ per abbassare ulteriormente i tempi computazionali.
- Inclusione dell'offset pulegge nel calcolo cinematico inverso.

### 6. Conclusioni
La ricerca dimostra che l'integrazione tra ragionamento geometrico computazionale e Digital Twin abilita una lavorazione free-form "fabrication-aware". Retrofittare un macchinario obsoleto si è rivelata una scelta vincente e sostenibile.

## Concetti Chiave
- [[Fabrication-Aware Design]]
- [[Digital Twin in Architettura]]

## Bibliografia Rilevante
1. Nel testo non vengono citate altre fonti bibliografiche specifiche.

---
[[Casestudy - CNC TPHWC Retrofit]]
