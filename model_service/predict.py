from .model_registry import load_model

model = load_model()

def predict(text: str):
    return int(model.predict([text])[0])
