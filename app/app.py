from load_data import load_resume_data

df = load_resume_data()

# Örnek: İlk 5 satırı yazdır
print(df[['skills', 'job_position_name', 'matched_score']].head())
