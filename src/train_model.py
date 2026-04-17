import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

def train_model(dataset_file):

    df = pd.read_csv(dataset_file)

    X = df[
        ["Close","Volume","sentiment","ma7","price_change","volatility"]
    ]

    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=200, random_state=42)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    score = r2_score(y_test, predictions)

    # --- Prediction for the latest day ---
    latest_features = X.iloc[-1:]
    predicted_price = model.predict(latest_features)[0]

    current_price = df["Close"].iloc[-1]

    expected_move = ((predicted_price - current_price) / current_price) * 100

    # --- Confidence from tree variance ---
    tree_preds = np.array([tree.predict(latest_features) for tree in model.estimators_])
    confidence = 1 - np.std(tree_preds) / predicted_price
    confidence = max(0, min(confidence, 1))

    return {
        "current_price": current_price,
        "predicted_price": predicted_price,
        "expected_move": expected_move,
        "confidence": confidence,
        "accuracy": score
    }