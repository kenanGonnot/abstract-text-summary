FROM python:3.7.13

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m nltk.downloader punkt
RUN python -c "from transformers import AutoModelForSeq2SeqLM, AutoTokenizer; model = AutoModelForSeq2SeqLM.from_pretrained('thekenken/mt5small-finetuned-summary-en-fr'); tokenizer = AutoTokenizer.from_pretrained('thekenken/mt5small-finetuned-summary-en-fr')"

# Copiez les fichiers de l'application
COPY *.py ./

# Commande d'entrée
CMD ["python", "app.py"]

# Exposez le port 5004
EXPOSE 5004
