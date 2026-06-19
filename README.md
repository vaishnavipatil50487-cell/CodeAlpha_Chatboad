# FAQ Chatbot Using Python

## Project Overview

This project is a simple FAQ (Frequently Asked Questions) Chatbot developed using Python. The chatbot answers user queries by matching them with predefined FAQ questions using Natural Language Processing (NLP) techniques.

The system uses TF-IDF Vectorization and Cosine Similarity to find the most relevant answer from the FAQ dataset.

---

## Features

* Interactive command-line chatbot
* Text preprocessing using NLTK
* Stopword removal
* FAQ matching using TF-IDF
* Similarity calculation using Cosine Similarity
* Automatic response generation
* Exit command to stop the chatbot

---

## Technologies Used

* Python 3.x
* NLTK
* Scikit-learn

---

## Installation

### Step 1: Install Required Libraries

```bash
pip install nltk scikit-learn
```

### Step 2: Run the Program

```bash
python chatboat.py
```

---

## Project Structure

```
project/
│
├── chatboat.py
└── README.md
```

---

## FAQ Dataset

The chatbot contains the following predefined FAQs:

* What is your product?
* How can I use this chatbot?
* What are the features?
* How to contact support?
* Is this service free?

---

## Working Process

1. User enters a question.
2. The text is converted to lowercase.
3. Punctuation and stopwords are removed.
4. TF-IDF converts text into numerical vectors.
5. Cosine Similarity compares the user's question with stored FAQ questions.
6. The most similar FAQ is selected.
7. The corresponding answer is displayed.
8. If no match is found, the chatbot returns a default response.

---

## Sample Output

```
===================================
      FAQ Chatbot Started
Type 'exit' to stop
===================================

You: what is your product
Bot: Our product is an AI based chatbot system.

You: how to contact support
Bot: You can contact support through email or customer service.

You: exit
Bot: Goodbye!
```

---

## Advantages

* Easy to understand and implement
* Fast response time
* No external API required
* Suitable for small FAQ systems

---

## Limitations

* Works only with predefined questions
* Cannot learn new responses automatically
* Limited conversational capabilities

---

## Future Enhancements

* Add GUI using Tkinter
* Store FAQs in a database
* Integrate speech recognition
* Add multilingual support
* Connect with AI APIs for advanced responses

---

## Conclusion

The FAQ Chatbot demonstrates how Natural Language Processing techniques can be used to build a simple question-answering system. It provides quick responses by matching user queries with predefined FAQs and is suitable for educational and beginner-level chatbot projects.
