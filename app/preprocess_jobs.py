import os
import pandas as pd
def preprocess_job_csv(input_path, output_path):
    df = pd.read_csv(input_path)

    if 'job_description' in df.columns:
        text_column = 'job_description'
    elif 'Job_Description' in df.columns:
        text_column = 'Job_Description'
    elif 'description' in df.columns:
        text_column = 'description'
    else:
        raise ValueError(
            "CSV'de iş tanımı için 'job_description', 'Job_Description' ya da 'description' sütunu bulunamadı.")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Temizlenmiş iş ilanı verisi şuraya kaydedildi: {output_path}")
