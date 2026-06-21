---
draft: true
tags:
  - tesi
  - 5D_BIM
  - approfondimento
  - cantierizzazione
  - 4D_BIM
  - earned_value
---

# 🎓 Proposta di Tesi 3: Sincronizzazione 4D/5D per il Controllo delle Varianze Costi-Tempi in Fase Esecutiva

## 1. Stato dell'Arte e Problematica

### Il Contesto Internazionale
A livello internazionale, specialmente nei progetti infrastrutturali e nei grandi complessi civili, l'approccio 4D/5D è considerato il cuore del controllo in fase di esecuzione. Metodologie come l'**Earned Value Management (EVM)** sono nativamente integrate nei workflow digitali: un modello "caricato di risorse" (*resource-loaded model*) funge da vero e proprio *Digital Twin* gestionale, permettendo di incrociare continuamente il Piano Finanziario Previsto (Planned Value) con il Lavoro Effettivamente Svolto (Earned Value) e i Costi Reali Sostenuti (Actual Cost).

### Il Contesto Italiano e le Problematiche di Cantiere
In Italia, la fase esecutiva è storicamente il "tallone d'Achille" del settore delle costruzioni. I cantieri italiani soffrono endemicamente di inefficienze, ritardi nelle forniture, imprevisti e varianti in corso d'opera (spesso generate da progetti esecutivi carenti o sopraggiunte esigenze della Committenza). 
Il controllo direzionale è spesso destrutturato: il controllo tempi si basa su diagrammi di Gantt statici (raramente aggiornati in tempo reale), e la contabilità di cantiere avviene "a posteriori", tramite la redazione manuale dello Stato Avanzamento Lavori (SAL) sui libretti delle misure.
Quando si verifica un imprevisto, l'impatto a cascata su tempi e costi viene compreso solo quando il danno è ormai compiuto, rendendo quasi impossibile l'attuazione di strategie correttive. L'incapacità di prevedere dinamicamente gli scostamenti genera conflitti contrattuali, penali e l'esplosione dei budget iniziali.

---

## 2. Obiettivo della Ricerca

L'obiettivo della tesi è validare la capacità predittiva e diagnostica di un modello 5D BIM utilizzato attivamente durante la cantierizzazione.
In sintesi, si intende:
1. Testare la prontezza del modello nell'assorbire e gestire dinamicamente i classici imprevisti del cantiere italiano.
2. Trasformare il monitoraggio retrospettivo del SAL in una metodologia predittiva per la mitigazione del rischio, calcolando l'esplosione dei costi *prima* che la variante generi ritardi critici.

---

## 3. Metodologia Dettagliata

La ricerca si focalizzerà esclusivamente sulla fase esecutiva e sulla simulazione della cantierizzazione. Verranno implementati i seguenti passaggi:

*   **Fase 1: Integrazione 4D/5D (Resource-Loaded Schedule)**
    *   Partendo da un modello BIM esecutivo (LOD E / LOD 400), si collegheranno gli oggetti 3D alle attività di un cronoprogramma (elaborato in MS Project o Primavera P6).
    *   Si utilizzerà un software di simulazione cantieristica (es. Synchro 4D, Navisworks Manage o Bexel Manager) per assegnare a ciascuna attività le risorse di manodopera, noli e materiali (costi).
*   **Fase 2: Baseline Simulation**
    *   Simulazione della "Baseline", ovvero del cantiere teorico perfetto senza imprevisti, estraendo la curva S del Budget Cost of Work Scheduled (Planned Value).
*   **Fase 3: Variance Testing (Stress Test)**
    *   Si inietteranno intenzionalmente due "fattori di disturbo" tipici del contesto locale. Ad esempio:
        *   Disturbo A: Ritardo di 15 giorni nella fornitura di un elemento critico (es. infissi speciali o travi prefabbricate).
        *   Disturbo B: Variante in corso d'opera richiesta dal committente (es. modifica sostanziale degli impianti in un blocco dell'edificio).
    *   Analisi della risposta del sistema: ricalcolo automatico del percorso critico e degli indici di performance dei costi e dei tempi (Cost Performance Index - CPI; Schedule Performance Index - SPI).

---

## 4. Risultati Attesi

### 4.1 Risultato Generale (Teorico e Metodologico)
*   **Validazione del Digital Twin Gestionale:** Dimostrazione di come l'impalcatura metodologica del 5D BIM rappresenti un salto evolutivo necessario dal *project management* tradizionale alla gestione parametrica e dinamica del cantiere.
*   **Dimostrazione dell'Efficacia del BIM-based EVM:** Conferma dell'applicabilità dell'Earned Value Management in ambito edile italiano, spesso ritenuto inapplicabile per la troppa instabilità dei nostri cantieri.

### 4.2 Risultati Secondari (Pratici e Operativi)
*   **Cruscotto di Monitoraggio (Dashboard):** Creazione di una dashboard visiva esportabile per la Direzione Lavori e la Committenza, capace di mostrare lo stato di salute economico/temporale del cantiere in un ambiente intuitivo a colori (semplificando la lettura dei dati grezzi).
*   **Protocollo per le Varianti:** Stesura di una breve *best practice* procedurale su come codificare e inserire le varianti in corso d'opera nel modello 5D senza distruggere i link preesistenti tra Gantt, modello e contabilità.

---

## 5. Bibliografia di Riferimento (Testi Rilevanti)

Per formare la base metodologica della tesi, ecco 5 articoli scientifici focalizzati sulla cantierizzazione 4D/5D e la gestione dei SAL:

1. **Elsheikh, A., Saqr, A., Motawa, I. (2025).** *"BIM-Based Integrated Model for Project Cost Estimation: A Case Study for Concrete Elements"*. (Eccellente framework logico per automatizzare l'integrazione del cronoprogramma con le quantità).
2. **Autori Vari (2023/2024).** *"BIM-Based Cost Estimation Monitoring For Building Construction"*. (Specifico sul monitoraggio esecutivo e il rilevamento delle varianze durante la costruzione).
3. **Pishdad, P., & Onungwa, I. O. (2024).** *"An Innovative Framework of 5D BIM Solutions for Construction Cost Management"*. (Si spinge fino alla strutturazione dei pagamenti intermedi e SAL tramite BIM).
4. **Chen, Q., & Lu, M. (2022/2023).** *"Automated 4D/5D BIM for Earned Value Management in Construction"*. (Testo accademico cruciale per l'incrocio tra tecniche di EVM e dati tridimensionali).
5. **Autori Vari (2021).** *"Integration of BIM and Primavera P6 for effective 5D scheduling"*. (Analisi pratica sulle sfide tecnologiche nell'uso combinato di software di scheduling puro e ambienti BIM).
