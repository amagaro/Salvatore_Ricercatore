---
tags:
  - source
  - paper
autore: Abdulwahed Fazeli, Mohammad Saleh Dashti, Farzad Jalaei, Mostafa Khanzadi
anno: 2021
titolo: "An integrated BIM-based approach for cost estimation in construction projects"
---

# 📄 Fonte: An integrated BIM-based approach for cost estimation in construction projects

## Metadati
- **Titolo:** An integrated BIM-based approach for cost estimation in construction projects
- **Autori:** Abdulwahed Fazeli, Mohammad Saleh Dashti, Farzad Jalaei, Mostafa Khanzadi
- **Anno:** 2021
- **Notebook Originale:** [[Notebook - BIM and costs estimation]]

## Sintesi Estesa

### 1. Obiettivi
Lo scopo principale della ricerca è proporre un approccio semi-automatico basato sul BIM per la stima dei costi, collegando dinamicamente le quantità estratte dai modelli 3D allo standard nazionale di stima dell'Iran. Il problema da risolvere riguarda la difficoltà di valutare dal punto di vista economico i diversi scenari progettuali in modo rapido e senza errori; i metodi di computo tradizionali, basati sull'esperienza manuale, sono lenti e inclini all'omissione. L'obiettivo è colmare il divario di interoperabilità tra gli standard internazionali (orientati all'oggetto) e le norme nazionali (orientate all'attività).

### 2. Metodologia
La ricerca sviluppa un framework operativo strutturato in un plug-in personalizzato in Autodesk Revit (programmato in C#). La metodologia prevede:
- Sviluppo della libreria in Revit.
- Modellazione (Building Geometric Model).
- Mappatura dei database in Excel: collegamento dei codici UniFormat (componenti) ai codici MasterFormat (materiali) e infine alle voci del listino FehrestBaha.
- Iniezione automatica di parametri personalizzati in Revit.
- QTO (Quantity Take-Off) verso Excel per moltiplicare le quantità estratte per i prezzi unitari e calcolare il costo totale.
Il sistema è stato validato sul caso studio "Tiffa project", stimando la porzione architettonica.

### 3. Limiti della Ricerca (Limitations)
Gli autori dichiarano due criticità principali:
- Barriere di conoscenza: il sistema richiede familiarità con gli standard UniFormat e MasterFormat, attualmente poco diffusi nel mercato iraniano.
- Limiti del database: l'approccio ha limitazioni nell'elaborare e incorporare le voci relative agli "Extra Works" (Lavori Extra) del FehrestBaha, che la logica dell'algoritmo non riesce a quantificare in automatico.

### 4. KPI e Risultati Misurati
**Risultati Qualitativi:** Il sistema ha calcolato la stima dei costi con un livello di accuratezza pienamente accettabile. Ha ridotto considerevolmente il tempo richiesto per l'estimo rispetto agli approcci manuali, eliminando la dipendenza soggettiva e minimizzando gli errori.
**Dati Quantitativi:** Il test ha prodotto tabelle di computo esatte per l'edificio di 18 piani. Il sistema ha quantificato un costo complessivo delle categorie (Sum of all Element Categories' Cost) pari a 30.726.911.732,60 Rial iraniani, al netto dei coefficienti regionali.

### 5. Sviluppi Futuri
I futuri sviluppi mirano a migliorare l'accuratezza del sistema integrando le voci speciali ("Extra Works"). In secondo luogo, l'approccio verrà esteso per includere le divisioni impiantistiche (MEP), superando il focus attuale sulle sole divisioni architettoniche e strutturali. Infine, si auspica l'adattamento dell'infrastruttura informatica ad altri standard di stima nazionali.

### 6. Conclusioni
Il contributo significativo del paper è aver dimostrato la possibilità di far dialogare le normative nazionali di computo con le classificazioni globali. Tramite database relazionali, il sistema ha convertito l'organizzazione "per materiali e attività" in una "per componenti". Questo framework semi-automatizzato si rivela uno strumento formidabile per valutare all'istante l'impatto economico di diverse alternative progettuali e tracciare le ricadute sul budget causate dalle modifiche al modello.

## Concetti Chiave
- [[Building Information Modelling (BIM)]]
- [[Cost estimation]]
- [[MasterFormat]]
- [[UniFormat]]
- [[Iran's cost estimation standard]]
- [[FehrestBaha]]

## Bibliografia Rilevante
1. Atlaf (1979)
2. Ghoddousi and Hosseini (2012)
3. Jrade and Alkass (2007)
4. Ma et al. (2013)

---
[[Casestudy - Tiffa project]]
