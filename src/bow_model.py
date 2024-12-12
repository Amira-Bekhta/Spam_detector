
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import sklearn
from sklearn.feature_extraction.text import CountVectorizer

english_stopwords = stopwords.words('english')
stemmer = SnowballStemmer('english')

def tokenize(text):
  return [stemmer.stem(word) for word in word_tokenize(text)]

vectorizer = CountVectorizer(lowercase=True, tokenizer=tokenize, stop_words=english_stopwords, max_features=1000)

def vectorize(df, column):
    vectorizer.fit(df[column])
    vectorizer.transform(df[column])





