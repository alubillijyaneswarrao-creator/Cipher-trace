📌 Project Title
AI-Powered Online Harassment Detection System

📖 Project Overview

Online platforms face increasing challenges in detecting harassment, abusive language, and threats in real time. Manual moderation is slow, inconsistent, and not scalable.

This project presents an AI-powered harassment detection system that analyzes user-generated text, evaluates risk using multiple AI models, and provides an administrative decision through a live dashboard.

The system is designed to minimize false positives while ensuring high safety, similar to real-world moderation systems used by social media platforms.


🎯 Objectives

Detect abusive and harassing content automatically

Analyze sentiment, severity, and threat level

Reduce false positives using sentiment-aware logic

Provide real-time moderation decisions

Offer an admin dashboard for visualization and monitoring

monitoring

🧠 Key Features

🔍 Harassment Probability Detection (ML classifier)

😊 Sentiment Analysis (NLTK VADER)

🚨 Threat Detection Module

🧠 Rule-Based Administrative Decision Engine

⚡ FastAPI REST API

📊 Admin Dashboard using Streamlit

☁️ Cloud Deployment (Render + Streamlit Cloud)

⚙️ Technology Stack

| Layer                | Technology              |
| -------------------- | ----------------------- |
| Programming Language | Python                  |
| Backend Framework    | FastAPI                 |
| ML Models            | Scikit-learn            |
| NLP                  | NLTK (VADER)            |
| API Server           | Uvicorn                 |
| Dashboard            | Streamlit               |
| Deployment           | Render, Streamlit Cloud |
| Version Control      | GitHub                  |


🧪 Decision Logic (Core Innovation)

The system uses multi-factor decision making:

Harassment probability (ML output)

Sentiment polarity

Threat detection

Severity classification

Example Policy:

Positive sentiment override → avoids false positives

Threat detected → immediate escalation

Medium severity → warning

Low severity → allow content

This mirrors industry-grade moderation pipelines.

🧠 Learning Outcomes

Built an end-to-end AI system from scratch

Integrated ML models with REST APIs

Designed policy-based decision systems

Deployed scalable cloud applications

Reduced ML false positives using sentiment-aware logic

🏆 Use Cases

Social media moderation

Online community platforms

Educational discussion forums

Comment filtering systems

📌 Future Enhancements

Transformer-based NLP models (BERT)

Multilingual harassment detection

Image & video moderation

User behavior analytics
