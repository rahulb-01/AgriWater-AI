import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

np.random.seed(42)

moisture = np.random.randint(10, 90, 200)
temperature = np.random.randint(20, 45, 200)
humidity = np.random.randint(30, 90, 200)

irrigation = []

for m in moisture:
    if m < 30:
        irrigation.append(1)
    else:
        irrigation.append(0)

data = pd.DataFrame({
    "moisture": moisture,
    "temperature": temperature,
    "humidity": humidity,
    "irrigation": irrigation
})

X = data[["moisture", "temperature", "humidity"]]
y = data["irrigation"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

joblib.dump(model, "irrigation_model.pkl")

print("Model trained and saved successfully")
