# api.py
from flask import Flask, request, jsonify
from utils import fetch_news, analyze_sentiments, generate_comparative_analysis, generate_hindi_tts

app = Flask(__name__)

@app.route("/news", methods=["GET"])
def get_news():
    company = request.args.get("company", "")
    if not company:
        return jsonify({"error": "Company name is required"}), 400

    # Fetch news articles using our utility function
    articles = fetch_news(company)
    if not articles:
        return jsonify({"error": "No articles found"}), 404

    # Analyze sentiment for each article and add dummy topic extraction
    for article in articles:
        article["sentiment"] = analyze_sentiments(article["summary"])

    # Generate comparative analysis across the articles
    comparative_data = generate_comparative_analysis(articles)

    # Generate a summary text to convert to Hindi speech
    summary_text = " ".join([f"{art['title']} shows a {art['sentiment']} sentiment." for art in articles])
    tts_file = generate_hindi_tts(summary_text)

    response_data = {
        "Company": company,
        "Articles": articles,
        "Comparative Sentiment Score": comparative_data,
        "Final Sentiment Analysis": f"{company} news coverage indicates a predominant sentiment based on analyzed articles.",
        "Audio": tts_file
    }
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
