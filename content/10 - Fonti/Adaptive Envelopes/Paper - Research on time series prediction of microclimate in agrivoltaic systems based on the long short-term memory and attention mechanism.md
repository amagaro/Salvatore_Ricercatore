---
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
