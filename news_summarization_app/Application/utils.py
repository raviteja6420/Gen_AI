import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from translate import Translator
from gtts import gTTS
import os
import uuid
import nltk

# Download NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def fetch_news(company):
    """Fetch news articles from Google News RSS feed"""
    url = f"https://news.google.com/rss/search?q={company}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    articles = []
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, "xml")
        for item in soup.find_all("item")[:10]:  # Limit to 10 articles
            title = item.title.text.strip() if item.title else "No Title"
            summary = item.description.text.strip() if item.description else ""
            link = item.link.text.strip() if item.link else ""
            
            articles.append({
                "title": title,
                "summary": summary,
                "link": link
            })
            
    except Exception as e:
        print(f"News fetch error: {e}")
    
    return articles

def analyze_sentiments(text):
    """Analyze text sentiment using TextBlob"""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0.2:
        return "Positive"
    elif polarity < -0.2:
        return "Negative"
    return "Neutral"

def generate_comparative_analysis(articles):
    """Generate sentiment distribution and topic analysis"""
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    
    for art in articles:
        sentiment = art.get("sentiment", "Neutral")
        sentiment_counts[sentiment] += 1
        
        # Extract first 3 unique keywords from summary
        words = [w.lower() for w in art["summary"].split() if len(w) > 3]
        art["topics"] = list(dict.fromkeys(words))[:3]
    
    return {"Sentiment Distribution": sentiment_counts}

def generate_hindi_tts(text, output_dir):
    """Convert text to Hindi speech using gTTS"""
    try:
        # Translate to Hindi
        translator = Translator(from_lang='en', to_lang='hi')
        translation = translator.translate(text)
        hindi_text = translation
        
        # Generate audio
        tts = gTTS(hindi_text, lang='hi')
        filename = os.path.join(output_dir, f"audio_{uuid.uuid4().hex}.mp3")
        tts.save(filename)
        return filename
        
    except Exception as e:
        print(f"TTS Error: {e}")
        return None