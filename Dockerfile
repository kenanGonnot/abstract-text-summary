FROM python:3.7.13
#FROM tensorflow/serving

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
#RUN python -m spacy download en_core_web_sm
COPY *.py ./

CMD [ "python", "app.py" ]

EXPOSE 5004