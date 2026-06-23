---
tags:
  - casestudy
progetto: "CNC TPHWC Retrofit"
localizzazione: "Non Specificato (Accademico)"
caratteristiche: "Retrofit di una taglierina a filo caldo Step-Four PC-CUT 1000 da MS-DOS a ESP32/FluidNC"
ambito: "Fabbricazione Digitale, Retrofitting Industriale"
target: "Produzione di superfici architettoniche Free-Form"
paper: "[[Paper - Strategies to Approximate Free-Form Surfaces]]"
---

# 🏗️ Progetto: CNC TPHWC Retrofit

## Dettagli Progetto
- **Team/Progettisti:** Moritz Koegel
- **Committenti/Finanziatori:** N/A
- **Costi:** Basso costo (sostituzione controller con microcontrollori commerciali)

## Descrizione e Scopo
Progetto di modernizzazione ("retrofitting") di una macchina CNC obsoleta per il taglio a filo caldo. Tramite reverse engineering, il vecchio sistema LPT/MS-DOS è stato sostituito da un array ESP32/Arduino. Questo ha permesso la comunicazione in tempo reale (tramite WebSocket) con Rhinoceros/Grasshopper, permettendo all'algoritmo di generare tracciati senza collisioni per il taglio di complesse superfici architettoniche "Free-Form", riducendo il tempo computazionale da 50 a 5 secondi e validando la sostenibilità del riuso industriale in ottica costruttiva.

---
**Fonte originale:** [[Paper - Strategies to Approximate Free-Form Surfaces]]
