import os

fonti_dir = r"d:\Vaults\Research\Research\10 - Fonti\Adaptive Envelopes"
casi_dir = r"d:\Vaults\Research\Research\30 - Casi di studio\Adaptive Envelopes"
concept_dir = r"d:\Vaults\Research\Research\20 - Concepts\Adaptive Envelopes"

os.makedirs(fonti_dir, exist_ok=True)
os.makedirs(casi_dir, exist_ok=True)
os.makedirs(concept_dir, exist_ok=True)

paper1 = """---
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
"""

paper2 = """---
tags:
  - source
  - review
autore: Pengyuan Shen, Xiaoni Gao, Shuai Lu, Yi Zhang, Xing Zheng, Matthaios Santamouris
anno: 2026
titolo: "How AI Shapes the Future Landscape of Sustainable Building Design With Climate Change Challenges?"
---

# 📄 Fonte: How AI Shapes the Future Landscape of Sustainable Building Design With Climate Change Challenges?

## Metadati
- **Titolo:** How AI Shapes the Future Landscape of Sustainable Building Design With Climate Change Challenges?
- **Autori:** Pengyuan Shen, Xiaoni Gao, Shuai Lu, Yi Zhang, Xing Zheng, Matthaios Santamouris
- **Anno:** 2026
- **Notebook Originale:** [[Notebook - Adaptive Envelopes]]

## Sintesi Estesa

### 1. Obiettivi
L'urgenza di una progettazione architettonica sostenibile è sempre più pressante a causa delle sfide poste dal rapido riscaldamento globale e dall'urbanizzazione. Gli edifici contribuiscono al 35% del consumo energetico mondiale e al 40% delle emissioni di gas serra. In questo panorama, l'intelligenza artificiale (AI), tramite foundation models (Modelli Fondazionali) e Large Language Models (LLM), offre un nuovo paradigma per rivoluzionare i processi di design. A differenza della tradizionale computazione parametrica, l'obiettivo di questa estesa revisione narrativa della letteratura (comprendente 116 pubblicazioni post-2020) è esplorare come l'AI stia guidando una transizione molto più profonda. Lo scopo principale è fornire una panoramica su come i sistemi generativi avanzati e multimodali possano interpretare dati climatici dinamici per generare design adattivi che non si basano solo su condizioni climatiche passate ma anticipano quelle future, per raggiungere una vera resilienza climatica nell'architettura sostenibile.

### 2. Metodologia
Lo studio applica un approccio narrativo strutturato esaminando la letteratura in quattro macro-aree:
1. **Stato dell'arte delle applicazioni AI** nel design architettonico clima-responsivo.
2. **Effetti trasformativi** dei modelli fondazionali (LLMs, sistemi Generativi Multi-Modali) nei confronti dei "climate stressors" (fattori di stress climatico) futuri, non prevedibili con i file climatici standardizzati (es. file epw classici).
3. **Framework operativi** per l'integrazione, portando allo sviluppo e alla proposizione del Framework ACBI (AI-Climate-Building Integration).
4. **Ostacoli, policy e direzioni future** per un uso etico, sicuro e funzionale delle intelligenze artificiali nell'edilizia green.
I KPI monitorati nello studio risiedono nella capacità dell'AI di gestire grandi set di variabili interdipendenti (es. surriscaldamento urbano, consumi idrici, esposizione e orientamento) durante le fasi concettuali e performative del design. Inoltre l'attenzione è stata rivolta al "reboud effect" dell'utilizzo dell'AI stessa (consumi energetici dei data center addestratori versus l'energia risparmiata dall'ottimizzazione degli edifici).

### 3. Conclusioni
La conclusione primaria evidenzia che l'AI cambierà radicalmente la pratica architettonica introducendo capacità predittive non stazionarie. Il Framework ACBI si fonda su tre pilastri: 
a) Integrazione Tecnica (accoppiamento dinamico delle informazioni e modelli Building Information Modeling, BIM semantico); 
b) Risposta Climatica (previsione e risposta adattiva agli stressor futuri basati su scenari IPPC); 
c) Governance (gestione del rischio, standardizzazione, e regolamenti come l'EU AI Act).
**Limiti:** Viene sottolineato il limite insito nei consumi "nascosti" dell'AI (il Green AI dilemma): i LLM consumano molta acqua e moltissima elettricità per l'inferenza, minacciando parte del saving generato. C'è inoltre un rischio di "allucinazione" progettuale, in cui l'AI generativa crea involucri dall'estetica eccezionale ma privi di fattibilità costruttiva o correttezza termodinamica. Un ulteriore ostacolo è la difficile standardizzazione dei dati ("data silos") tra vari professionisti.
**Sviluppi Futuri:** La ricerca dovrà focalizzarsi sul perfezionamento dei "Foundation Models" nativamente educati sulla fisica delle costruzioni (Physics-Informed Neural Networks), migliorando l'interpretabilità dei risultati. Nel futuro si attendono digital twins intelligenti, auto-calibranti e multi-modali (interpreti di testo, planimetrie, diagrammi 3D) per ottimizzare dinamicamente in tempo reale l'involucro edilizio (es. schermature mobili, set point HVAC) per l'adattamento ai cambiamenti climatici imprevedibili in arrivo.

## Concetti Chiave
- [[AI-Climate-Building Integration Framework (ACBI)]]
- [[Physics-Informed Foundation Models per l'Architettura]]

## Bibliografia Rilevante
1. Li, L. et al. "An AI-Driven Model for Predicting and Optimizing Energy-Efficient Building Envelopes" (2023)
2. Forth, K. and Borrmann, A. "Semantic Enrichment for BIM-Based Building Energy Performance Simulations Using Semantic Textual Similarity and Fine-Tuning Multilingual LLM" (2024)

---
"""

paper3 = """---
tags:
  - source
  - paper
autore: Long Zhang, Jianhui Gong, Cuinan Wu, et al.
anno: 2026
titolo: "Research on time series prediction of microclimate in agrivoltaic systems based on the long short-term memory and attention mechanism"
---

# 📄 Fonte: Research on time series prediction of microclimate in agrivoltaic systems based on the long short-term memory and attention mechanism

## Metadati
- **Titolo:** Research on time series prediction of microclimate in agrivoltaic systems based on the long short-term memory and attention mechanism
- **Autori:** Long Zhang, Jianhui Gong, Cuinan Wu, Erik Harry Murchie, Alexandra Jacquelyn Gibbs, Bingbing Liu, Chen Yang, Guijun Xu, Jinxin Zhang, Jiguang Guo, Maohua Xiao, Encai Bao
- **Anno:** 2026
- **Notebook Originale:** [[Notebook - Adaptive Envelopes]]

## Sintesi Estesa

### 1. Obiettivi
I sistemi Agrivoltaici (AV) uniscono la produzione di energia fotovoltaica (PV) con le attività agricole sullo stesso terreno, introducendo però una complessa variazione spaziale e temporale del microclima dovuta all'ombreggiamento imposto dai pannelli. Tali variazioni incidono fortemente sull'efficienza fotosintetica, sullo stress termico e sulla resa complessiva dei raccolti, evidenziando il ruolo dell'involucro "adattivo" agricolo. Lo studio ha l'obiettivo primario di prevedere con altissima accuratezza i parametri microclimatici critici (in particolare l'intensità della radiazione solare e la temperatura dell'aria) in sistemi AV in campo aperto, elaborando modelli capaci di affrontare le limitazioni tipiche degli approcci stazionari, dei lunghi tempi di calcolo della CFD (Computational Fluid Dynamics) o dell'errore previsionale crescente tipico delle serie temporali lunghe. A questo scopo viene proposto un modello Long Short-Term Memory accoppiato a meccanismi di Attenzione (LSTM-Attention).

### 2. Metodologia
I ricercatori hanno strutturato l'indagine presso il parco sperimentale Agrivoltaico di Nanchino (Nanjing, Cina), installazione di 47 ettari equipaggiata con sensori avanzati. La metodologia segue una rotta fortemente data-driven:
1. **Configurazioni e Parametri:** Il modello è stato testato su diverse densità di copertura dei moduli fotovoltaici (pannelli densamente accoppiati, semi-densi o radi). Sono stati raccolti dati multivariati su radiazione fotosinteticamente attiva, temperature, umidità, variabilità stagionale e tipologie di copertura nuvolosa.
2. **Architettura Neurale:** Il network si basa su celle LSTM (eccellenti per l'estrazione di feature da sequenze temporali come le serie di dati climatici) abbinate ad un *Attention Mechanism*. Questo meccanismo pesa e alloca in modo dinamico l'importanza (focus) alle diverse variabili temporali, "ricordando" i momenti chiave che più influenzano la predizione (es. improvvisi passaggi nuvolosi o angolazioni solari critiche) senza perdersi nei rumori di fondo di lunga durata.
3. **Validazione e KPI:** I risultati del modello LSTM-Attention sono stati validati confrontandoli con classiche LSTM non pesate, reti convoluzionali e modelli di regressione tradizionale. I KPI principali misurati sono il Root Mean Square Error (RMSE) per stimare lo scarto assoluto tra radiazione misurata (W/m2) e predetta e la temperatura (°C).

### 3. Conclusioni
Il modello ha registrato un successo schiacciante nei confronti dei benchmark. L'algoritmo LSTM-Attention è stato capace di abbattere l'RMSE nella predizione della radiazione solare del 28.0%, 35.7% e ben 42.1% alle diverse densità di copertura fotovoltaica. Analogamente, la precisione sulla previsione della temperatura dell'aria è migliorata sensibilmente (drop dell'RMSE del 39.0% in estate e 18.1% in inverno).
**Limiti:** Uno dei limiti riscontrati riguarda la limitata applicabilità topografica dei dati raccolti: lo studio è stato validato unicamente su terreni in pianura. Terreni scoscesi, inclinati o terrazzati modificherebbero significativamente l'ombreggiamento dei moduli PV introducendo dinamiche termodinamiche e convettive molto differenti. Inoltre l'assenza di enclosure (essendo un campo aperto) comporta un'esposizione non controllabile a eventi precipitativi anomali.
**Sviluppi Futuri:** La futura implementazione mira a convertire l'LSTM-Attention in un cervello di controllo per *involucri agrivoltaici adattivi*: array di pannelli in grado di inseguire o modificare il proprio tilt angle dinamicamente non solo per massimizzare la resa elettrica, ma per governare attivamente il microclima sottostante (temperatura e luce) a seconda del fabbisogno momentaneo della coltura, creando una vera e propria simbiosi termo-luminosa autonoma.

## Concetti Chiave
- [[LSTM-Attention per Dinamiche Microclimatiche]]
- [[Agrivoltaico come Involucro Adattivo]]

## Bibliografia Rilevante
1. Jiang, B. et al. Attention-LSTM architecture combined with Bayesian hyperparameter optimization for indoor temperature prediction. (2022)
2. Bellone, Y. et al. Simulation-based decision support for agrivoltaic systems. (2024)

---
[[Casestudy - Nanjing Experimental Agrivoltaic Park]]
"""

casi1 = """---
tags:
  - casestudy
progetto: "IONIQ-5 Vehicle Thermal Management Evaluation"
localizzazione: "Seoul, Corea del Sud"
caratteristiche: "EV con Sky Camera Fisheye e sensori solari su tetto"
ambito: "Automotive / Gestione Climatica Mobile"
target: "Ottimizzazione consumi batteria tramite gestione termica proattiva"
paper: "[[Paper - Dynamic solar irradiance estimation for vehicle thermal management using a multi-modal machine learning framework]]"
---

# 🏗️ Progetto: IONIQ-5 Vehicle Thermal Management Evaluation

## Dettagli Progetto
- **Team/Progettisti:** Kookmin University (Department of Mechanical Engineering), Korea Automotive Technology Institute (KATECH)
- **Committenti/Finanziatori:** Ministry of Trade, Industry & Energy (MOTIE, Corea), National Research Foundation of Korea
- **Costi:** N/D

## Descrizione e Scopo
Il caso studio illustra l'integrazione di tecnologie multi-sensoriali su un veicolo elettrico Hyundai IONIQ-5 per affrontare le sfide del carico termico derivante dalla radiazione solare. In ambienti urbani densi (il test è stato effettuato in un percorso di 7 km a Seoul), le grandi superfici vetrate dei moderni EV assorbono enormi quote di calore, penalizzando severamente l'autonomia della batteria a causa dell'attivazione dei sistemi di raffreddamento (HVAC). Il progetto sperimentale ha visto l'installazione di piranometri, sensori di umidità e temperatura, GPS e una telecamera industriale fisheye U3-3280CP sul tetto del veicolo. Questi strumenti, incrociati con i dati forniti dal satellite GK2A, hanno nutrito un algoritmo ML (XGBoost, CatBoost, LightGBM) che mappa proattivamente gli ostacoli urbani, il passaggio delle nubi e stima la radiazione. L'applicazione rappresenta il primo passo verso finestrature elettrocromiche predittive: l'involucro dell'auto del futuro sarà capace di scurire dinamicamente specifiche zone del vetro e pre-raffrescare l'abitacolo pochi istanti prima che un intenso raggio solare, superato un grattacielo, colpisca direttamente i passeggeri.

---
**Fonte originale:** [[Paper - Dynamic solar irradiance estimation for vehicle thermal management using a multi-modal machine learning framework]]
"""

casi2 = """---
tags:
  - casestudy
progetto: "Nanjing Experimental Agrivoltaic Park"
localizzazione: "Nanjing (Nanchino), Jiangsu, Cina"
caratteristiche: "Array fotovoltaici a densità variabile su campo aperto"
ambito: "Agricoltura Sostenibile / Energie Rinnovabili"
target: "Simbiosi microclimatica tra pannelli e colture"
paper: "[[Paper - Research on time series prediction of microclimate in agrivoltaic systems based on the long short-term memory and attention mechanism]]"
---

# 🏗️ Progetto: Nanjing Experimental Agrivoltaic Park

## Dettagli Progetto
- **Team/Progettisti:** Institute of Agricultural Facilities and Equipment, Jiangsu Academy of Agricultural Sciences; Shenzhen Energy Group; University of Nottingham.
- **Committenti/Finanziatori:** Shenzhen Energy Nanjing Holding Co., Ltd. e Major Science and Technology Special Project of China Electric Power Engineering.
- **Costi:** N/D (Installazione da 47 ettari con riduzione emissioni stimata di 19.800 tonnellate/anno di CO2).

## Descrizione e Scopo
Costruito nel 2016 e operante a pieno regime, questo enorme parco agrivoltaico da 47 ettari rappresenta uno dei siti di test più avanzati per l'integrazione strutturale di impianti fotovoltaici in campo aperto. Il caso studio è focalizzato sulla variabilità della disposizione dei pannelli solari (a diversa densità: pienamente densi, semi-densi e radi) posti ad un'altezza minima da terra di 2.5 metri e con inclinazione di 24 gradi. A differenza dei sistemi in serra, il campo aperto richiede modelli molto più sofisticati (implementati tramite reti neurali LSTM con meccanismi di *Attention*) per prevedere l'andamento della temperatura e dell'insolazione sotto le vele fotovoltaiche. Il progetto dimostra che un impianto fotovoltaico può evolversi da un mero sistema di "energy harvesting" in un vero e proprio *involucro adattivo* per il terreno agricolo: prevedere le sacche di calore e la riduzione della radiazione fotosinteticamente attiva permette di strutturare rotazioni di colture specifiche o di automatizzare irrigazioni localizzate, ottimizzando sia il guadagno economico dell'operatore energetico che la resa agronomica del contadino in scenari di forte stress idrico indotto dai cambiamenti climatici.

---
**Fonte originale:** [[Paper - Research on time series prediction of microclimate in agrivoltaic systems based on the long short-term memory and attention mechanism]]
"""

c1 = """---
tags:
  - concept
aliases:
  - ML Multi-Modale Predittivo
---

# 💡 Concetto: ML Multi-Modale per Irraggiamento Solare Dinamico

## Definizione
Il Machine Learning Multi-Modale nell'ambito della stima dell'irraggiamento solare fa riferimento all'uso di algoritmi (come Gradient Boosting, XGBoost, CatBoost) che operano analizzando simultaneamente flussi di dati di natura profondamente eterogenea, o "modalità" differenti. Anziché affidarsi unicamente a dataset stazionari di tipo testuale o numerico, l'approccio multi-modale fonde macro-dati (es. immagini satellitari a infrarossi e nel visibile che mappano formazioni nuvolose globali) con micro-dati (immagini in tempo reale da fisheye ground-based che identificano ostacoli urbani immediati come grattacieli o alberi) e parametri di stato vettoriale (coordinate GPS, giroscopio, temperatura). Questa sinergia consente una previsione altissima dell'irraggiamento per veicoli o componenti in rapido movimento, un risultato storicamente irraggiungibile per i classici modelli climatici statici o GIS.

## Fonti Collegate
- [[Paper - Dynamic solar irradiance estimation for vehicle thermal management using a multi-modal machine learning framework]] - *Introduce un framework per EVs capace di stimare in tempo reale il carico solare fondendo le immagini delle sky camera e dei satelliti GK2A per gestire il raffreddamento proattivo.*

---
**Vedi anche:**
- [[Gestione Termica Location-Aware]]
"""

c2 = """---
tags:
  - concept
aliases:
  - ACBI
  - AI-Climate-Building Integration
---

# 💡 Concetto: AI-Climate-Building Integration Framework (ACBI)

## Definizione
L'AI-Climate-Building Integration Framework (ACBI) è un quadro concettuale e metodologico proposto per affrontare la complessità della progettazione edilizia sostenibile durante la transizione ecologica e l'intensificazione del cambiamento climatico. Il framework riconosce che gli strumenti di simulazione tradizionali non sono in grado di gestire i massicci flussi di dati dei modelli climatici futuri in tempo reale. ACBI si articola in tre pilastri interdipendenti:
1) **Technical Integration Pillar**: accoppiamento dinamico delle intelligenze artificiali con l'infrastruttura (BIM, sensori IoT in real-time, digital twins).
2) **Climate Response Pillar**: focalizzato sull'azione, richiede che i sistemi processino scenari di proiezione IPPC formulando strategie adattive di sopravvivenza per l'edificio contro stressor anomali (flood, ondate di calore estreme).
3) **Governance Pillar**: la parte legale e di gestione del rischio, che include i protocolli di condivisione sicura dei dati e il rispetto dell'AI Act per un'intelligenza artificiale non inquinante e non "allucinata".

## Fonti Collegate
- [[Paper - How AI Shapes the Future Landscape of Sustainable Building Design With Climate Change Challenges]] - *Proposta teorica formale del framework per sistematizzare l'implementazione etica ed efficiente dell'AI generativa e dei LLM nell'architettura verde futura.*

---
**Vedi anche:**
- [[Physics-Informed Foundation Models per l'Architettura]]
"""

c3 = """---
tags:
  - concept
aliases:
  - Physics-Informed AI per l'Architettura
  - PI-LLM
---

# 💡 Concetto: Physics-Informed Foundation Models per l'Architettura

## Definizione
I Foundation Models (Modelli Fondazionali) come i LLM (Large Language Models) generativi sono originariamente pre-addestrati su enormi corpus linguistici o visivi. Nel contesto architettonico e ingegneristico, questa natura generica comporta il rischio di "allucinazioni costruttive": proporre involucri esteticamente perfetti ma che violano palesemente i fondamenti della termodinamica, della meccanica strutturale o del bilancio energetico. I *Physics-Informed Foundation Models* rappresentano il salto evolutivo in cui le equazioni fisiche (es. leggi di trasferimento del calore, dinamica dei fluidi per la ventilazione naturale, calcolo strutturale) vengono codificate nativamente all'interno della loss function o del processo di training dell'Intelligenza Artificiale. Questo impone ai sistemi generativi di rispettare la fisica del mondo reale, rendendo la loro ideazione di edifici, pelli reattive e sistemi HVAC immediatamente calcolabile, fattibile e affidabile, superando il solo approccio basato sul riconoscimento statistico dei pattern.

## Fonti Collegate
- [[Paper - How AI Shapes the Future Landscape of Sustainable Building Design With Climate Change Challenges]] - *Evidenzia come limite degli attuali LLM la mancanza di solidità scientifica costruttiva, raccomandando i modelli informati sulla fisica come requisito di sicurezza del design.*

---
**Vedi anche:**
- [[AI-Climate-Building Integration Framework (ACBI)]]
"""

c4 = """---
tags:
  - concept
aliases:
  - LSTM-Attention
  - RNN Attention Mechanism
---

# 💡 Concetto: LSTM-Attention per Dinamiche Microclimatiche

## Definizione
LSTM-Attention è un'architettura avanzata di reti neurali in ambito Deep Learning per l'analisi di serie temporali. Combina le celle LSTM (Long Short-Term Memory), che sono reti neurali ricorrenti eccellenti nel trattenere la "memoria" degli eventi passati e gestire lunghe sequenze (ad esempio misurazioni orarie di un intero anno climatico), con un "Attention Mechanism". Nel contesto microclimatico, l'Attention calcola dinamicamente un "peso" in tempo reale per determinare quali punti esatti nel passato recente abbiano la massima influenza sul presente immediato. Questo evita la degradazione della predizione tipica delle LSTM semplici al crescere dell'orizzonte temporale. L'algoritmo impara autonomamente a ignorare i giorni piatti e ad assegnare pesi mastodontici alle improvvise variazioni di nuvolosità o angolazione del vento, producendo predizioni estremamente aderenti alla realtà fisica, vitali per l'attivazione tempestiva di frangisole o il controllo di serre e agrivoltaico.

## Fonti Collegate
- [[Paper - Research on time series prediction of microclimate in agrivoltaic systems based on the long short-term memory and attention mechanism]] - *Applica con successo l'architettura LSTM-Attention battendo i modelli tradizionali e preannunciando la radiazione e temperatura in parchi agrivoltaici ombrosi con riduzioni drastiche dell'errore (RMSE).*

---
**Vedi anche:**
- [[Agrivoltaico come Involucro Adattivo]]
"""

c5 = """---
tags:
  - concept
aliases:
  - Agrivoltaico Adattivo
---

# 💡 Concetto: Agrivoltaico come Involucro Adattivo

## Definizione
Tipicamente, il settore agrivoltaico (AV) valuta i pannelli solari come superfici passive di ostruzione volte primariamente alla raccolta fotovoltaica, con la coltivazione agricola sottomessa all'ombra proiettata. Riconcettualizzare l'agrivoltaico come un "Involucro Adattivo" significa applicare alla scala territoriale le logiche tipiche degli involucri edilizi intelligenti. In questo paradigma, la matrice fotovoltaica viene gestita (spesso grazie all'AI predittiva e all'automazione IoT) non solo in base al movimento solare per la massima resa energetica (tracking solare), ma interfacciandosi con le esigenze biologiche puntuali e momentanee della coltura sottostante (rischio di stress da calore, deficit idrico o scarsità di luce fotosinteticamente attiva - PAR). Variando dinamicamente il tilt o traslando, i pannelli agiscono come una copertura attiva termoregolatrice del campo, ottimizzando la simbiosi tra produzione energetica e microclima agronomo in un mondo minacciato dal riscaldamento globale.

## Fonti Collegate
- [[Paper - Research on time series prediction of microclimate in agrivoltaic systems based on the long short-term memory and attention mechanism]] - *Testa e prova modelli che prevedono esattamente il comportamento microclimatico spaziotemporale in un parco AV, condizione essenziale per far evolvere l'installazione statica in un sistema adattivo intelligente.*

---
**Vedi anche:**
- [[LSTM-Attention per Dinamiche Microclimatiche]]
"""

c6 = """---
tags:
  - concept
aliases:
  - Predictive HVAC
  - Controllo Climatico Proattivo Mobile
---

# 💡 Concetto: Gestione Termica Location-Aware

## Definizione
La Gestione Termica Location-Aware (Location-Aware Thermal Management) rappresenta un salto di paradigma per il controllo del clima interno nei veicoli (e potenzialmente negli edifici mobili o modulari). I sistemi classici reagiscono termostaticamente (attivano il raffreddamento o il riscaldamento solo quando il sensore interno registra una discrepanza dal setpoint). Un sistema location-aware unisce la localizzazione GPS, dati satellitari e telecamere di prossimità per "sapere" in anticipo cosa succederà: ad esempio sa che nei prossimi 3 chilometri il veicolo emergerà dall'ombra protettiva di un filare alberato ed entrerà in un'autostrada in pieno sole. Sulla base di questa predizione visiva e spaziale, il veicolo proattivamente pre-regola i parametri di raffreddamento dell'abitacolo o varia l'oscuramento delle finestre elettrocromiche prima che si inneschi il picco di calore, minimizzando l'energia sprecata per il recupero termico d'emergenza, aspetto fondamentale per massimizzare il range dei Veicoli Elettrici (EV).

## Fonti Collegate
- [[Paper - Dynamic solar irradiance estimation for vehicle thermal management using a multi-modal machine learning framework]] - *Usa l'AI per prevedere le ombre degli edifici per consentire all'HVAC dell'auto di anticipare la radiazione solare violenta in città.*

---
**Vedi anche:**
- [[ML Multi-Modale per Irraggiamento Solare Dinamico]]
"""


with open(os.path.join(fonti_dir, "Paper - Dynamic solar irradiance estimation for vehicle thermal management using a multi-modal machine learning framework.md"), "w", encoding="utf-8") as f:
    f.write(paper1)
with open(os.path.join(fonti_dir, "Paper - How AI Shapes the Future Landscape of Sustainable Building Design With Climate Change Challenges.md"), "w", encoding="utf-8") as f:
    f.write(paper2)
with open(os.path.join(fonti_dir, "Paper - Research on time series prediction of microclimate in agrivoltaic systems based on the long short-term memory and attention mechanism.md"), "w", encoding="utf-8") as f:
    f.write(paper3)

with open(os.path.join(casi_dir, "Casestudy - IONIQ-5 Thermal Management Evaluation.md"), "w", encoding="utf-8") as f:
    f.write(casi1)
with open(os.path.join(casi_dir, "Casestudy - Nanjing Experimental Agrivoltaic Park.md"), "w", encoding="utf-8") as f:
    f.write(casi2)

with open(os.path.join(concept_dir, "Concept - ML Multi-Modale per Irraggiamento Solare Dinamico.md"), "w", encoding="utf-8") as f:
    f.write(c1)
with open(os.path.join(concept_dir, "Concept - AI-Climate-Building Integration Framework (ACBI).md"), "w", encoding="utf-8") as f:
    f.write(c2)
with open(os.path.join(concept_dir, "Concept - Physics-Informed Foundation Models per l'Architettura.md"), "w", encoding="utf-8") as f:
    f.write(c3)
with open(os.path.join(concept_dir, "Concept - LSTM-Attention per Dinamiche Microclimatiche.md"), "w", encoding="utf-8") as f:
    f.write(c4)
with open(os.path.join(concept_dir, "Concept - Agrivoltaico come Involucro Adattivo.md"), "w", encoding="utf-8") as f:
    f.write(c5)
with open(os.path.join(concept_dir, "Concept - Gestione Termica Location-Aware.md"), "w", encoding="utf-8") as f:
    f.write(c6)

print("Tutti i file sono stati scritti con successo!")
