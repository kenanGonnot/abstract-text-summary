import json
import os

import spacy
from flask import Flask, jsonify, request

from text_summarization import extractive_summarization, abstractive_summarization_pipeline, \
    calculate_cosine_similarity, generate_abstractive_summary

import nltk
nltk.download("punkt")

spacy.cli.download("en_core_web_sm")
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/v1/inference/text_summarization/extract', methods=["GET"])
def extractive_summary():
    """
    Extractive Summarization
    """
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
        data = json.loads(data)
        paragraphs = data['input_text']
        if paragraphs is [] or paragraphs is None:
            return jsonify("No paragraph found")
    else:
        return jsonify("Content-Type must be application/json")
    summary = extractive_summarization(paragraphs)
    similarity = calculate_cosine_similarity(paragraphs, summary)
    response = {
        "summary": summary,
        "similarity": similarity
    }
    return jsonify(response)


@app.route('/v1/inference/text_summarization/abstract', methods=["GET"])
def abstractive_summary():
    """
    Abstractive Summarization
    """
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
        # data = json.loads(data)
        paragraphs = data['input_text']
        if paragraphs is [] or paragraphs is None:
            return jsonify("No paragraph found")
    else:
        paragraphs = request.args.get('input_text')
    # model = "JulesBelveze/t5-small-headline-generator"
    # model = "thekenken/ludwig-llama7b-summarization"
    # model = "google/pegasus-xsum"
    model = "thekenken/mt5small-finetuned-summary-en-fr"
    framework = "pt"  # pytorch or tf (tensorflow)
    # summary = abstractive_summarization_pipeline(paragraphs, model, framework,  max_length=200, min_length=50)
    summary = generate_abstractive_summary(model, paragraphs, max_length=150, min_length=50)
    similarity = calculate_cosine_similarity(paragraphs, summary)
    response = {
        "summary": summary,
        "similarity": similarity
    }
    return jsonify(response)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5004))
    app.run(debug=True, host='0.0.0.0', port=port)
