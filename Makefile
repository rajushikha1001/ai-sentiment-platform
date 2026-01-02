PYTHON=python
VENV=venv
ACTIVATE=$(VENV)\Scripts\activate

.PHONY: help venv install pipeline train api run-all clean

help:
	@echo Available commands:
	@echo   make venv
	@echo   make install
	@echo   make pipeline
	@echo   make train
	@echo   make api
	@echo   make run-all
	@echo   make clean

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(ACTIVATE) && $(PYTHON) -m pip install --upgrade pip
	$(ACTIVATE) && $(PYTHON) -m pip install -r data_pipeline/requirements.txt
	$(ACTIVATE) && $(PYTHON) -m pip install -r model_service/requirements.txt
	$(ACTIVATE) && $(PYTHON) -m pip install -r api_gateway/requirements.txt

pipeline:
	$(ACTIVATE) && $(PYTHON) data_pipeline/ingest.py
	$(ACTIVATE) && $(PYTHON) data_pipeline/preprocess.py

train:
	$(ACTIVATE) && $(PYTHON) -m model_service.train

api:
	$(ACTIVATE) && uvicorn api_gateway.main:app --reload

run-all: install pipeline train api

clean:
	rmdir /S /Q $(VENV) 2>nul || true
	del dataset.csv 2>nul || true
	del clean_dataset.csv 2>nul || true
	rmdir /S /Q models 2>nul || true
