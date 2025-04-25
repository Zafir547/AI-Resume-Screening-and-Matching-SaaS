import pickle
import re

# Load the saved ML models
rf_classifier_categorization = pickle.load(open('models/rf_classifier_categorization.pkl', 'rb'))
tfidf_vectorizer_categorization = pickle.load(open('models/tfidf_vectorizer_categorization.pkl', 'rb'))
rf_classifier_job_recommendation = pickle.load(open('models/rf_classifier_job_recommendation.pkl', 'rb'))
tfidf_vectorizer_job_recommendation = pickle.load(open('models/tfidf_vectorizer_job_recommendation.pkl', 'rb'))

def clean_resume(text: str) -> str:
    clean_text = re.sub('http\S+\s', ' ', text)
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\S+\s', ' ', clean_text)
    clean_text = re.sub('@\S+', ' ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', ' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)
    return clean_text

def predict_category(text: str) -> str:
    text = clean_resume(text)
    resume_tfidf = tfidf_vectorizer_categorization.transform([text])
    predicted_category = rf_classifier_categorization.predict(resume_tfidf)[0]
    return predicted_category

def job_recommendation(text: str) -> str:
    text = clean_resume(text)
    resume_tfidf = tfidf_vectorizer_job_recommendation.transform([text])
    recommeded_job = rf_classifier_job_recommendation.predict(resume_tfidf)[0]
    return recommeded_job