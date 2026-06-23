---
tags:
  - source
  - pdf
autore: N/A
anno: N/A
titolo: "An adaptive Industrial Internet of things (IIOts) based technology for prediction and control of cavitation in centrifugal pumps"
---

# 📄 Fonte: An adaptive Industrial Internet of things (IIOts) based technology for prediction and control of cavitation in centrifugal pumps

## Metadati
- **Titolo:** An adaptive Industrial Internet of things (IIOts) based technology for prediction and control of cavitation in centrifugal pumps (1-s2.0-S2212827120309240-main.pdf)
- **Autori:** N/A
- **Anno:** N/A
- **Notebook Originale:** [[Notebook - Adaptive Envelopes]]

## Sintesi Estesa

### 1. Obiettivi
Lo scopo principale della ricerca è simulare, prevedere e controllare il fenomeno della cavitazione all'interno delle pompe centrifughe industriali sfruttando le tecnologie dell'Industrial Internet of Things (IIoT). La cavitazione, un processo dinamico che comporta la formazione, la crescita e la successiva implosione di bolle d'aria sulle pale della girante a causa di una pressione di aspirazione insufficiente, genera livelli elevati di rumore, vibrazioni e, a lungo termine, una grave corrosione dei componenti. Il problema centrale che gli autori intendono risolvere è l'inefficienza degli attuali dispositivi di monitoraggio. Pertanto, la ricerca si pone l'obiettivo di sviluppare un sistema intelligente in grado di raccogliere dati telemetrici sonori, inviarli in cloud e processarli tramite algoritmi di Machine Learning per riconoscere e classificare i pattern di cavitazione rispetto ai normali rumori ambientali. I risultati mirano ad assistere i produttori nella mitigazione del problema fin dalla fase di progettazione e a fornire un controllo di processo efficace durante le normali operazioni industriali.

### 2. Metodologia
La ricerca è stata condotta attraverso la progettazione e la calibrazione di un banco di prova sperimentale (test rig) ibrido, composto da componenti meccanici ed elettronici. La parte meccanica comprende un motore elettrico AC da 0.5 hp accoppiato a una pompa centrifuga operante a 2850 rpm, un serbatoio rettangolare in Teflon, tubazioni in PVC e una valvola a sfera posta in aspirazione per regolare il flusso. La parte elettronica è costituita da un'architettura IIoT basata su un microcontrollore Arduino Uno interfacciato con sensori sonori (microfoni ad elettrete con amplificatore). L'esperimento ha simulato le condizioni di flusso utilizzando acqua a 25 °C, inducendo variazioni di portata tramite l'apertura graduale della valvola a sfera mantenendo costante la velocità di rotazione. I segnali acustici ambientali e vibrazionali generati dalla girante (nel range di frequenza 0-1 kHz) sono stati acquisiti in tempo reale e convertiti in segnali elettrici. Tali dati sono stati elaborati utilizzando l'algoritmo Fast Fourier Transform (FFT). Successivamente, i dati sono stati inviati in cloud e analizzati mediante una Rete Neurale Artificiale (Artificial Neural Network - ANN), impiegata come algoritmo di machine learning per classificare in modo netto i modelli con e senza cavitazione. Per garantire l'affidabilità statistica, il test sperimentale è stato ripetuto per cinque volte consecutive.

### 3. Limiti della Ricerca (Limitations)
Nel paper vengono dichiarate esplicitamente pochissime criticità. L'unico limite metodologico e di scopo indicato formalmente dagli autori è che il presente lavoro "è limitato alla previsione della cavitazione" ("This work is limited to prediction of cavitation"), omettendo la determinazione empirica diretta di altre prestazioni fondamentali della pompa durante il test, come ad esempio la prevalenza totale (pump head) o misurazioni fluidodinamiche complesse. Nel testo non vengono riportati altri limiti tecnologici (ad esempio tassi di errore dell'algoritmo ANN o latenze di trasmissione nel sistema IIoT), in quanto l'esperimento viene considerato una prova di fattibilità riuscita e convalidata dai segnali elettrici.

### 4. KPI e Risultati Misurati
Il documento riporta in modo puntuale diversi risultati di successo quantitativi e qualitativi, derivanti sia dai calcoli fluidodinamici preventivi sia dai dati telemetrici catturati dal sistema IIoT:
- KPI Meccanici calcolati: La velocità del flusso all'interno del sistema è stata calcolata a 3.79 m/s. Il tasso di flusso volumetrico (discharge) si è attestato a 1.92×10−3 m3/s. Il Numero di Reynolds calcolato è 63.375, indicando un flusso spiccatamente turbolento. L'efficienza calcolata del motore della pompa è del 67.8%.
- Risultati di successo (Pattern di Non-Cavitazione): Con la valvola a sfera aperta a 90°, nei regimi operativi inferiori alla portata di progetto o normali, i segnali di tensione registrati dai sensori sonori si attestano in un intervallo compreso tra 0.5 e 0.75 V (riportato anche fino a 0.79 V nel dettaglio dell'analisi). Le fluttuazioni in questo range sono attribuite al normale rumore ambientale.
- Risultati di successo (Pattern di Cavitazione): Quando la portata supera i limiti di progetto, generando alta interazione tra fluido e pale (implosione di bolle), si verifica un incremento significativo dell'ampiezza di vibrazione. In questo scenario, i segnali elettrici misurati salgono e si concentrano in un range compreso tra 0.76 e 0.95 V (riportato fino a 0.99 V nel grafico di dettaglio). L'integrazione di sensori sonori e algoritmo FFT ha quindi dimostrato con successo di poter tracciare e isolare il momento esatto dell'innesco della cavitazione in tempo reale.

### 5. Sviluppi Futuri
Al termine del documento, gli autori raccomandano specifici filoni di indagine per implementare e affinare la tecnologia proposta:
- L'integrazione nel sistema IIoT di ulteriori tipologie di sensori (nello specifico sensori di pressione e sensori di temperatura), che permetterebbero di migliorare ulteriormente la precisione predittiva all'innesco del fenomeno cavitazionale. A tal fine viene suggerito l'uso di trasduttori di pressione posti sui lati di aspirazione e scarico.
- L'adozione di un modulo Bluetooth/Wi-Fi dedicato per inviare i segnali di allarme e i dati direttamente allo smartphone dell'operatore industriale.
- L'aggiunta di una videocamera per monitorare visivamente e fisicamente la cavitazione, in modo da incrociare i dati acustici con quelli visivi per ottenere risultati ancora più accurati.

### 6. Conclusioni
In sintesi, il documento fornisce un contributo pragmatico al campo dell'ingegneria meccanica e della diagnostica predittiva, dimostrando che è possibile prevedere e simulare la cavitazione nelle pompe centrifughe attraverso un'architettura economica e scalabile basata sull'Internet of Things. La ricerca ha validato che l'analisi in frequenza dei segnali sonori (tramite FFT e reti neurali) rappresenta un indicatore estremamente affidabile: i pattern di rumore si convertono in voltaggi distinti che separano chiaramente i regimi di flusso stabili da quelli critici. Si conclude, infine, che la cavitazione è una funzione diretta della portata del fluido, la quale è più problematica sul lato di aspirazione; la sua mitigazione operativa può essere ottenuta non solo digitalmente, ma anche fisicamente, inserendo ostacoli per ottimizzare la struttura del flusso e indebolire l'intensità del vortice in prossimità della voluta della pompa.

## Concetti Chiave
- [[IIoT per Involucri e Impianti]]

## Bibliografia Rilevante
1. Nel testo non vengono citate altre fonti bibliografiche specifiche.

---
[[Casestudy - IIoT Cavitation Prediction]]
