import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
data = pd.read_csv("data/uci-ml-phishing-dataset.csv")

# Display column names (for verification)
print("\nCOLUMNS:\n", list(data.columns))

# Separate features and target
X = data.drop("Result", axis=1)
y = data["Result"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", accuracy)

# Save model
with open("model/phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully.")
