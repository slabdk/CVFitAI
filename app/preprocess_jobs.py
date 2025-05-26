import pandas as pd

def preprocess_job_data(path="app/data/postings.csv"):
    # CSV dosyasını oku
    df = pd.read_csv(path)

    # Sütun adlarını temizle
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # İşimize yarayan sütunları al
    keep_columns = ['title', 'description', 'skills_desc']
    df = df[[col for col in keep_columns if col in df.columns]]

    # Eksik satırları temizle (boş olanları at)
    df = df.dropna(subset=keep_columns)

    # Tüm string hücrelerde baş/son boşlukları temizle
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    return df
