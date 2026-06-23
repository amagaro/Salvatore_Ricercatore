---
tags:
  - source
  - pdf
autore: N/A
anno: N/A
titolo: "Responsive Composites"
---

# 📄 Fonte: Responsive Composites

## Metadati
- **Titolo:** Responsive Composites (2020_ResponsiveComposites_PLEA2020_Proc_Vol2_VF_IWF.pdf)
- **Autori:** N/A
- **Anno:** 2020
- **Notebook Originale:** [[Notebook - Adaptive Envelopes]]

## Sintesi Estesa

### 1. Obiettivi
Lo scopo principale della ricerca è esplorare e sviluppare nuovi metodi di progettazione integrata per l'implementazione di materiali attivi e responsivi nel settore delle costruzioni, focalizzandosi in particolare su superfici architettoniche dotate di responsività termica intrinseca. Il problema fondamentale che gli autori intendono risolvere è l'impatto ambientale critico del comparto edile, responsabile fino al 50% delle emissioni globali di CO2 se si include l'intero ciclo di vita. A differenza delle facciate dinamiche tradizionali, che si affidano a sistemi meccanici complessi, costosi ed energivori controllati digitalmente, questa ricerca mira a sviluppare "compositi edilizi responsivi basati sull'exergia" (exergy-based responsive building composites) sfruttando le proprietà anisotropiche e igroscopiche del legno. L'obiettivo è creare un involucro edilizio capace di adattarsi passivamente alle variazioni termiche, ottimizzando l'efficienza energetica senza la necessità di un'alimentazione elettrica continua o di complessi meccanismi attuativi.

### 2. Metodologia
La ricerca è stata condotta adottando un metodo sperimentale ibrido, che integra la prototipazione fisica dei materiali con metodologie di simulazione computazionale ad alta risoluzione. A livello materiale, sono stati utilizzati fogli di tranciato di rovere (quarter-cut oak veneer) con uno spessore di 0,6 mm, scelti per la loro elevata resistenza, omogeneità e l'alto coefficiente di espansione termica tangenziale agli anelli di crescita. Sono stati testati tre gruppi di compositi: elementi a singolo strato, compositi a doppio strato (con direzioni delle fibre opposte e giunti a scatto in PLA), e materiali a gradazione funzionale (FGM) multi-fibra. Le prove fisiche sono state eseguite in una camera climatica personalizzata dotata di un radiatore termico da 1000 Watt, un umidificatore a ultrasuoni e un microcontrollore Arduino per programmare cicli di attivazione ripetibili, portando la temperatura a 38 °C e mantenendo l'umidità relativa al 30%. La validazione del comportamento è avvenuta tracciando la deformazione fisica in tempo reale tramite una telecamera a infrarossi (Kinect V2), esportando i dati in una nuvola di punti. Dal punto di vista computazionale, il team ha sviluppato modelli parametrici (in Grasshopper e Rhinoceros, utilizzando il solutore fisico Kangaroo 2 basato su molle) per simulare il comportamento di piegatura e gli stress strutturali prima della fabbricazione. Infine, l'intero sistema è stato validato realizzando un dimostratore architettonico in scala reale (un'installazione di 2 x 3 metri).

### 3. Limiti della Ricerca (Limitations)
Nel documento vengono dichiarati esplicitamente diversi limiti legati alla ricerca e alla tecnologia dei materiali proposti. In primis, gli autori affermano che il caso studio rappresenta un'indagine limitata ("a limited enquiry") e che sarà necessario ulteriore lavoro per valutare le prestazioni di questi compositi su scale e campioni più ampi e differenziati. Dal punto di vista tecnologico, viene evidenziata una criticità fondamentale legata alla natura organica del legno: un'esposizione eccessiva o una distribuzione irregolare del calore (ad esempio a causa della radiazione UV attraverso le venature) può causare una distribuzione non uniforme degli sforzi nel sistema. Questo fenomeno rischia di provocare danni microstrutturali (deformazioni plastiche permanenti) e una riduzione complessiva della reattività nel tempo, portando a un affaticamento del materiale (material fatigue) che incide negativamente sulla vita operativa della facciata. Infine, vi è un limite metodologico per la fabbricazione: per garantire prestazioni coerenti, è richiesta una rigorosa misurazione del contenuto di umidità intrinseco del legno e un severo controllo dei parametri ambientali durante l'intera fase di produzione.

### 4. KPI e Risultati Misurati
Il paper elenca in modo puntuale i seguenti dati quantitativi e qualitativi derivanti dalle misurazioni e dalle sperimentazioni effettuate:
- Specifiche e Resistenza del materiale (KPI): Il tranciato di rovere scelto ha uno spessore di 0,6 mm, con un modulo elastico di resistenza misurato in E=343N/mm2 e un coefficiente di espansione termica tangenziale del 11,9%.
- Ambiente di test (KPI): I cicli di attivazione hanno operato a una temperatura massima di 38 °C, con un'umidità relativa costante del 30%.
- Dimostratore fisico (KPI): È stata assemblata con successo una struttura di 2 x 3 metri formata da 50 elementi reattivi multistrato. Il sistema è basato su celle sovrapposte di 300 x 300 mm tenute insieme da giunti a scatto.
- Risultato qualitativo (Comportamento direzionale): La direzione delle fibre del legno è stata confermata come il fattore principale e assoluto per guidare la direzione della piegatura termica.
- Risultato qualitativo/quantitativo (Spessore e reattività): I campioni di materiale più spesso hanno richiesto più tempo per convertire il calore in espansione termica, ma si sono rivelati in grado di resistere alle forze di deformazione per periodi più lunghi. I campioni più lunghi tagliati perpendicolarmente alla venatura hanno ottenuto cambiamenti di curvatura marcatamente maggiori.
- Successo dei FGM: Mentre i pannelli a singolo e doppio strato hanno fornito solo curvature unidirezionali, l'utilizzo di materiali a gradazione funzionale (FGM) ha permesso di ottenere con successo piegature funzionali multi-direzionali, unendo un'elevata rigidità a una complessa variazione di forma.

### 5. Sviluppi Futuri
Gli autori delineano vari filoni di indagine futuri per superare le limitazioni attuali e ottimizzare i sistemi. Si propone l'impiego della fabbricazione robotica per la produzione dei compositi responsivi: questo permetterebbe un controllo ad altissima risoluzione sulle specifiche del materiale, ottimizzando la distribuzione delle fibre in un'ottica "build-per-requirement" che aumenterebbe l'efficienza economica ed ecologica. Inoltre, si suggerisce di superare il solo utilizzo del legno orientandosi verso una stratificazione multi-materiale, in grado di introdurre nuove e inedite proprietà ibride nei sistemi architettonici responsivi. Infine, si evidenzia la necessità di sviluppare ulteriormente i flussi di lavoro digitali, creando modelli predittivi capaci di anticipare in modo affidabile i cambiamenti comportamentali e le incoerenze del sistema dopo numerosi cicli operativi a lungo termine.

### 6. Conclusioni
In sintesi, il documento fornisce un contributo innovativo all'architettura sostenibile, dimostrando che è possibile progettare involucri edilizi adattivi rinunciando a sensori e attuatori meccatronici tradizionali in favore dell'intelligenza materiale intrinseca. Utilizzando le proprietà anisotropiche e termo-espansive del legno, la ricerca prova che la materia può agire contemporaneamente come sensore, motore e struttura. La creazione di compositi multistrato, in particolare i FGM (Functionally Graded Materials), permette di superare i limiti dimensionali dei classici tranciati in legno, offrendo moduli rigidi capaci di piegarsi in molteplici direzioni come risposta ai cambiamenti termici. Il successo della ricerca risiede nell'aver consolidato un workflow ibrido "design-to-production": i modelli computazionali sviluppati riescono a prevedere e controllare con alta precisione le deformazioni organiche della materia, offrendo ai progettisti un quadro di riferimento affidabile per costruire schermature solari e facciate cinetiche a energia zero (exergy-based), segnando un importante passo verso la riduzione dell'impronta carbonica degli edifici.

## Concetti Chiave
- [[Compositi Edilizi Responsivi]]
- [[Materiali a Gradazione Funzionale (FGM)]]

## Bibliografia Rilevante
1. Nel testo non vengono citate altre fonti bibliografiche specifiche.

---
[[Casestudy - Exergy-based Responsive Composites Prototype]]
