---
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
