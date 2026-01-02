import joblib
from pathlib import Path 

MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

def save_model(model):
    joblib.dump(model, MODEL_DIR / "sentiment.pkl")

def load_model():
    return joblib.load(MODEL_DIR / "sentiment.pkl")
    
        