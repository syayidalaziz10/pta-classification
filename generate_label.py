import nltk
import re
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import joblib


nltk.download("punkt")
nltk.download("stopwords")


def get_label(news_text):
    lower = news_text.lower()
    lower = news_text.split()

    puncuation = [re.sub(r'[.,()&=%:-]', '', token)
                  for token in lower]
    puncuation = [re.sub(r'\d+', '', token)
                  for token in lower]
    stop_words = set(stopwords.words("indonesian"))
    stopword = [
        puncuation for puncuation in puncuation if puncuation.lower() not in stop_words]

    stopword = " ".join(stopword)

    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    stemm = stemmer.stem(stopword)

    vectorizer = joblib.load('model/tfidf_vectorizer')
    model = joblib.load('model/knn_model')

    x_new = vectorizer.transform([stemm]).toarray()
    prediction = model.predict(x_new)
    result = prediction[0]

    return result
