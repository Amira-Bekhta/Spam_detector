from data_loader import load_data
from bow_model import vectorize
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd

data = pd.read_csv("data/processed/data.csv")

X = vectorize(data, "Message")
y = data["Category"]
classes = ["ham", "spam"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

x = y_test[0]

