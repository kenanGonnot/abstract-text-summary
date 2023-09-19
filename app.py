import json
import os

import spacy
from flask import Flask, jsonify, request

from text_summarization import extractive_summarization, abstractive_summarization

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
    response = {
        "summary": summary
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
        data = json.loads(data)
        paragraphs = data['input_text']
        if paragraphs is [] or paragraphs is None:
            return jsonify("No paragraph found")
    else:
        paragraphs = request.args.get('input_text')
    model = "JulesBelveze/t5-small-headline-generator"
    # model = "thekenken/ludwig-llama7b-summarization"
    # model = "deep-learning-analytics/wikihow-t5-small"
    # model = "google/pegasus-xsum"
    # model = "thekenken/text_summarization"
    framework = "pt" # pytorch or tf (tensorflow)
    summary = abstractive_summarization(paragraphs, model, framework)
    response = {
        "summary": summary
    }
    return jsonify(response)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5004))
    app.run(debug=True, host='0.0.0.0', port=port)
