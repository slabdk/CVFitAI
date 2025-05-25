from load_data import load_resume_data
from preprocess import preprocess_data

df = load_resume_data()
df = preprocess_data(df)

# İlk satırları kontrol et
print(df[['skills', 'skills_required', 'matched_score']].head())
