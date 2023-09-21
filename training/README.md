## Training
Two distinct approaches were employed for model training:

* **Transformer Encoder-Decoder Model (From Scratch):** We trained a Transformer-based encoder-decoder model from scratch on a
  diverse dataset of text documents. This model was designed to understand the nuances of the summarization task and
  generate abstractive summaries through extensive training iterations.

* **Fine-tuning Llama-2-7b (7 Billion Parameters):** To harness the power of large pre-trained models, we fine-tuned the
  Llama-2-7b language model with the Ludwig library. This model, with its immense 7 billion parameters, offers the
  capability to generate high-quality abstractive summaries by leveraging a vast amount of prior knowledge.

***
### Technical information:
* **Model Architecture:**
    * Transformer Encoder-Decoder Model
    * Fine-tuned Llama-2-7b (7 Billion Parameters)
* **Dataset:** `XSum`
* **Training Time:** 2 days
* **Training Hardware:** 1x NVIDIA RTX 4090 GPU via [cloud GPU - VAST](https://vast.ai/)
* **Training Framework:**
    * TensorFlow (Transformer Encoder-Decoder Model)
    * Ludwig (Fine-tuned Llama-2-7b)
***

## More information about Ludwig and Llama-2-7b
* [Ludwig](https://ludwig.ai/latest/)

_"Ludwig is a low-code framework for building custom AI models like LLMs and other deep neural networks."_

>You can watch the following videos to learn more about Ludwig and Llama-2-7b:
>[Video YouTube - Efficient Fine-Tuning for Llama-2-7b on a single GPU](https://www.youtube.com/watch?v=g68qlo9Izf0)