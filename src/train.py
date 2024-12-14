from data_loader import load_data_root
from bow_model import vectorize
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

data = load_data_root("data.csv", "processed")

X = vectorize(data["Message"])
y = data["Category"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

path = "models/" 

joblib.dump(model, path + "Spam_DetectorV0.pkl")
joblib.dump(X_test, path + "X_test.pkl")
joblib.dump(y_test, path + "y_test.pkl")


