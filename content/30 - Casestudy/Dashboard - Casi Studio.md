---
tags:
  - dashboard
---

# 📊 Dashboard: Casi di Studio

Questa dashboard riepiloga i casi di studio archiviati nel Vault, con riferimenti visivi e tecnici.

## 🌿 Giardini Terapeutici
```dataview
TABLE 
  localizzazione AS "📍 Luogo", 
  ambito AS "🏥 Ambito",
  target AS "👥 Target",
  caratteristiche AS "✨ Caratteristiche"
FROM #casestudy
WHERE contains(file.folder, "giardini-terapeutici")
SORT file.name ASC
```

## 📱 Realtà Aumentata e Patrimonio
```dataview
TABLE 
  localizzazione AS "📍 Luogo", 
  ambito AS "🏛️ Ambito",
  target AS "👥 Target",
  caratteristiche AS "✨ Caratteristiche"
FROM #casestudy
WHERE contains(file.folder, "Realtà Aumentata Patrimonio")
SORT file.name ASC
```

---
**Ultimo aggiornamento:** 2026-05-12
