# app.py
import streamlit as st
import requests
import os

st.title("News Summarization and Hindi TTS Application")

company_name = st.text_input("Enter Company Name", "Tesla")

if st.button("Fetch News"):
    if company_name:
        try:
            # Ensure the Flask backend is running on port 5000
            response = requests.get(f"http://127.0.0.1:5000/news?company={company_name}")
            response.raise_for_status()  # Check for HTTP errors
            data = response.json()

            st.header(f"News Sentiment Report for {data['Company']}")
            for art in data.get("Articles", []):
                st.subheader(art.get("title", "No Title"))
                st.write(f"**Summary:** {art.get('summary', 'No Summary')}")
                st.write(f"**Sentiment:** {art.get('sentiment', 'Neutral')}")
                st.write(f"**Topics:** {', '.join(art.get('topics', []))}")
                st.markdown(f"[Read More]({art.get('link', '')})")
                st.write("---")

            st.subheader("Comparative Sentiment Score")
            st.json(data.get("Comparative Sentiment Score", {}))

            st.subheader("Final Sentiment Analysis")
            st.write(data.get("Final Sentiment Analysis", ""))

            # Display the TTS audio if available
            audio_file = data.get("Audio", "")
            if audio_file and os.path.exists(audio_file):
                st.audio(audio_file)
            else:
                st.error("Audio file not available. Check backend logs for errors.")
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching news data: {e}")
    else:
        st.error("Please enter a company name")
