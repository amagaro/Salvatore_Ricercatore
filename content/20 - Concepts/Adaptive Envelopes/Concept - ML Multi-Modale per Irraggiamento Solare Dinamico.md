---
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
