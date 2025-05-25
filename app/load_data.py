import pandas as pd

def load_resume_data(path="app/data/CVdata.csv"):
    df = pd.read_csv(path)
    df.columns = df.columns.str.replace('\ufeff', '')  # BOM temizle
    return df
