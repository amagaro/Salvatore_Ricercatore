---
draft: true
tags:
  - tesi
  - 5D_BIM
  - approfondimento
  - optioneering
  - value_engineering
---

# 🎓 Proposta di Tesi 2: Valutazione Economica Multi-Scenario (Optioneering) in fase di Design

## 1. Stato dell'Arte e Problematica

### Il Contesto Internazionale
Nel panorama internazionale della gestione di progetto (Project Management), l'uso del 5D BIM nelle fasi preliminari è sempre più orientato al *Value Engineering* e al *Data-Driven Design*. L'Optioneering – ovvero la valutazione comparata di decine di scenari progettuali alternativi (es. tecnologie costruttive, materiali per l'involucro) – è considerata una *best practice* in mercati maturi come quello anglosassone o nordeuropeo. In questi contesti, l'integrazione dinamica tra geometria e costi permette ai decision-maker di ottimizzare il rapporto costi/benefici sin dal Concept Design, quando l'impatto economico delle scelte è massimo e il costo per apportare modifiche è minimo (Curva di MacLeamy).

### Il Contesto Italiano: La Progettazione "a Silos"
In Italia, la pratica professionale sconta ancora una forte divisione "a compartimenti stagni" (silos) tra la progettazione architettonica e la stima economica. Tradizionalmente, la quantificazione dei costi avviene esclusivamente "a valle" del processo (nei progetti definitivi/esecutivi). Se il costo supera il budget, si procede a dolorosi tagli (i cosiddetti "tagli lineari" ai capitolati) che spesso deprimono la qualità architettonica e le performance dell'edificio. 
Inoltre, a causa di onorari professionali compressi e tempistiche serrate, la propensione all'esplorazione di opzioni alternative in fase preliminare è bassissima. Il 5D BIM è quindi raramente percepito come uno strumento "attivo" a supporto della creatività e delle decisioni del progettista.

---

## 2. Obiettivo della Ricerca

Il focus della tesi è dimostrare l'utilità del 5D BIM non come strumento puramente contabile e retroattivo, ma come **strumento proattivo di "Value Engineering"**. L'obiettivo è:
1. Sviluppare un flusso di lavoro che permetta ai progettisti di testare diverse alternative costruttive in modo agile durante le prime fasi del progetto.
2. Dimostrare che la consapevolezza economica in tempo reale non limita la libertà architettonica, ma indirizza le scelte progettuali verso un reale "Target Value Design", ottimizzando il budget disponibile per massimizzare la qualità del costruito.

---

## 3. Metodologia Dettagliata

La ricerca si applicherà su un edificio (es. residenziale pluripiano o edificio scolastico) e si svilupperà in tre fasi:

*   **Fase 1: Scenario Design & Modellazione Parametrica**
    *   Definizione di un modello Architettonico e Strutturale "Base".
    *   Sviluppo di almeno tre scenari progettuali alternativi. Ad esempio: 
        *   Scenario A: Struttura tradizionale a telaio in C.A. e tamponamenti in laterizio.
        *   Scenario B: Struttura in legno X-LAM e involucro a secco.
        *   Scenario C: Struttura ibrida acciaio/legno.
*   **Fase 2: Dynamic Link e Strutturazione dei Costi**
    *   Associazione parametrica degli elementi (in Revit) a un database di costi elementari (tramite Navisworks o plugin di 5D integrato come Bexel Manager o Vico Office).
    *   Sviluppo di un sistema di classificazione macroscopico, in grado di stimare i costi per assiemi e componenti funzionali prima di scendere al livello di dettaglio delle singole lavorazioni.
*   **Fase 3: Cost/Benefit Analysis & Optioneering**
    *   Estrazione in tempo reale delle variazioni di budget al semplice variare (tramite switch parametrico) dell'opzione costruttiva nel modello 3D.
    *   Valutazione comparativa (Analisi Multicriterio) che incroci non solo il CAPEX (costo di costruzione), ma anche fattori qualitativi come i tempi di esecuzione e la sostenibilità ambientale.

---

## 4. Risultati Attesi

### 4.1 Risultato Generale (Teorico e Metodologico)
*   **Shift di Paradigma:** Dimostrare il passaggio concettuale dalla *Cost Estimation* passiva (registrazione dei costi a posteriori) al *Cost Design* proattivo (progettazione guidata dai costi), dimostrando l'efficacia del Target Value Design nel mercato locale.
*   **Valorizzazione del Ruolo del Progettista:** Evidenziare come il BIM restituisca all'architetto o all'ingegnere il controllo economico sul proprio progetto fin dalle fasi embrionali.

### 4.2 Risultati Secondari (Pratici e Operativi)
*   **Matrice Decisionale Interattiva:** Produzione di un workflow (es. tramite dashboard in PowerBI connessa al modello Revit) che consenta al Committente di "giocare" con le scelte di progetto visualizzando immediatamente l'impatto sul portafoglio.
*   **Proof of Concept sull'Ottimizzazione del Budget:** Validazione quantitativa che, in almeno uno degli scenari proposti, l'approccio integrato abbia evitato l'*over-budget* mantenendo inalterata l'intenzione architettonica.

---

## 5. Bibliografia di Riferimento (Testi Rilevanti)

Per la revisione della letteratura, si consiglia di ingerire in NotebookLM i seguenti 5 testi fondamentali sull'optioneering e il Value Engineering:

1. **El-Sayed, M., et al. (2022/2023).** *"Synergizing BIM and Value Engineering in the Construction of Residential Projects"*. (Lettura obbligata per il framework di integrazione tra esplorazione del design e stima dei costi).
2. **Niemioja, S., et al.** *"Classification of cost data and its use in 5D BIM"*. (Fondamentale per risolvere il problema dell'aggiornamento dei cataloghi di costo durante le continue iterazioni spaziali di design).
3. **Autori Vari (2021).** *"Exploring the Application of BIM Technology in the Whole Process of Construction Cost Management"*. (Analizza l'efficacia del controllo costi nell'intero ciclo di vita, con focus sul phase-gating preliminare).
4. **Al-Hajj, A., & Zanni, M. A. (2021/2023).** *"BIM and Target Value Design: A synergistic approach for construction projects"*. (Analizza l'approccio proattivo al cost management fin dalle prime bozze progettuali).
5. **Smith, P. (2016/2024 aggiornamenti).** *"BIM implementation – global strategies and cost management"*. (Fornisce la cornice internazionale sulle best practice per l'integrazione del Quantity Surveying nel BIM).
