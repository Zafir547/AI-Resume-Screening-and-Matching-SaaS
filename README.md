# AI-Resume-Screening-and-Matching-SaaS

## Tech Stack

- Frontend: Angular + SCSS
- Backend: FastAPI (Python)
- Database: Azure PostgreSQL
- ML Tools: Scikit-learn, TfidfVectorizer, cosine_similarity
- Resume Parsers: PyPDF2, docx2txt

## Resume Matching Flow

1. Enter Job Description
2. Upload Multiple Resumes
3. Compute Similarity (TF-IDF + Cosine Similarity)
4. Top 5 Closest Matches Shown

## Machine Learning Models

- Job Categorization: Trained using labeled resume data
- Text Vectorization: TfidfVectorizer
- Similarity Measure: Cosine Similarity for matching
- Model Deployment: Integrated in FastAPI

# How to Run Code in Terminal:

backend: uvicorn main:app --host 0.0.0.0 --port 8000 --reload

frontend/my-angular-app: ng serve

Open the Website locally: http://localhost:4200/






