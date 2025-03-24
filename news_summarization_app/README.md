---
title: "News Summarization and Hindi TTS Application"
emoji: "📰"
colorFrom: "blue"
colorTo: "green"
sdk: streamlit
sdk_version: "1.43.2"
app_file: app.py
pinned: false
---

# News Summarization and Hindi TTS Application

## Overview
This project is a web-based application that extracts news articles related to a specified company, performs sentiment analysis on these articles, provides a comparative analysis of the sentiments, and generates a Hindi text-to-speech (TTS) summary of the findings. The application uses a Flask API (embedded within the same file) and a Streamlit frontend, and is designed to be deployed on Hugging Face Spaces.

## Features
- **News Extraction:**  
  Scrapes up to 10 news articles using the Google News RSS feed with proper headers to mimic a browser request.
  
- **Sentiment Analysis:**  
  Uses TextBlob to classify each article's sentiment as Positive, Negative, or Neutral.
  
- **Comparative Analysis:**  
  Aggregates sentiment data across articles and performs a basic comparative analysis, including dummy topic extraction.
  
- **Hindi TTS:**  
  Translates a generated summary into Hindi using the `google_trans_new` library and converts the text into speech using gTTS.
  
- **Deployment Ready:**  
  The project is structured as a single entry-point application (`app.py`) for easy deployment on Hugging Face Spaces.

## Project Structure




## Setup and Installation

### Prerequisites
- Python 3.10 or later
- Git (if you plan to clone the repository)
- An active internet connection

### Local Setup

1. **Clone the Repository:**
   ```bash
   git clone <repository_link>
   cd news_summarization_app
