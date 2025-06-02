import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import os

nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'http\S+', ' ', text)
    text = re.sub(r'[^a-z\s]', ' ', text)
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and len(word) > 2]
    return ' '.join(tokens)


def preprocess_resume_csv(input_path, output_path):
    df = pd.read_csv(input_path)

    if 'Resume_str' not in df.columns:
        raise ValueError("CSV dosyasında 'Resume_str' sütunu bulunamadı.")
    df['Cleaned_Resume'] = df['Resume_str'].apply(clean_text)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Temizlenmiş CV verisi şuraya kaydedildi: {output_path}")
