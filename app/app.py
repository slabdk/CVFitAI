from preprocess import preprocess_resume_csv
from preprocess_jobs import preprocess_job_csv

# Veri temizleme
preprocess_resume_csv("app/data/Resume.csv", "app/cleaned_data/cleaned_resumes.csv")
preprocess_job_csv("app/data/training_data.csv", "app/cleaned_data/cleaned_jobs.csv")
