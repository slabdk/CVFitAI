import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    # Sütun adlarını temizle
    df.columns = df.columns.str.strip().str.replace('\ufeff', '')

    # Gereksiz/çift sütun varsa sil
    df = df.drop(columns=["responsibilities"], errors="ignore")

    # matched_score sayıya çevrilmeli
    df["matched_score"] = pd.to_numeric(df["matched_score"], errors="coerce")

    # Eksik kritik alanları temizle
    df = df.dropna(subset=["skills", "skills_required", "matched_score"])

    # career_objective boşsa Unknown yap
    df["career_objective"] = df["career_objective"].fillna("Unknown")

    # Tüm string hücreleri kırp
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    return df
