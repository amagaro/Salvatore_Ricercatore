---
draft: true
tags:
  - tesi
  - 5D_BIM
  - approfondimento
  - wbs
---

# 🎓 Proposta di Tesi 1: Integrazione tra BIM orientato agli oggetti e Normative di Computo Locali

## 1. Stato dell'Arte e Problematica

### Il Contesto Internazionale
A livello globale, il 5D BIM è ampiamente riconosciuto come un'evoluzione fondamentale per l'ottimizzazione e il controllo dei costi nel settore AEC. Standard internazionali come l'UniFormat o il MasterFormat sono strutturati in modo gerarchico e spaziale, sposandosi naturalmente con la logica *Object-Oriented* (orientata agli oggetti) tipica dei software di BIM authoring. In questi contesti, l'estrazione delle quantità (QTO - Quantity Take-Off) e l'associazione ai costi risultano processi fluidi, basati su un Code of Accounts (COA) largamente condiviso. Tuttavia, la letteratura evidenzia ancora sfide legate alla "perdita di informazioni" (Information Loss) durante i passaggi di interoperabilità tramite formati aperti (IFC) tra piattaforme di modellazione e software di computazione.

### Il Contesto Italiano e la Crisi delle WBS
In Italia, l'implementazione del 5D BIM si scontra con una barriera sistemica e metodologica profonda. I prezzari locali, regionali e nazionali (es. prezzari DEI, prezzari Camerali) sono storicamente strutturati per "lavorazione" e non per "elemento fisico". 
Questo genera un forte attrito con il BIM: mentre il modello digitale è composto da *oggetti* (es. "Muro", "Pilastro"), il computo tradizionale italiano è costruito per *attività* (es. "Getto in opera", "Posa di casseri", "Rasatura"). 

**La criticità delle WBS italiane:** Il sistema delle *Work Breakdown Structures* utilizzato tradizionalmente in Italia risulta spesso disfunzionale in ambiente BIM. Non esistendo una standardizzazione nazionale per il raccordo tra WBS e oggetti BIM, i progettisti e le imprese sono costretti a creare mappature manuali (Mapping) complesse e frammentate. Nonostante la spinta del DM 560/2017 e del Nuovo Codice degli Appalti (D.Lgs 36/2023) verso la digitalizzazione, la mancanza di interoperabilità tra i software gestionali/contabili (ERP) italiani e le piattaforme BIM costringe spesso a estrazioni manuali e data-entry ridondanti, limitando il 5D BIM a un mero esercizio teorico o esponendo i progetti a gravi errori di stima.

---

## 2. Obiettivo della Ricerca

Il focus centrale della tesi è dimostrare come colmare il **divario semantico e operativo** tra i modelli informativi BIM e le rigide strutture delle stazioni appaltanti locali italiane. L'obiettivo è duplice:
1. **Analizzare criticamente e "mettere in crisi"** l'attuale impostazione delle WBS in Italia, evidenziandone l'inadeguatezza per i flussi di lavoro digitali contemporanei.
2. **Proporre un framework ibrido di standardizzazione**, un ponte logico e informatico (BIM-to-WBS) capace di allineare i database dei prezzari locali ai parametri estratti in automatico dal modello 3D, garantendo un aggiornamento dei costi in tempo reale e senza perdita di dati.

---

## 3. Metodologia Dettagliata

La ricerca si strutturerà in tre fasi operative applicate a un caso studio (nuova costruzione o recupero edilizio tramite HBIM):

*   **Fase 1: Data Collection & Information Modeling**
    *   Sviluppo di un modello architettonico e strutturale (es. in Revit) definendo a priori i Livelli di Fabbisogno Informativo (LOIN/LOD) necessari per la fase 5D.
    *   Creazione di parametri condivisi specifici per intercettare i requisiti dei prezzari italiani (es. scorporo dei vuoti, spessori, tipologie di finitura stratificata).
*   **Fase 2: Strutturazione della WBS e Data Mapping (Il Core della Ricerca)**
    *   Decomposizione di una porzione di listino prezzi locale e riorganizzazione in una WBS "BIM-Oriented" che tenti di mediare tra la logica a lavorazioni e quella a oggetti.
    *   Sviluppo di algoritmi di associazione automatica tramite Visual Scripting (es. Dynamo) o Python. Lo script dovrà incrociare le QTO (Quantity Take-Off) geometriche estratte dagli oggetti con i codici del listino tramite una chiave relazionale.
*   **Fase 3: Validation, Automation & Stress Test**
    *   Generazione del Computo Metrico Estimativo automatizzato (con esportazione dati in CSV/XML o interfacciamento diretto con software come Primus/Mastro).
    *   **Test di Varianza:** Simulazione di tre varianti di progetto in corso d'opera. Misurazione dei tempi di ricalcolo del computo e dell'incidenza di errore rispetto al metodo di aggiornamento tradizionale manuale.

---

## 4. Risultati Attesi

Per evidenziare la portata innovativa del lavoro, i risultati verranno suddivisi su due livelli di impatto:

### 4.1 Risultato Generale (Teorico e Metodologico)
*   **Validazione di un'Ontologia BIM-WBS:** La tesi fornirà la dimostrazione teorica che è possibile superare il disallineamento semantico tra la logica "a oggetti" e quella "a lavorazioni", proponendo un nuovo paradigma di classificazione delle WBS per il panorama italiano, ispirato a standard internazionali ma adattato ai vincoli normativi locali.
*   **Critica Strutturale e Policy Recommendation:** Un'analisi documentata che dimostra l'inefficienza tecnica dei prezzari attuali, suggerendo linee guida per la futura evoluzione dei prezzari regionali verso formati *machine-readable* e *object-oriented*.

### 4.2 Risultati Secondari (Pratici e Operativi)
*   **Riduzione Misurabile dei Tempi e degli Errori:** Dimostrazione empirica, tramite il caso studio, dell'abbattimento (es. -80%) delle ore uomo necessarie per l'aggiornamento del computo a seguito di varianti, con contestuale riduzione degli errori di omissione geometrica.
*   **Toolkit Esportabile:** Creazione di uno script (Dynamo/Python) funzionante e riutilizzabile da studi professionali o stazioni appaltanti per mappare e automatizzare il QTO con i prezzari locali.

---

## 5. Bibliografia di Riferimento (Testi Rilevanti)

Di seguito 5 articoli accademici fondamentali per inquadrare l'integrazione del 5D BIM, il problema del cost estimation e la gestione delle WBS:

1. **Fazeli, A., et al. (2021).** *"An integrated BIM-based approach for cost estimation in construction projects"*. (Fondamentale per comprendere il mapping tra parametri 3D e normative/costi, abbattendo il gap di integrazione).
2. **Pishdad, P., & Onungwa, I. O. (2024).** *"Analysis of 5D BIM for Cost Estimation, Cost Control, and Payments"*. (Analisi recente focalizzata sull'accuratezza del computo in fase esecutiva e sulla strutturazione dei dati).
3. **Autori Vari (2023).** *"Influence of BIM on Work Breakdown Structure in the Construction Industry"*. (Testo chiave per analizzare criticamente come l'avvento del BIM obblighi a ripensare la frammentazione della WBS in cantiere per evitare contraddizioni).
4. **Boton, C., et al. (2023/2024).** *"Systematic Review of 5D BIM Implementation in Construction Projects"*. (Overview bibliografica essenziale che correla la WBS, l'estrazione delle quantità QTO e l'organizzazione dei codici di conto COA).
5. **Perera, S., et al.** *"O2E2: A Framework for Evolving Cost Estimation in BIM Workflow"*. (Illumina il processo tecnico di transizione da sistemi codificati spazialmente alla stima dei costi locale).
