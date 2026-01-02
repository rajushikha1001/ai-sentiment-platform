import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from .model_registry import save_model

# Resolve project root
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data_pipeline" / "clean_dataset.csv"

print(f"Loading data from: {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

pipeline.fit(df["text"], df["label"])

save_model(pipeline)

print("Model trained & saved.")


