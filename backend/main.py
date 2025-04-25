import logging
from fastapi import FastAPI, Depends, HTTPException, Form, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text, inspect

from typing import List
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from database import get_db, Base, engine
from models import Resume as ResumeModel, Base
from schemas import ResumeResponse
from ml_models import (
    predict_category,
    job_recommendation,
)
from utils import (
    extract_text_from_upload,
    extract_contact_number,
    extract_email,
    extract_skills,
    extract_education,
    extract_name,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    logger.info("Creating tables in the database if they do not exist...")
    Base.metadata.create_all(bind=engine)
    logger.info("Tables created successfully!")
except Exception as e:
    logger.error(f"Error creating tables: {e}")

# Inspect the database to print the list of tables
inspector = inspect(engine)
tables = inspector.get_table_names(schema="public")
if "resumes" in tables:
    print("Table 'resumes' exists.")
else:
    print("Table 'resumes' does not exist.")   

app = FastAPI()

# Configure CORS to allow requests from your Angular frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Adjust this list to match your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def insert_resume(db_session, resume_data):
    query = text("""
        INSERT INTO resumes (filename, predicted_category, recommended_job, phone, email, skills, education, name)
        VALUES (:filename, :predicted_category, :recommended_job, :phone, :email, :skills, :education, :name)
        RETURNING id, created_at
    """)

    print("\n SQL Query to be executed:", query)
    print("Parameters:", resume_data)

    result = db_session.execute(query, resume_data)
    db_session.commit()
    
    inserted_id, created_at = result.fetchone()
    return inserted_id, created_at

    
# --- Resume Screening Endpoints ---

@app.post("/api/predict_resume", response_model=ResumeResponse)
async def predict_resume(
    resume: UploadFile = File(...), db: Session = Depends(get_db)
):
    filename = resume.filename.lower()
    text = ""
    if filename.endswith(".pdf") or filename.endswith(".txt") or filename.endswith(".docx"):
        text = await extract_text_from_upload(resume)
    else:
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a PDF, DOCX or TXT file.")

    predicted_category = predict_category(text)
    recommended_job = job_recommendation(text)
    phone = extract_contact_number(text)
    email = extract_email(text)
    skills = extract_skills(text)
    education = extract_education(text)
    name = extract_name(text)

    # Save the resume details in the database
    resume_data = ResumeModel(
        filename=resume.filename,
        predicted_category=predicted_category,
        recommended_job=recommended_job,
        phone=phone,
        email=email,
        skills=", ".join(skills) if skills else None,
        education=", ".join(education) if education else None,
        name=name,
    )
    db.add(resume_data)
    db.commit()
    db.refresh(resume_data)

    return resume_data

# --- Job Matching Endpoints ---

@app.post("/api/match_resumes", response_class=JSONResponse)
async def match_resumes(
    job_description: str = Form(...),
    resumes: List[UploadFile] = File(...),
):
    texts = []
    filenames = []
    for resume in resumes:
        text = await extract_text_from_upload(resume)
        texts.append(text)
        filenames.append(resume.filename)

    if not texts or not job_description:
        raise HTTPException(status_code=400, detail="Please upload resumes and enter a job description.")

    corpus = [job_description] + texts
    vectorizer = TfidfVectorizer().fit_transform(corpus)
    vectors = vectorizer.toarray()
    job_vector = vectors[0]
    resume_vectors = vectors[1:]

    similarities = cosine_similarity([job_vector], resume_vectors)[0]
    top_indices = np.argsort(similarities)[-5:][::-1]
    top_resumes = [filenames[i] for i in top_indices]
    similarity_scores = [round(float(similarities[i] * 100), 2) for i in top_indices]

    return {
        "top_resumes": top_resumes,
        "similarity_scores": similarity_scores,
    }

# --- API Endpoint to Retrieve a Resume Entry ---

@app.get("/api/resumes/{resume_id}", response_model=ResumeResponse)
def get_resume(resume_id: int, db: Session = Depends(get_db)):
    resume = db.query(ResumeModel).filter(ResumeModel.id == resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    return resume
