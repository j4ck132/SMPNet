from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import pandas as pd

def handle_response(message) -> str:
    pickled_model = pickle.load(open('model.pkl', 'rb'))
    vectorizer = TfidfVectorizer()
    df = pd.read_csv('human_annotations_same.csv')
    X = df['text']
    X = vectorizer.fit_transform(X)
    vectorized_singular_text = vectorizer.transform([message])
    prediction = pickled_model.predict(vectorized_singular_text)
    if (prediction == [1.] and len(message) > 8):
        return("Hi, you seem to be lonely, would someone like to be their friend? You can go to talkwithstranger.com to talk to someone or call 988 for emotional help!")
    else:
        return("")