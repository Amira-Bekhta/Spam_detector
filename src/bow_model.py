
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer

english_stopwords = stopwords.words('english')
stemmer = SnowballStemmer('english')

def tokenize(text):
  return [stemmer.stem(word) for word in word_tokenize(text)]

vectorizer = CountVectorizer(lowercase=True, tokenizer=tokenize, stop_words=english_stopwords, max_features=1000)

def vectorize(text):
    vectorizer.fit(text)
    return vectorizer.transform(text)


def transform(txt):
   return vectorizer.transform(txt)










