---
title: "News Summarization and Hindi TTS Application"
emoji: "📰"
colorFrom: "blue"
colorTo: "green"
sdk: streamlit
sdk_version: "1.24.1"
app_file: app.py
pinned: false
---


# News Summarization and Hindi TTS Application

## Overview
This project is a web-based application that extracts news articles related to a given company, performs sentiment analysis on the articles, conducts a comparative analysis of the sentiments, and generates a Hindi text-to-speech (TTS) output summarizing the findings. The application provides an intuitive user interface built with Streamlit and leverages a Flask API (embedded within the same file) for backend processing. It is designed to be easily deployable on Hugging Face Spaces.

## Features
- **News Extraction:**  
  Scrapes up to 10 unique news articles using the Google News RSS feed. Each article includes a title, summary, and a link for further reading.
  
- **Sentiment Analysis:**  
  Uses TextBlob to analyze the sentiment of each article's summary, categorizing them as Positive, Negative, or Neutral.
  
- **Comparative Analysis:**  
  Provides a breakdown of sentiment distribution across the articles and generates a basic comparative analysis (including dummy topic extraction and coverage differences).
  
- **Hindi Text-to-Speech (TTS):**  
  Translates a summary of the news report into Hindi using googletrans and then converts the translated text into audio using gTTS.
  
- **User Interface:**  
  The application uses Streamlit to provide a clean, interactive interface where users can input a company name and view the results directly.
  
- **Deployment Ready:**  
  The entire project is designed as a single entry point for seamless deployment on Hugging Face Spaces.

## Project Structure
