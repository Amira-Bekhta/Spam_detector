
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer

english_stopwords = stopwords.words('english')
stemmer = SnowballStemmer('english')

# tokenize a text and stem it
def tokenize(text):
  return [stemmer.stem(word) for word in word_tokenize(text)]

vectorizer = CountVectorizer(lowercase=True, tokenizer=tokenize, stop_words=english_stopwords, max_features=1000)

# fit and transform a text to a count vectorizer
def vectorize(text):
    vectorizer.fit(text)
    return vectorizer.transform(text)












