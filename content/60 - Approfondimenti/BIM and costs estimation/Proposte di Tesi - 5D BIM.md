---
draft: true
tags:
  - synthesis
  - tesi
  - 5D_BIM
---

# 🎓 Proposte di Tesi: 5D BIM e Cost Management

Questa nota raccoglie tre proposte strutturate per una tesi di laurea in Architettura incentrate sull'applicazione del 5D BIM. Le proposte spaziano dall'automazione del computo, all'optioneering in fase di design, fino al controllo delle varianze in cantiere. 

Tutti i framework proposti sono applicabili sia a progetti di recupero del patrimonio esistente (qualora si disponga o si realizzi un modello HBIM/BIM accurato) sia a edifici di nuova costruzione.

---

## 1. Integrazione tra BIM orientato agli oggetti e Normative di Computo Locali

### Struttura Scientifica
- **Obiettivo della Ricerca:** Dimostrare come colmare il divario semantico e operativo tra i modelli informativi (strutturati secondo standard internazionali come MasterFormat/UniFormat) e le stazioni appaltanti locali (che utilizzano Prezzari Regionali o DEI strutturati per "lavorazione").
- **Metodologia (Workflow):**
  1. *Data Collection:* Modellazione architettonica e strutturale di un caso di studio (esistente o nuovo) in Revit.
  2. *Data Mapping:* Creazione di un database relazionale (es. in Excel) o script (Dynamo) per mappare i parametri geometrici estratti (QTO - Quantity Take-Off) con i codici del listino prezzi locale.
  3. *Validation:* Generazione automatica del computo metrico estimativo e confronto (per tempi di esecuzione e accuratezza) con il metodo di stima manuale/tradizionale.
- **Risultato Atteso:** Un framework replicabile che abbatta gli errori di omissione e riduca drasticamente il tempo di aggiornamento del computo a seguito di varianti architettoniche.

### 📚 Paper Consigliati per Ingestione (NotebookLM)
1. **Fazeli, A., et al. (2021).** *"An integrated BIM-based approach for cost estimation in construction projects"*. (Già presente nel Vault: dimostra l'integrazione di standard internazionali con normative locali, caso studio Tiffa Project).
2. **Pishdad, P., & Onungwa, I. O. (2024).** *"Analysis of 5D BIM for Cost Estimation, Cost Control, and Payments"*. (Già presente nel Vault: affronta la necessità di standardizzazione nella mappatura degli oggetti).
3. **Perera, S., et al.** *"O2E2: A Framework for Evolving Cost Estimation in BIM Workflow"*. (Da ricercare/ingerire: analizza la transizione dai codici MasterFormat/UniFormat all'estimo locale automatizzato).

---

## 2. Valutazione Economica Multi-Scenario (Optioneering) in fase di Design

### Struttura Scientifica
- **Obiettivo della Ricerca:** Utilizzare il 5D BIM non come mero strumento contabile a valle del progetto, ma come strumento di "Value Engineering" a supporto del *decision-making* nelle fasi preliminari e definitive.
- **Metodologia (Workflow):**
  1. *Scenario Design:* Definizione di un caso di studio e modellazione parametrica di 2 o 3 scenari costruttivi alternativi (es. involucro performante vs involucro standard, oppure struttura X-LAM vs Cemento Armato).
  2. *Dynamic Link:* Collegamento del modello Revit a un database dei costi (tramite plugin 5D o Navisworks).
  3. *Cost/Benefit Analysis:* Estrazione in tempo reale delle variazioni di budget al variare delle scelte progettuali.
- **Risultato Atteso:** La tesi dimostrerà come la quantificazione in tempo reale dei costi abiliti una progettazione consapevole (Data-Driven Design), ottimizzando il rapporto tra qualità architettonica e budget disponibile.

### 📚 Paper Consigliati per Ingestione (NotebookLM)
1. **El-Sayed, M., et al.** *"Synergizing BIM and Value Engineering in the Construction of Residential Projects"*. (Da ricercare/ingerire: paper fondamentale sull'integrazione tra BIM e Value Engineering per l'optioneering).
2. **Autori Vari.** *"Exploring the Application of BIM Technology in the Whole Process of Construction Cost Management"*. (Già presente nel Vault: copre l'uso del BIM per la gestione dei costi nell'intero ciclo di vita).
3. **Niemioja, S., et al.** *"Classification of cost data and its use in 5D BIM"*. (Da ricercare/ingerire: affronta le sfide pratiche nell'aggiornamento dei cataloghi di costo durante le iterazioni di design).

---

## 3. Sincronizzazione 4D/5D per il Controllo delle Varianze Costi-Tempi in Fase Esecutiva

### Struttura Scientifica
- **Obiettivo della Ricerca:** Testare la capacità del modello 5D BIM di assorbire e gestire dinamicamente gli imprevisti di cantiere (varianti in corso d'opera, ritardi nelle forniture) per evitare l'esplosione dei costi.
- **Metodologia (Workflow):**
  1. *4D/5D Integration:* Collegamento del modello 3D (Revit) con il cronoprogramma (Primavera P6 o MS Project) e con i costi all'interno di un software di cantierizzazione (es. Navisworks Manage o Synchro 4D).
  2. *Simulation:* Simulazione del "resource-loaded schedule" (cronoprogramma caricato di costi e risorse) di un cantiere reale o teorico.
  3. *Variance Testing:* Iniezione di "fattori di disturbo" (es. ritardo di 10 giorni in una lavorazione chiave) per analizzare come il sistema ricalcoli in automatico le conseguenze su tempi (Earned Value) e costi.
- **Risultato Atteso:** Validazione del 5D BIM come "digital twin" gestionale per il cantiere, misurando l'efficienza nel tracciamento della varianza (Planned Value vs Actual Cost).

### 📚 Paper Consigliati per Ingestione (NotebookLM)
1. **Elsheikh, A., Saqr, A., Motawa, I. (2025).** *"BIM-Based Integrated Model for Project Cost Estimation: A Case Study for Concrete Elements"*. (Già presente nel Vault: eccellente framework per l'automazione dello scheduling 4D/5D).
2. **Autori Vari.** *"BIM-Based Cost Estimation Monitoring For Building Construction"*. (Già presente nel Vault: focus specifico sul monitoraggio e controllo della varianza durante la fase esecutiva).
3. **Autori Vari.** *"An Innovative Framework of 5D BIM Solutions for Construction Cost Management"*. (Già presente nel Vault: fornisce soluzioni avanzate per l'integrazione del controllo costi nei pagamenti e stati di avanzamento lavori).
