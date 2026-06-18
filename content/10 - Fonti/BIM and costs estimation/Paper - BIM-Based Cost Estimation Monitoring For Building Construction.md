---
tags:
  - source
  - paper
autore: Emad Elbeltagi, Ossama Hosny, Mahmoud Dawood, Ahmed Elhakeem
anno: 2014
titolo: "BIM-Based Cost Estimation/ Monitoring For Building Construction"
---

# 📄 Fonte: BIM-Based Cost Estimation/ Monitoring For Building Construction

## Metadati
- **Titolo:** BIM-Based Cost Estimation/ Monitoring For Building Construction
- **Autori:** Emad Elbeltagi, Ossama Hosny, Mahmoud Dawood, Ahmed Elhakeem
- **Anno:** 2014
- **Notebook Originale:** [[Notebook - BIM and costs estimation]]

## Sintesi Estesa

### 1. Obiettivi
Lo scopo principale della ricerca è sviluppare un modello completo e integrato di stima, monitoraggio e controllo dei costi sfruttando le potenzialità del BIM e della visualizzazione tridimensionale. Il problema fondamentale riguarda la crescente complessità del controllo finanziario man mano che un progetto avanza. L'obiettivo è fornire un sistema visivo automatizzato che permetta di confrontare direttamente sul modello 3D i costi effettivi sostenuti con quelli previsti a budget, consentendo ai project manager di rilevare immediatamente le deviazioni e intraprendere azioni correttive.

### 2. Metodologia
La ricerca propone un framework concettuale suddiviso in tre moduli principali: stima dei costi/pianificazione, monitoraggio/controllo e BIM. L'infrastruttura utilizza la WBS (Work Breakdown Structure) per collegare il piano dei lavori (su MS Project) al modello BIM. Le quantità geometriche dal modello 3D (Revit) vengono esportate in un database (MS Access) che comunica con modelli avanzati in Excel per fondere tempi, quantità e costi base delle risorse. Durante la costruzione, i dati effettivi vengono acquisiti per calcolare automaticamente le varianze di costo e i risultati vengono re-importati nel modello BIM per alterare l'aspetto grafico degli elementi.

### 3. Limiti della Ricerca (Limitations)
- Limitazione del perimetro di calcolo: Il modulo di stima dei costi sviluppato nel prototipo calcola esclusivamente i costi diretti delle attività, escludendo i costi indiretti.
- Sensibilità ai dati iniziali: Le valutazioni automatizzate delle prestazioni di costo nelle primissime fasi sono molto suscettibili al "rumore" derivante da variazioni improvvise.
- Limiti di interfaccia: Durante la validazione è emersa una mancanza tecnica relativa alla visualizzazione, ovvero l'assenza di una "split view" per osservare simultaneamente le varianze di singole risorse e la varianza di costo complessiva.

### 4. KPI e Risultati Misurati
Non sono esplicitati KPI quantitativi numerici esatti, ma sono misurati risultati qualitativi:
- Successo nella visualizzazione: Il sistema di codifica a colori implementato nel modello BIM (rosso per varianze sfavorevoli, verde chiaro per costi in linea, grigio per risparmi) è risultato estremamente efficace.
- Successo decisionale e ottimizzazione dei tempi: Il sistema riduce in modo considerevole il tempo normalmente impiegato per il tracciamento manuale dei dati e semplifica il monitoraggio delle attività costruttive.

### 5. Sviluppi Futuri
L'indagine futura si concentrerà sullo sviluppo tecnologico dell'interfaccia BIM, investigando l'utilizzo del "BIM versioning" come motore per implementare una funzione avanzata di split view. Questo permetterà di visualizzare contemporaneamente i dati di varianza di costo delle singole risorse associate a un'attività e la varianza complessiva.

### 6. Conclusioni
Il contributo del paper rappresenta un passo fondamentale nell'evoluzione del Project Management edile. Il documento dimostra come il BIM possa trasformarsi da mero strumento di progettazione pre-costruttiva a piattaforma di controllo gestionale dinamica in fase esecutiva. Attraverso l'uso sinergico di database interconnessi e codifiche cromatiche, si colma la storica frattura tra la contabilità astratta dei fogli di calcolo e la percezione fisica dell'avanzamento in cantiere.

## Concetti Chiave
- [[Cost monitoring and Control]]
- [[Cost Variances]]
- [[Cost Estimate]]
- [[BIM]]
- [[Visualization]]

## Bibliografia Rilevante
1. Sacks et al. (2010)
2. Fard et al. (2009)
3. Khemlani (2010)
4. Elbeltagi and Dawood (2011)

---
[[Casestudy - Applicazione prototipale su edificio a 8 piani]]
