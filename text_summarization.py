import time
from collections import Counter
from heapq import nlargest
from string import punctuation

import spacy
from spacy.lang.en import STOP_WORDS
from transformers import pipeline

import pandas as pd


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


def abstractive_summarization(paragraph, model_name, framework="pt"):
    start = time.time()
    # model = "thekenken/text_summarization"
    # tokenizer = "thekenken/text_summarization"
    # model = "t5-small"
    # tokenizer = "t5-small"
    summarizer = pipeline("summarization", model=model_name, tokenizer=model_name, framework=framework)

    summary = summarizer(
        paragraph,
        # raw_datasets["test"][0]["document"],
        min_length=80,
        max_length=500,
    )

    end = time.time()
    print("Time : {} seconds".format(end - start))
    # df = pd.DataFrame({"paragraph": paragraph, "summary": summary[0]['summary_text']}, index=[0])
    # return df.to_json(orient="records")
    return summary[0]['summary_text']

# from transformers import pipeline


# def extractive_summarization_bt(body):
#     # use bart in pytorch
#     # summarizer = pipeline("summarization")
#     # ptorch = summarizer("An apple a day, keeps the doctor away", min_length=5, max_length=20)
#
#     # use t5 in tf
#     summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
#     tflow = summarizer(body, min_length=5, max_length=500)
#     return tflow
# print(ptorch, tflow)

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
