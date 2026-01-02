import pandas as pd
from pathlib import Path

DATA_PATH = Path("data_pipeline/dataset.csv")
OUT_PATH = Path("data_pipeline/clean_dataset.csv")

def preprocess():
    df = pd.read_csv(DATA_PATH)
    df["text"] = df["text"].str.lower()
    df.to_csv(OUT_PATH, index=False)
    print("clean_dataset.csv created")

if __name__ == "__main__":
    preprocess()
