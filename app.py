from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "Sentiment Analysis Service",
        "status": "running",
        "endpoints": {
            "GET /": "Service info",
            "POST /predict": "Predict sentiment for text"
        }
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)
    if not data or "text" not in data:
        return jsonify({"error": "Provide JSON with a 'text' field."}), 400

    text = data["text"]

    positive_words = ["love", "great", "excellent", "good", "amazing",
                      "fantastic", "wonderful", "best", "happy", "enjoy"]
    negative_words = ["hate", "terrible", "bad", "awful", "worst",
                      "frustrating", "difficult", "horrible", "poor", "disappointing"]

    text_lower = text.lower()
    pos_score = sum(1 for w in positive_words if w in text_lower)
    neg_score = sum(1 for w in negative_words if w in text_lower)

    if pos_score > neg_score:
        sentiment = "positive"
        score = round(pos_score / (pos_score + neg_score), 2)
    elif neg_score > pos_score:
        sentiment = "negative"
        score = round(neg_score / (pos_score + neg_score), 2)
    else:
        sentiment = "neutral"
        score = 0.5

    return jsonify({
        "text": text,
        "sentiment": sentiment,
        "score": score,
        "status": "success"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)





















