import time
from collections import Counter
from heapq import nlargest
from string import punctuation

import spacy
from spacy.lang.en import STOP_WORDS
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

from langdetect import detect
import pandas as pd
import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_cosine_similarity(document, summary):
    # Créez un vecteur TF-IDF à partir du document et du résumé
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([document, summary])

    # Calculez la similarité cosinus entre le document et le résumé
    cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

    # La similarité cosinus varie de 0 (pas de similarité) à 1 (similitude maximale)
    return round(cosine_sim[0][0] * 100, 2)


def filtering_tokens(documents):
    keyword = []
    stopwords = list(STOP_WORDS)
    pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
    for token in documents:
        if token.text in stopwords or token.text in punctuation:
            continue
        if token.pos_ in pos_tag:
            keyword.append(token.text)
    return keyword


def normalization(keywords, freq_word):
    max_freq = Counter(keywords).most_common(1)[0][1]
    for word in freq_word.keys():
        freq_word[word] = (freq_word[word] / max_freq)
    return freq_word


def weighing_sentences(doc, freq_word):
    sent_strength = {}
    for sent in doc.sents:
        for word in sent:
            if word.text in freq_word.keys():
                if sent in sent_strength.keys():
                    sent_strength[sent] += freq_word[word.text]
                else:
                    sent_strength[sent] = freq_word[word.text]
    return sent_strength


def extractive_summarization(body):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(body)
    print("Number of sentences :  ", len(list(doc.sents)))

    keywords = filtering_tokens(doc)

    ''' Calculate the frequency of each token using the Counter function '''
    freq_word = Counter(keywords)
    freq_word.most_common(5)

    ''' Normalization '''
    freq_word = normalization(keywords, freq_word)

    ''' Weighing sentences '''
    sent_strength = weighing_sentences(doc, freq_word)

    ''' Summarize the string '''
    summarized_spacy_span = nlargest(7, sent_strength, key=sent_strength.get)

    ''' Convert the sentences spacy.tokens.span.Span to a string '''
    summarized_sentences = [w.text for w in summarized_spacy_span]
    summary = ' '.join(summarized_sentences)

    # df = pd.DataFrame({"paragraph": body, "summary": summary}, index=[0])
    # return df.to_json(orient="records")
    return summary


def abstractive_summarization_pipeline(paragraph, model_name, framework="pt", max_length=200, min_length=50):
    start = time.time()
    summarizer = pipeline("summarization", model=model_name, tokenizer=model_name, framework=framework)

    summary = summarizer(
        paragraph,
        min_length=min_length,
        max_length=max_length,
    )

    end = time.time()
    print("Time : {} seconds".format(end - start))
    return summary[0]['summary_text']


def split_text_into_sentences(text, language="english"):
    # Découpez le texte en phrases en fonction de la langue
    if language == "fr":
        language = "french"
    if language == "en":
        language = "english"
    sentence_splitter = nltk.data.load(f'tokenizers/punkt/{language}.pickle')
    sentences = sentence_splitter.tokenize(text)
    return sentences


def generate_abstractive_summary(hub_model_id, text, max_length=150, min_length=50):
    tokenizer = AutoTokenizer.from_pretrained(hub_model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(hub_model_id)
    language = detect(text)
    print("Language: ", language)

    # Découpez le texte en phrases en fonction de la langue
    sentences = split_text_into_sentences(text, language)

    # Générer un résumé pour chaque phrase
    summaries = []

    if len(sentences) > 4:
        # Si le document a plus de 4 phrases, divisez-le en deux parties
        midpoint = len(sentences) // 2
        first_half = sentences[:midpoint]
        second_half = sentences[midpoint:]
        print("Le document possède plus de 4 phrases: {} phrases".format(len(sentences)))

        for sentences_to_summarize in [first_half, second_half]:
            summary = model.generate(
                tokenizer.encode(" ".join(sentences_to_summarize), return_tensors="pt"),
                max_length=max_length,
                min_length=25,
                num_beams=5,  # Augmenter num_beams pour des résumés de meilleure qualité
                early_stopping=True,  # Assurez-vous que la génération se termine correctement
            )[0]
            summaries.append(tokenizer.decode(summary, skip_special_tokens=True))
    else:
        # Générez un résumé pour l'ensemble du texte
        print("Le document possède moins de 4 phrases")
        summary = model.generate(
            tokenizer.encode(text, return_tensors="pt"),
            max_length=max_length,
            min_length=min_length,
            num_beams=5,  # Augmenter num_beams pour des résumés de meilleure qualité
            early_stopping=True,  # Assurez-vous que la génération se termine correctement
        )[0]
        summaries.append(tokenizer.decode(summary, skip_special_tokens=True))

    # Concaténez les résumés des phrases (ou des moitiés) pour obtenir le résumé complet
    full_summary = " ".join(summaries)
    return full_summary


if __name__ == '__main__':
    print("Start Summarization ...")
    # start_time = time.time()
    # spacy.cli.download("en_core_web_sm")
    # df = extractive_summarization(body)
    # print("=========================================")
    # print("Body : ", body)
    # print("=========================================")
    # print("Summarization : ", df)
    # print("=========================================")
    # print("type : ", type(df))
    # print("Summarization Done in %s seconds" % (time.time() - start_time))
