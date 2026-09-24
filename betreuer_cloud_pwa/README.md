# GBB Lernen

Mobile Lern-App zur Vorbereitung auf den **Sachkundenachweis** für gesetzliche Berufsbetreuerinnen und Berufsbetreuer (Module nach Anlage zu § 3 Abs. 4 BtRegV).

## Funktionen

- 11 Module mit Themenübersicht und Lernkarten
- Quiz pro Modul (Auswertung serverseitig, Bestehensgrenze 60 %)
- Fortschritt lokal im Browser (localStorage)
- PWA-tauglich (Manifest, Homescreen)

**Hinweis:** Dies ist eine Lernhilfe, kein anerkannter Sachkundelehrgang nach BtRegV § 6.

## Start

```bash
cd betreuer_cloud_pwa
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

Öffnen: http://localhost:8000
