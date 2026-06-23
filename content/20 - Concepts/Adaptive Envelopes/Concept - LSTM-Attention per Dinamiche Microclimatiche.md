---
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
