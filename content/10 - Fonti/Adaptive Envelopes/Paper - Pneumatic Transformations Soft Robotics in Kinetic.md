---
tags:
  - source
  - pdf
autore: Alexander Urban
anno: 2025
titolo: "Pneumatic Transformations Soft Robotics in Kinetic Spatial Structures"
---

# 📄 Fonte: Pneumatic Transformations Soft Robotics in Kinetic Spatial Structures

## Metadati
- **Titolo:** Pneumatic Transformations Soft Robotics in Kinetic Spatial Structures
- **Autori:** Alexander Urban
- **Anno:** 2025
- **Notebook Originale:** [[Notebook - Adaptive Envelopes]]

## Sintesi Estesa

### 1. Obiettivi
Lo scopo principale della ricerca è sfidare la convenzione secondo cui l'architettura debba essere un'entità statica e immutabile. L'autore intende esplorare il potenziale di uno spazio in costante mutamento, concepito come un sistema attivo capace di reagire fisicamente alla presenza umana. Il problema centrale affrontato è l'indagine filosofica e pratica sulla "proprietà dello spazio" (ownership): può una macchina rivendicare autorità su uno spazio fisico e costringere l'uomo a cederlo? Per rispondere a questa domanda, l'obiettivo pratico è progettare, prototipare e realizzare un'installazione spaziale cinetica e interattiva, basata sui principi della soft robotics e composta da volumi pneumatici (airbags) che si gonfiano e si sgonfiano in risposta alla vicinanza degli utenti, agendo come entità territoriali autonome.

### 2. Metodologia
La ricerca è stata condotta attraverso un approccio interdisciplinare (architettura, ingegneria meccanica/elettrica e informatica) basato su una forte componente di prototipazione iterativa (Research by Design). La metodologia si è articolata in diverse fasi:
- Fabbricazione dei corpi pneumatici: Inizialmente, l'autore ha testato modelli in silicone colati in stampi stampati in 3D, seguendo i dettami classici della soft robotics. A causa di costi, peso e problemi di perdite d'aria su larga scala, la metodologia è passata all'uso di fogli di plastica. Dopo aver scartato la saldatura a caldo e ad alta frequenza per difficoltà tecniche, l'autore ha validato l'uso di fogli di LDPE traslucido riciclato, uniti con successo tramite nastro adesivo universale.
- Sviluppo Hardware e Software: È stata progettata e costruita una ventola intubata bidirezionale personalizzata, utilizzando componenti stampati in 3D e motori DC brushless. Il sistema di controllo logico è stato programmato tramite l'ambiente di programmazione visiva MAX/MSP.
- Grandezza del campione e Validazione: La validazione finale è avvenuta testando un prototipo in scala reale in tre diversi contesti spaziali: un grande atrio ben illuminato, un piccolo soggiorno e una stanza buia con luci stroboscopiche. Le osservazioni qualitative sulle reazioni umane sono state condotte su un campione esplicitamente dichiarato di 5 partecipanti.

### 3. Limiti della Ricerca (Limitations)
Nel documento vengono dichiarate esplicitamente diverse criticità e limitazioni, sia di natura tecnologica che metodologica:
- Limiti Tecnologici (Sensori e Posizionamento): Il sistema di tracciamento Ultra-Wideband (UWB) scelto per rilevare la prossimità umana ha fallito a causa di problemi microelettronici. Di conseguenza, durante i test, la prossimità è stata tracciata manualmente dall'autore utilizzando un gamepad.
- Limiti Tecnologici (Hardware): Il controller del motore della ventola è andato in blocco di sicurezza superato il 10% della velocità a causa della scarica profonda del pacco batterie agli ioni di litio; il sistema ha dovuto essere testato con un alimentatore diretto. Inoltre, le strisce LED integrate nei condotti si sono rivelate troppo deboli per essere visibili in ambienti ben illuminati. Durante lo sgonfiaggio ad alta velocità, il foglio in LDPE veniva occasionalmente risucchiato contro la griglia della ventola, bloccando il flusso d'aria.
- Limiti Metodologici: L'autore dichiara esplicitamente che il campione di 5 partecipanti è troppo piccolo per trarre conclusioni generali e scientificamente inconfutabili sul comportamento umano. Infine, il materiale LDPE, pur essendo economico, ha mostrato pieghe permanenti dopo i cicli di gonfiaggio, rendendolo inadatto per installazioni non supervisionate a lungo termine o all'aperto.

### 4. KPI e Risultati Misurati
Il paper riporta i seguenti dati quantitativi e risultati qualitativi:
- Dati Quantitativi (Prototipo Finale): Il volume pneumatico finale in LDPE da 100 µm misurava 3 metri di diametro e 6 metri di altezza. Il volume totale raggiunto era di 21,7 m³, con una superficie di 56,5 m² e un peso di soli 5,2 kg.
- Dati Quantitativi (Test preliminari): Un prototipo intermedio in LDPE da 45 µm (2,85 m³) è stato gonfiato completamente in circa 4 minuti registrando una portata volumetrica di 0,019 m³/s.
- Risultati Qualitativi (Successo): L'installazione ha avuto successo nel suo intento concettuale primario: i partecipanti si sono sistematicamente spostati e hanno ceduto lo spazio quando l'airbag si espandeva, dimostrando fisicamente la "negoziazione" del territorio con l'entità artificiale. L'unione dei fogli di LDPE tramite nastro adesivo si è dimostrata robusta ed efficace per un'esposizione temporanea.
- Risultati Qualitativi (Atmosfera): Il successo dell'impatto emotivo è variato in base all'ambiente: nell'atrio grande l'oggetto era percepito come neutrale; nel soggiorno piccolo l'impatto acustico della ventola e la costrizione fisica hanno generato la sensazione autoritaria desiderata; nella stanza buia con stroboscopio l'effetto è stato descritto come intenso, disorientante e stressante.

### 5. Sviluppi Futuri
Alla fine del documento, l'autore propone una chiara roadmap per i futuri filoni di indagine:
- Obiettivi a breve termine: Risolvere i problemi del sistema UWB progettando PCB personalizzati e alloggiamenti stampati in 3D. Riparare i problemi del pacco batteria della ventola e implementare interruttori di finecorsa o protezioni meccaniche. L'obiettivo imminente è espandere l'installazione a tre oggetti completi per testarli in scenari espositivi reali.
- Obiettivi a lungo termine: Sostituire l'LDPE con materiali molto più durevoli, come PVC saldato o fogli in TPU elastico, per consentire esposizioni permanenti. Migliorare il sistema di illuminazione interna con LED più potenti. Semplificare l'architettura IoT per permettere la manutenzione a personale non tecnico.

### 6. Conclusioni
In sintesi, il documento fornisce un contributo altamente sperimentale e innovativo al campo dell'architettura cinetica e dell'arte interattiva. Combinando la costruzione di strutture pneumatiche con l'elettronica, la programmazione e i protocolli IoT, la tesi dimostra che lo spazio architettonico non deve essere necessariamente un contenitore passivo, ma può essere ingegnerizzato per comportarsi come un agente sociale attivo. Nonostante le sfide tecniche, la realizzazione fisica del prototipo certifica che è possibile utilizzare materiali poveri, leggeri e accessibili integrati con componenti meccatroniche ibride per generare architetture adattive su larga scala. La ricerca apre nuove prospettive su come il flusso d'aria e le trasformazioni di forme biomimetiche possano manipolare la percezione psicologica dell'autorità e della proprietà spaziale.

## Concetti Chiave
- [[Architettura Cinetica e Soft Robotics]]
- [[Strutture Pneumatiche Interattive]]

## Bibliografia Rilevante
1. Nel testo non vengono citate altre fonti bibliografiche specifiche.

---
[[Casestudy - Pneumatic Transformations]]
