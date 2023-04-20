import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
NAME=""
TARGET_LABEL="opening_name"
# Load data from CSV file
data = pd.read_csv("data.csv")

# Split data into features and labels
X = data.drop("label", axis=1)
y = data["label"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define XGBoost model parameters
params = {
    "objective": "binary:logistic",
    "max_depth": 200,
    "learning_rate": 0.1,
    "subsample": 0.8,
    "colsample_bytree": 0.8,
    "seed": 42
}

# Convert data to XGBoost DMatrix format
train_data = xgb.DMatrix(X_train, label=y_train)
test_data = xgb.DMatrix(X_test, label=y_test)

# Train XGBoost model
model = xgb.train(params, train_data, num_boost_round=100)

# Make predictions on test set
y_pred = model.predict(test_data)
y_pred_binary = [round(value) for value in y_pred]

# Evaluate model accuracy
accuracy = accuracy_score(y_test, y_pred_binary)
print("Accuracy:", accuracy)