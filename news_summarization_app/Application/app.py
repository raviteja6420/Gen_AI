import streamlit as st
from utils import fetch_news, analyze_sentiments, generate_comparative_analysis, generate_hindi_tts
import os
import tempfile

# Configure page
st.set_page_config(page_title="News Summarizer & Hindi TTS", page_icon="📰")

# Create temporary directory for audio files
temp_dir = tempfile.TemporaryDirectory()
AUDIO_DIR = os.path.join(temp_dir.name, "static")
os.makedirs(AUDIO_DIR, exist_ok=True)

# App UI
st.title("📰 News Summarization & Hindi TTS")
st.markdown("Get news summaries with sentiment analysis and Hindi audio conversion")

company_name = st.text_input("Enter Company Name", "Tesla")
process_btn = st.button("Analyze News")

def display_results(company, articles, comparative_data, audio_path):
    """Helper function to display analysis results"""
    st.header(f"📊 News Analysis for {company}")
    
    # Articles display
    for idx, art in enumerate(articles, 1):
        with st.expander(f"Article {idx}: {art.get('title', 'No Title')}"):
            st.write(f"**Summary:** {art.get('summary', 'No Summary')}")
            st.markdown(f"**Sentiment:** `{art.get('sentiment', 'Neutral')}`")
            st.write(f"**Topics:** {', '.join(art.get('topics', []))}")
            st.markdown(f"[Read Full Article]({art.get('link', '')})")
    
    # Sentiment metrics
    st.subheader("📈 Sentiment Distribution")
    st.json(comparative_data.get("Sentiment Distribution", {}))
    
    # Audio playback
    if audio_path and os.path.exists(audio_path):
        st.subheader("🎧 Hindi Summary Audio")
        st.audio(audio_path)
    else:
        st.warning("Could not generate audio summary")

if process_btn:
    if not company_name:
        st.error("Please enter a company name")
        st.stop()
    
    with st.spinner("🔍 Analyzing news articles..."):
        try:
            # Fetch and process news
            articles = fetch_news(company_name)
            if not articles:
                st.error("No articles found for this company")
                st.stop()
            
            # Analyze sentiments
            for art in articles:
                art["sentiment"] = analyze_sentiments(art["summary"])
            
            # Generate comparative analysis
            comparative_data = generate_comparative_analysis(articles)
            
            # Generate TTS
            summary_text = " ".join(
                [f"{art['title']} shows {art['sentiment']} sentiment." 
                 for art in articles[:3]]  # Limit to 3 articles for audio
            )
            tts_file = generate_hindi_tts(summary_text, AUDIO_DIR)
            
            # Display results
            display_results(company_name, articles, comparative_data, tts_file)
            
        except Exception as e:
            st.error(f"❌ Error processing request: {str(e)}")