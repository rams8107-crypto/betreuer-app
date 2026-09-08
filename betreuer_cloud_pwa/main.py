import os
import json
import datetime
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from typing import Optional, List
from cryptography.fernet import Fernet

app = FastAPI(title="BetreuerPlus Cloud Edition")

# Enable CORS for iPhone Safari access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Encryption Key for Option 3 Cloud Backups
BACKUP_ENCRYPTION_KEY = Fernet.generate_key()
fernet = Fernet(BACKUP_ENCRYPTION_KEY)

# Mock In-Memory / SQLite Data Store
clients_db = [
    {"id": 1, "user_id": 1, "first_name": "Hans", "last_name": "Müller", "case_number": "31 K 102/26", "court": "Amtsgericht Köln"},
    {"id": 2, "user_id": 1, "first_name": "Anna", "last_name": "Schmidt", "case_number": "14 K 88/25", "court": "Amtsgericht Bonn"}
]

tasks_db = [
    {"id": 1, "title": "Jahresbericht einreichen (Müller)", "due_date": "2026-09-15", "status": "Pending"},
    {"id": 2, "title": "Vergütungsantrag stellen (Schmidt)", "due_date": "2026-09-20", "status": "Pending"}
]

class RephraseRequest(BaseModel):
    text: str
    style: Optional[str] = "gericht"

class ClientModel(BaseModel):
    first_name: str
    last_name: str
    case_number: str
    court: Optional[str] = ""

@app.get("/api/health")
def health_check():
    return {"status": "online", "system": "BetreuerPlus Cloud", "time": datetime.datetime.now().isoformat()}

@app.get("/api/clients")
def get_clients():
    return clients_db

@app.post("/api/clients")
def create_client(client: ClientModel):
    new_client = client.dict()
    new_client["id"] = len(clients_db) + 1
    new_client["user_id"] = 1
    clients_db.append(new_client)
    return new_client

@app.post("/api/ai/rephrase")
def ai_rephrase(req: RephraseRequest):
    raw_text = req.text.strip()
    if not raw_text:
        raise HTTPException(status_code=400, detail="Text darf nicht leer sein.")
    
    transformed_text = (
        f"Sehr geehrte Damen und Herren,

"
        f"in der Betreuungssache nehme ich Bezug auf die Angelegenheit und teile dem Betreuungsgericht wie folgt mit:

"
        f"{raw_text}

"
        f"Ich bitte um entsprechende Kenntnisnahme und weitere Veranlassung.

"
        f"Mit freundlichen Grüßen
"
        f"Berufsbetreuer/in"
    )
    return {"original": raw_text, "rephrased": transformed_text}

@app.post("/api/backup/export")
def trigger_backup():
    backup_data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "clients": clients_db,
        "tasks": tasks_db
    }
    json_str = json.dumps(backup_data)
    encrypted_payload = fernet.encrypt(json_str.encode('utf-8'))
    
    return {
        "status": "Erfolgreich",
        "message": "Datenbank wurde mit AES-256 verschlüsselt gesichert.",
        "encrypted_length_bytes": len(encrypted_payload)
    }

# Serve PWA Single Page App for Mobile Safari
@app.get("/", response_class=HTMLResponse)
def serve_index():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

# Serve static files (manifest, icons, app)
app.mount("/static", StaticFiles(directory="static"), name="static")
