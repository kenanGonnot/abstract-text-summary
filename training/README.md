## Training
Three distinct approaches were employed for model training:

* **Transformer Encoder-Decoder Model (From Scratch):** We trained a Transformer-based encoder-decoder model from scratch on a
  diverse dataset of text documents. This model was designed to understand the nuances of the summarization task and
  generate abstractive summaries through extensive training iterations.

* **Fine-tuning Llama-2-7b (7 Billion Parameters):** To harness the power of large pre-trained models, we fine-tuned the
  Llama-2-7b language model with the Ludwig library. This model, with its immense 7 billion parameters, offers the
  capability to generate high-quality abstractive summaries by leveraging a vast amount of prior knowledge.
* **Fine-tuning mT5-small (280 Million Parameters):** We also fine-tuned the mT5-small language model with the HuggingFace library - Transformers. This model, with its 280 million parameters, offers the capability to generate high-quality abstractive summaries in French and English by leveraging a vast amount of prior knowledge.

***
### Technical information:
* **Model Architecture:**
    * Transformer Encoder-Decoder Model
    * Fine-tuned Llama-2-7b (7 Billion Parameters)
    * Fine-tuned mT5-small (250 Million Parameters)
* **Dataset:** `XSum`
* **Training Time:** 2 days
* **Training Hardware:** 1x NVIDIA RTX 4090 GPU via [cloud GPU - VAST](https://vast.ai/)
* **Training Framework:**
    * TensorFlow (Transformer Encoder-Decoder Model)
    * Ludwig (Fine-tuned Llama-2-7b)
***

## More information about fine-tuning Google/mT5-small
n this project, three models were trained and fine-tuned for abstractive summarization. The model currently deployed is the Google/mT5-small model. It has been fine-tuned with PyTorch and HuggingFace on two datasets: "Xsum" in English and "Mlsum" in French. The fine-tuning process involved extensive preprocessing, data cleaning, and hyperparameter tuning to optimize the model's performance.

The choice of mT5-small was made with consideration for both efficiency and effectiveness in generating high-quality abstractive summaries. It's worth noting that the abstractive summarization task is a challenging one, as it requires the model to not only understand the content of the text but also to generate coherent and concise summaries.

Additionally, the project placed a strong emphasis on multilingual summarization capabilities. This enables the model to generate summaries in both English and French, making it versatile for a wide range of applications in various linguistic contexts.

The evaluation metrics for the model include Rouge scores, where we assess the quality and relevance of the generated summaries by comparing them to the reference summaries. This allows us to continually refine the model and ensure that it meets the desired standards for summarization in both languages.

Overall, this project represents a significant step in the field of abstractive summarization, pushing the boundaries of what can be achieved with state-of-the-art language models."

I've expanded the text and added additional information about the project's emphasis on multilingual capabilities and the use of Rouge scores for evaluation.

## More information about Ludwig and Llama-2-7b
* [Ludwig](https://ludwig.ai/latest/)

_"Ludwig is a low-code framework for building custom AI models like LLMs and other deep neural networks."_

>You can watch the following videos to learn more about Ludwig and Llama-2-7b:
>[Video YouTube - Efficient Fine-Tuning for Llama-2-7b on a single GPU](https://www.youtube.com/watch?v=g68qlo9Izf0)