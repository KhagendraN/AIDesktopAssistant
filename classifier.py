from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import pickle
import json

# training data
def load_training_data():
    try:
        with open('training_data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = [
            ("Hi there!", "friendly"),
            ("Can you tell me a joke?", "friendly"),
            ("What is the capital of France?", "normal"),
            ("Explain the theory of relativity in detail.", "long"),
        ]
    return data


#load data
data = load_training_data()
# Prepare data
X_train, y_train = zip(*data)

# Vectorize the text data
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)

# Train a classifier
classifier = SVC(kernel='linear')
classifier.fit(X_train_tfidf, y_train)

# Save the trained model and vectorizer
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

with open('classifier.pkl', 'wb') as f:
    pickle.dump(classifier, f)

def classify_query(query):
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    
    with open('classifier.pkl', 'rb') as f:
        classifier = pickle.load(f)
    
    query_tfidf = vectorizer.transform([query])
    return classifier.predict(query_tfidf)[0]
