from data_loader import load_data_root, save_data_root
from bow_model import vectorize
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
import pickle

data = load_data_root("data.csv", "processed")

X = data["Message"]
y = data["Category"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

save_data_root(X_test, "X_test.csv")
save_data_root(y_test, "y_test.csv")

X_train = vectorize(X_train)

model = LogisticRegression()
model.fit(X_train, y_train)

path = "models/Spam_DetectorV0.pkl" 

x = model.predict(vectorize(X_test))

print(x)

with open(path, 'wb') as file:
    pickle.dump(model, file)

