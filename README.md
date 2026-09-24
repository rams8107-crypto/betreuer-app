# GBB Lernen

Dauerhafte private Lern-App (Passwort) für iPhone und Android.

## Sofort öffnen (dauerhaft)

Kopieren und im Handy-Browser öffnen:

**https://htmlpreview.github.io/?https://raw.githubusercontent.com/rams8107-crypto/betreuer-app/gbb-lernen/docs/gbb.html**

Login:

| | |
|---|---|
| Benutzer | `ramazan` |
| Passwort | `GBBprivat26` |

Zum Homescreen: iPhone Safari → Teilen → Zum Home-Bildschirm / Android Chrome → App installieren.

## Render (optional, eigener Server)

Siehe unten – Blueprint in `render.yaml`.

## Render einrichten (einmalig)

1. Konto: [https://dashboard.render.com](https://dashboard.render.com) (mit GitHub einloggen)
2. **New** → **Blueprint**
3. Repository **`rams8107-crypto/betreuer-app`** verbinden
4. Branch wählen: `main` (nach Merge) oder `cursor/gbb-lernen-app-f85f`
5. Blueprint anwenden – Service **gbb-lernen** wird erstellt
6. Nach dem Deploy: unter **gbb-lernen** die URL kopieren und am Handy öffnen

Die Datei `render.yaml` im Repo-Root steuert Build und Start automatisch (`rootDir`: `betreuer_cloud_pwa`).

### Alternative ohne Blueprint

1. **New** → **Web Service** → Repo wählen  
2. Root Directory: `betreuer_cloud_pwa`  
3. Build: `pip install -r requirements.txt`  
4. Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`  
5. Region: Frankfurt, Plan: Free  

## Lokal testen

```bash
cd betreuer_cloud_pwa
pip install -r requirements.txt
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
```

Dann im Heim-WLAN: `http://<PC-IP>:8000` (PC und Handy gleiches WLAN).

**Hinweis:** Lernhilfe, kein anerkannter Sachkundelehrgang nach BtRegV § 6.
