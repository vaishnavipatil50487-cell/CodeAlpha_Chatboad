import nltk
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK data
nltk.download('stopwords')

# FAQ Dataset
faqs = {
    "what is your product": "Our product is an AI based chatbot system.",
    "how can i use this chatbot": "You can type your questions and get instant answers.",
    "what are the features": "Features include NLP processing, FAQ matching and automatic replies.",
    "how to contact support": "You can contact support through email or customer service.",
    "is this service free": "Yes, basic services are free to use."
}

# Text preprocessing
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    return " ".join(words)

# Prepare FAQ questions
questions = list(faqs.keys())
processed_questions = [preprocess(q) for q in questions]

# Vectorization
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(processed_questions)

# Chatbot function
def chatbot(user_input):
    user_text = preprocess(user_input)

    user_vector = vectorizer.transform([user_text])

    similarity = cosine_similarity(user_vector, faq_vectors)

    best_match = similarity.argmax()
    score = similarity[0][best_match]

    if score < 0.2:
        return "Sorry, I could not understand your question."

    return faqs[questions[best_match]]

# Chat UI
print("===================================")
print("      FAQ Chatbot Started")
print("Type 'exit' to stop")
print("===================================")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = chatbot(user)
    print("Bot:", response)