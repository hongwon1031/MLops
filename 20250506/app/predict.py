import joblib

model = joblib.load("model.pkl")
def predict_spam(message : str) -> str:
    pred = model.predict([message])[0]
    return "spam" if pred == 1 else "ham"