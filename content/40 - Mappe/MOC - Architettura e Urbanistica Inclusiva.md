---
tags:
  - moc
  - inclusione
aliases:
  - Mappa Concettuale Architettura Inclusiva
---

# 🗺️ MOC - Architettura e Urbanistica Inclusiva

Questa mappa raggruppa tutti i concetti e le indagini relative all'accessibilità dell'ambiente costruito, alle metriche di walkability e alle sfide imposte dall'abilismo urbano.

## 📌 Concetti Chiave

```dataview
TABLE aliases as "Alias", file.mtime as "Ultimo Aggiornamento"
FROM "20 - Concepts/Sulla disabilità"
SORT file.name ASC
```

## 🏗️ Casi di Studio Recenti

```dataview
TABLE progetto as "Progetto", localizzazione as "Localizzazione", ambito as "Ambito"
FROM "30 - Casi di studio/Sulla disabilità"
SORT file.name ASC
```

## 📚 Ultime Fonti Analizzate

```dataview
TABLE anno_pubblicazione as "Anno", tipologia as "Tipo"
FROM "10 - Fonti/Sulla disabilità"
WHERE file.name != "10 - Raw"
SORT file.mtime DESC
LIMIT 5
```
