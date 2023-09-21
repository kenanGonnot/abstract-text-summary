# Abstractive Text Summarization - Transformers

![m-abstract-extract.png](assets%2Fm-abstract-extract.png)

## Project Description

This GitHub project is dedicated to the development of an Abstractive Text Summarization system using advanced deep
learning techniques. The goal of this project is to create a model that can generate concise and coherent summaries of
long textual documents, capturing the essential meaning and context of the original content.

## Demo:

You can try out my Abstractive Text Summarization model through my [online demo
](http://kenan.gonnot.net/text_summarization).



> If you want to train your own model, please refer to the [Training](training) page.

## Key Features

* Utilizes state-of-the-art Natural Language Processing (NLP) models such as Transformers.
* Pre-trained language models for improved performance.
* Support for multiple languages and various text data formats.
* User-friendly interface for text input and summary generation.
* Option for customization and fine-tuning for specific domains.

### Why Abstractive Summarization

Abstractive summarization goes beyond simply extracting sentences from the source text; it generates human-like
summaries that can be more informative and concise. This technology has applications in content curation, document
summarization, and even chatbots to generate coherent responses.

### How it works

Abstractive text summarization is an advanced Natural Language Processing (NLP) technique that aims to distill the
essential meaning and context from a longer text into a concise and coherent summary. Unlike extractive summarization,
which selects and combines existing sentences from the source text, abstractive summarization involves generating
entirely new sentences that capture the core information.

#### The process typically involves the following steps:

1. **Text Preprocessing:** The input text undergoes preprocessing to remove noise, tokenize sentences and words, and
   handle special characters. This ensures the text is in a suitable format for NLP models.
2. **Model Selection:** Abstractive summarization often utilizes deep learning models, such as Transformer-based architectures,
   due to their ability to capture complex language patterns. These models are pre-trained on vast corpora of text data,
   which helps them understand grammar, context, and semantics.
3. **Fine-tuning (Optional):** In some cases, pre-trained models can be fine-tuned on domain-specific data to enhance their
   summarization capabilities for particular industries or topics.
4. **Encoding:** The input text is encoded into a numerical representation that the model can understand. This
   representation
   captures the semantic meaning of words and sentences.
5. **Decoding:** The model decodes the encoded representation to generate a summary. During this step, it predicts and
   generates words one at a time, considering context and coherence. Beam search or other decoding techniques may be used
   to improve the quality of generated summaries.
6. **Evaluation:** The generated summary is evaluated using metrics such as ROUGE (Recall-Oriented Understudy for Gisting
   Evaluation) to measure its similarity and quality compared to reference summaries or gold standards.

Abstractive text summarization finds applications in various domains, including content curation, document
summarization, chatbots, and more. It provides a more human-like summarization approach, allowing the creation of
concise and informative summaries that can be valuable for readers and automation tasks.

> In summary, abstractive text summarization is a sophisticated NLP technique that leverages deep learning models to
> generate coherent and contextually accurate summaries from longer texts, making it a powerful tool for information
> extraction and content optimization.

### Future Enhancements

* Multimodal summarization (text and images).
* Enhanced support for summarization of scientific papers.
* Integration with web scraping tools for automatic content summarization from websites.

***

# How to run the app

## Prerequisites

* Docker
* Kubernetes

## Information about the project

* `app.py` - the main file of the app - API via FLASK
* `requirements.txt` - the list of requirements
* `text_summarization.py` - the file that summarize the text
* `manifests/` - the folder that contains the manifest files (k8s specifications)
    * `Ingress.yml` - to expose the app on the internet via GCP
* `training/` - the folder that contains the training files

## How to use the app

1. Clone the repo
2. Create a virtual environment
```bash 
 python3 -m venv venv
 source venv/bin/activate 
```
2. Install the requirements

```bash
pip install -r requirements.txt
```

3. Run the app

```bash
python app.py
```

4. Curl the API

```bash
curl -X POST -H "Content-Type: application/json" -d '{"input_text":$YOUR_TEXT}' http://localhost:5004/v1/inference/text_summarization/abstract
```

Replace `$YOUR_TEXT` with your text.

Example:

```string
One Piece is one of the most daunting anime one could start watching. It began when mangaka, Eiichiro Oda, started publishing One Piece in Weekly Shonen Jump’s manga magazine in 1997. It would get a quick anime adaption that started airing in 1999, and it became known as one of Shonen Jump’s “Big Three,” the most popular titles in the magazine, alongside Bleach and Naruto. Roughly a decade after the term the Big Three was coined, One Piece is the only manga and anime still running with weekly manga chapters and anime episodes.
One Piece is the story of Monkey D. Luffy, a young man who has a single dream: To find the legendary treasure known as the One Piece and become the King of the Pirates. Alongside a crew of trusted friends, Luffy sails the dangerous seas of the Grand Line to find Laugh Tale, the hidden island containing the One Piece. On his journey, Luffy faces many dangerous foes, including fellow pirates who want to conquer the seas, and the Navy who want to purge the world of the pirate menace.
With over a thousand published chapters and nearly as many anime episodes, One Piece has gathered an immense cast of characters, two rich magic systems, and a depth of lore across many diverse locales. This depth can make it hard for new viewers to jump into the anime or the manga, and this article will get you started by explaining the two magic systems: Devil Fruits and Haki.Of the two magic systems, Devil Fruits are the oldest and perhaps one of Oda’s greatest creations in the entire manga. Introduced at the beginning of the story, Devil Fruits have always been a vital part of One Piece’s frequent spectacular battles. Devil Fruits are incredibly rare and distinctive fruits that grant anyone who eats a single bite incredible powers. The fruits are easily identifiable, thanks to their vibrant colors, an intricate pattern of swirls on their skin, and by their foul taste. No two Devil Fruits grant the same power, but all Devil Fruit eaters share two weaknesses: The ocean and Sea Prism Stone.All Devil Fruit eaters lose their ability to swim after consuming the Devil Fruit. It’s not just a loss of muscle memory; entering a body of water saps them of all energy. Even entering a bath can drain a Devil Fruit eater of energy and prevent them from using their abilities. Notably, it does need to be a body of water. Simply spilling a glass of water on them or spraying them with a hose wouldn’t have the same effect. One Piece is an anime about pirates sailing the high seas, making this an especially devastating weakness. One poor battle on the ocean can send a Devil Fruit eater to their death, or even just a patch of rough water. It’s currently unknown why Devil Fruit eaters can’t swim. One explanation is because the ocean hates those with Devil Fruit powers, but it’s unclear if this is the truth or one of the many myths that have grown around the Fruits over the centuries.Sea Prism Stone is known as a stone that has the same properties as the ocean. When a Devil Fruit eater touches Sea Prism Stone, it provokes a response very similar to being dropped in the ocean, draining them of their energy and preventing them from using their powers. The Sea Prism Stone is also impervious to any Devil Fruit powers used on it.
Sea Prism Stone is most commonly used to build cuffs and chains that bind Devil Fruit users, keeping them lethargic and powerless for easy capture and detainment. However, it has several other applications; offensively, the Navy makes bullets and nets from it to capture Devil Fruit eaters easier. The Navy has also been known to line the bottoms of their ships with the Stone to deter violent ocean life from attacking them. The Devil Fruits are central to One Piece’s appeal by offering a wild variety of abilities that help keep battles interesting while showing off Oda’s immense creative abilities. One hallmark of Devil Fruits is that they’re only as powerful as the user, offering greater strength to those willing to test the limits of their power and use their minds as well as their fists. While no two Devil Fruits grant the same abilities, they are grouped into three classes: Zoan, Logia, and Paramecia.Zoan-type fruits offer their users the ability to transform and shapeshift, most often into some form of animal, though a member of Luffy's crew, Chopper is a reindeer who ate the Human-Human Fruit. Most Zoan users gain access to several transformations that range from completely human to completely bestial, though they retain their human minds regardless of their form. Zoan-types can be further divided into two especially rare subclasses: Mythical and Ancient. Mythical Zoan-types allow their users to become creatures straight from myths and legends. A great example of a mythical Zoan Fruit is the one possessed by Kaido, a fearsome villain who’s known as a Yonko, one of the Four Emperors of the Sea. Kaido’s Fish-Fish Fruit: Azure Dragon Model allows him to become a massive dragon, allowing Kaido to uphold his reign of terror in the New World Ancient-type Zoan Fruits allow their users to become long-extinct creatures like dinosaurs, such as X Drake’s Dragon-Dragon Fruit: Allosaurus Model that allows him to become a powerful allosaurus. Mythical and ancient Zoan Fruits are immensely rare compared to average Zoan types, and even Devil Fruits in general and are considered stronger than ordinary Zoan like Chopper’s Human-Human Fruit.Logia-type Devil Fruits are the rarest and most powerful type of Devil Fruit. They grant elemental-based powers, including the four elements of fire, water, earth, and air most Western audiences will be familiar with. While some of the Fruits grant one of these directly, such as the Flare-Flare Fruit that grants fire-based abilities, they also offer unique ways of using them. Both the Gas-Gas Fruit and the Smoke-Smoke Fruit involve air-based powers but have very different uses. All Logia-types allow their users to generate infinite amounts of their element, giving them extremely powerful offensive capabilities. The true strength of Logia-type fruits, however, lies in how they make the eater a part of that element. Logia-type users are incredibly hard to harm, with many of them being incorporeal. For example, one of protagonist Luffy’s greatest rivals is Navy Vice Admiral Smoker, who ate the Smoke-Smoke Fruit. Trying to strike Smoker without Sea Prism Stone or Haki is like trying to punch a pile of smoke - completely ineffective. Logia-types can also make part or all of their bodies into their element, giving them a variety of ways to manipulate their environment and attack. The combination of offense and defense capabilities is what makes Logia-type users such dangerous foes.Paramecia-type Devil Fruits are the most common type of Devil Fruit and offer a wide range of abilities, acting as a catch-all for fruits that don’t allow animal transformation or element-based powers. However, they are sorted into three groups: Body manipulation, environmental manipulation, and substance generation. The best example of body manipulation Paramecia lies in the protagonist, Luffy. After eating the Gum-Gum Fruit, Luffy became a rubber person - his body is incredibly stretchy and resistant to many physical-based attacks because he bounces back. His body always has the same properties as rubber. Other body manipulation fruits work on command, such as the Weapon-Weapon Fruit that allows its user to turn their arms and legs into various weapons.
Environmental manipulation Fruits let their users dramatically alter the environment around them, working on either inanimate objects, living objects, or both. An especially powerful environmental manipulation fruit is the Ope-Ope Fruit, possessed by Trafalgar Law. Law can create an environment called a “Room” around him in a sphere and can manipulate anything within his sphere as he pleases, living or not. Finally, substance-generating Paramecia-types can appear similar to Logia-types. Users with this kind of fruit are capable of producing infinite amounts of a substance and manipulating it to their will, but they are not made of it the way a Logia-type user is. An example of this Devil Fruit is the String-String Fruit possessed by the villain, Doflamingo. Doflamingo can produce incredibly strong, sharp strings for a variety of purposes such as flying and attacking, but he’s unable to make his body into strings; any blows against him will strike normally.Haki is the second magic system introduced in One Piece. Haki wasn’t properly introduced until the Marineford Arc, just before a two-year time skip that theoretically marks the halfway point of One Piece, but it was hinted at several times before this arc. Haki is a way of utilizing a person’s spiritual energy in offensive or defensive manners. Unlike Devil Fruit powers, which are only obtainable by consuming the rare Fruits, any living person is capable of awakening their Haki though the vast majority of people go their entire lives without knowing it even exists. There are three major types of Haki: Observational, Armament, and Conqueror’s.  
```

## Acknowledgments:

We extend our gratitude to the contributors of popular NLP libraries and datasets that have made this project possible.

## Contact

* Kenan Gonnot - [linkedin](https://www.linkedin.com/in/kenan-gonnot/) 
