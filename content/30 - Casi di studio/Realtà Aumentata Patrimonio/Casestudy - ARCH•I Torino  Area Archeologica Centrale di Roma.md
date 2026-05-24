---
tags:
  - casestudy
progetto: "ARCH•I Torino / Area Archeologica Centrale di Roma"
localizzazione: "Italia (Torino e Fori Imperiali di Roma)"
caratteristiche: "Deep Learning (CNN), AR Offline, Riconoscimento Monumenti, Fotogrammetria 3D"
ambito: "Beni Culturali / Archeologia / Intelligenza Artificiale"
target: "Turisti, studiosi, visitatori"
paper: "[[Paper - INTELLIGENZA ARTIFICIALE E REALTÀ AUMENTATA PER LA CONDIVISIONE DEL PATRIMONIO CULTURALE]]"
---

# 🏗️ Progetto: ARCH•I Torino / Area Archeologica Centrale di Roma

## Dettagli Progetto
- **Team/Progettisti:** Centro FULL (Politecnico di Torino) in partnership con il Dipartimento di Architettura dell'Università di Roma Tre (es. D. Adiutori)
- **Committenti/Finanziatori:** Progetto di ricerca accademica (ArCH - Architectural Cultural Heritage)
- **Costi:** Sviluppo basato interamente su architetture Free and Open Source Software (FOSS) come Keras e TensorFlow

## Descrizione e Scopo
Il progetto rappresenta un'intersezione avanzata tra **Geomatica, Intelligenza Artificiale e Realtà Aumentata**. Lo scopo è creare un'applicazione mobile in grado di riconoscere automaticamente, offline e in tempo reale, i monumenti inquadrati dalla fotocamera dello smartphone (es. nell'Area Archeologica Centrale di Roma o a Torino). Una volta riconosciuto il monumento, l'app sovrappone (AR) modelli 3D ad alta risoluzione (derivati da laser scanner e fotogrammetria) e schede storico-descrittive.

## Caratteristiche Chiave
- **Riconoscimento basato su AI:** utilizza Reti Neurali Convoluzionali (CNN) addestrate su vasti dataset fotografici per superare i limiti dei tradizionali marker AR visivi (QR code) o del GPS (spesso impreciso nei centri storici densi)
- **Elaborazione Offline:** la rete neurale è "compressa" per girare nativamente sul dispositivo mobile (edge computing), evitando ritardi di rete (latenza) e garantendo il funzionamento anche in aree archeologiche prive di connessione
- **Integrazione Dati 3D:** i modelli sovrapposti non sono semplici render approssimativi, ma nuvole di punti o mesh fotogrammetriche accurate prodotte dai dipartimenti di architettura (DAD/DIATI del Politecnico)

## Esito / Risultati
- Dimostra la fattibilità tecnica dell'uso del Deep Learning mobile per la fruizione del patrimonio culturale senza alterare fisicamente l'area archeologica con cartellonistica
- Costituisce una solida base per la creazione di dataset aperti (ArCH) per il training di algoritmi di riconoscimento architettonico

---
**Fonte originale:** [[Paper - INTELLIGENZA ARTIFICIALE E REALTÀ AUMENTATA PER LA CONDIVISIONE DEL PATRIMONIO CULTURALE]]
**Fonti integrative:** polito.it (progetto ArCH)
