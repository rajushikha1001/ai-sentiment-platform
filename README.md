# AI Sentiment Analysis Platform — End-to-End MLOps Project

An **end-to-end AI Platform MVP** built to practice **AI Architecture & MLOps engineering** — going beyond model training into **real-world system design, deployment, observability, and lifecycle management.**

This project implements a **complete Sentiment Analysis Platform**, including:

✅ Data ingestion & preprocessing  
✅ ML model training pipeline  
✅ Model registry & experiment tracking using MLflow  
✅ FastAPI inference service  
✅ Structured logging & latency monitoring  
✅ Reproducible development environment  
✅ Modular, production-style folder structure  

---

## Tech Stack

| Layer | Technologies |
|------|-------------|
| Language | Python |
| ML | Scikit-Learn, Pandas |
| Serving | FastAPI, Uvicorn |
| MLOps | MLflow |
| Logging | Python Logging |
| Packaging | venv, Makefile |
| OS | Windows-friendly setup |

---

## Features

### Machine Learning
✔️ TF-IDF + Logistic Regression  
✔️ Training pipeline  
✔️ Accuracy metric logging  
✔️ Model persistence (`sentiment.pkl`)  

---

### FastAPI Inference Service
Exposes `/predict` endpoint to score text sentiment.

🔹 POST JSON → Response with prediction & latency  
🔹 Model loaded once (cached in memory)  
🔹 Input validation via Pydantic  

---

### MLflow Experiment Tracking
Tracks:

✔️ Runs  
✔️ Parameters  
✔️ Accuracy metrics  
✔️ Stored model artifacts  
✔️ Registered models  

MLflow UI available at:

