import datetime
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from content.modules import MODULES, get_module, progress_meta

app = FastAPI(title="GBB Lernen", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuizAnswer(BaseModel):
    question_id: str
    selected: int = Field(ge=0)


class QuizSubmit(BaseModel):
    module_id: int
    answers: List[QuizAnswer]


@app.get("/api/health")
def health_check():
    return {
        "status": "online",
        "system": "GBB Lernen",
        "time": datetime.datetime.now().isoformat(),
    }


@app.get("/api/meta")
def meta():
    return progress_meta()


@app.get("/api/modules")
def list_modules():
    return [
        {
            "id": m["id"],
            "title": m["title"],
            "hours": m["hours"],
            "area": m["area"],
            "summary": m["summary"],
            "topic_count": len(m["topics"]),
            "card_count": len(m["cards"]),
            "quiz_count": len(m["quiz"]),
        }
        for m in MODULES
    ]


@app.get("/api/modules/{module_id}")
def module_detail(module_id: int):
    module = get_module(module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Modul nicht gefunden.")
    return module


@app.get("/api/modules/{module_id}/quiz")
def module_quiz(module_id: int):
    module = get_module(module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Modul nicht gefunden.")
    # Antworten nicht vorab mitsenden – nur Optionen
    return {
        "module_id": module_id,
        "title": module["title"],
        "questions": [
            {
                "id": q["id"],
                "question": q["question"],
                "options": q["options"],
            }
            for q in module["quiz"]
        ],
    }


@app.post("/api/modules/{module_id}/quiz/submit")
def submit_quiz(module_id: int, payload: QuizSubmit):
    if payload.module_id != module_id:
        raise HTTPException(status_code=400, detail="Modul-ID stimmt nicht überein.")
    module = get_module(module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Modul nicht gefunden.")

    by_id = {q["id"]: q for q in module["quiz"]}
    results = []
    correct_count = 0

    for answer in payload.answers:
        question = by_id.get(answer.question_id)
        if not question:
            raise HTTPException(
                status_code=400, detail=f"Unbekannte Frage: {answer.question_id}"
            )
        is_correct = answer.selected == question["correct"]
        if is_correct:
            correct_count += 1
        results.append(
            {
                "question_id": answer.question_id,
                "selected": answer.selected,
                "correct_index": question["correct"],
                "is_correct": is_correct,
                "explain": question["explain"],
            }
        )

    total = len(module["quiz"])
    percent = round((correct_count / total) * 100) if total else 0
    passed = percent >= 60

    return {
        "module_id": module_id,
        "correct": correct_count,
        "total": total,
        "percent": percent,
        "passed": passed,
        "results": results,
    }


@app.get("/", response_class=HTMLResponse)
def serve_index():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()


app.mount("/static", StaticFiles(directory="static"), name="static")
