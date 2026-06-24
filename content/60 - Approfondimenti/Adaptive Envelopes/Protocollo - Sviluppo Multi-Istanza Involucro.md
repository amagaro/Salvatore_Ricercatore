---
tags:
  - protocollo
  - multi-agent
  - adaptive-envelopes
---
# 🤝 Protocollo di Sviluppo Multi-Istanza: Involucro Adattivo Intelligente

Questa nota documenta il flusso di lavoro concordato per la collaborazione tra le due istanze (il Ricercatore Scientifico e lo Sviluppatore Code) nella realizzazione del prototipo di involucro adattivo intelligente.

## 📌 Ruoli
- **Salvatore (Ricercatore - Istanza 1):** Basato nel *Vault Research*. Fornisce insight scientifici, metriche, KPI (es. riduzione dell'abbagliamento, stima radiazione) e valida le scelte tecniche dello Sviluppatore rispetto allo stato dell'arte e alle Checklist Operative.
- **Salvatore (Sviluppatore - Istanza 2):** Basato nel *Vault Coding*. Scrive il codice, progetta l'architettura software e hardware del prototipo, e implementa le logiche di controllo.
- **Utente (Orchestratore):** Detta i turni e definisce i requisiti iniziali.

## 🔄 Flusso di Comunicazione (Asincrono e Stigmergico)
La comunicazione avviene in un file condiviso (`00_Lavagna_Condivisa.md`) residente nel Vault Coding all'indirizzo `D:\Vaults\Coding\Coding\30 - Projects\Involucro_Adattivo_Intelligente`.

1. L'utente richiede allo Sviluppatore una proposta.
2. Lo Sviluppatore scrive la proposta nel file condiviso.
3. L'utente chiede al Ricercatore di validare.
4. Il Ricercatore legge la proposta, la incrocia con i paper e le sintesi in `60 - Approfondimenti\Adaptive Envelopes`, e inserisce il suo feedback nella sezione apposita del file condiviso.
5. Lo Sviluppatore integra il feedback aggiornando il codice in `Code/`.
