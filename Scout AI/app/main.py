from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import PlainTextResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from typing import Dict, Any
import os

from app.recommender import recommend_jobs_with_skill_gap
from app.interview import recommend_interview_questions
from app.pdf_parser import extract_resume_text

app = FastAPI(
    title="Scout AI",
    description="Full Stack AI Resume Analyzer API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

if FRONTEND_DIR.exists():
    app.mount("/frontend", StaticFiles(directory=str(FRONTEND_DIR)), name="frontend")


@app.get("/", response_class=PlainTextResponse)
def root():
    return "Scout AI API Running"


@app.get("/ui")
def serve_ui():
    index_file = FRONTEND_DIR / "index.html"

    if index_file.exists():
        return FileResponse(index_file)

    return PlainTextResponse(
        "Frontend HTML not found.",
        status_code=404
    )


@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    try:

        os.makedirs("uploads", exist_ok=True)

        file_path = os.path.join("uploads", file.filename)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        resume_text = extract_resume_text(file_path)

        recommendations = recommend_jobs_with_skill_gap(
            resume_text=resume_text,
            top_k=5
        )

        interview_questions = recommend_interview_questions(
            top_k=5
        )

        return {
            "recommendations": recommendations,
            "interview_questions": interview_questions
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )