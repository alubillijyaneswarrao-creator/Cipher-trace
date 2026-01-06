📌 Project Title

🔐 Cipher-Trace — AI-Powered Online Harassment Detection Platform                                                                          👤 Author

                                                                                                                                            Jyanesh Naidu

GitHub: https://github.com/alubillijyaneswarrao-creator                                                                                     ⭐ If you find this project useful, give it a star!

LinkedIn: https://linkedin.com/in/jyaneshnaidu


DESCRIPTION:
Online platforms face increasing challenges in detecting harassment, abusive language, and threats in real time. Manual moderation is slow, inconsistent, and not scalable.

This project presents an AI-powered harassment detection system that analyzes user-generated text, evaluates risk using multiple AI models, and provides an administrative decision through a live dashboard.

The system is designed to minimize false positives while ensuring high safety, similar to real-world moderation systems used by social media platforms.



📖 Project Overview
Cipher-Trace is an AI-powered content moderation platform designed to detect online harassment, abusive language, and explicit threats in real time.
The system combines machine learning, sentiment analysis, and rule-based threat detection with a sentiment-aware decision engine to reduce false positives and enable fair moderation.

The project is fully deployed, cloud-based, and includes an administrative dashboard for real-time monitoring.

🚀 Live Demo

Backend API (FastAPI)
👉 https://harassment-detection-api.onrender.com

API Documentation (Swagger UI)
👉 https://harassment-detection-api.onrender.com/docs

Admin Dashboard (Streamlit)
👉 https://cipher-trace-harassment.streamlit.app/
🎯 Objectives

Detect abusive and harassing content automatically

Analyze sentiment, severity, and threat level

Reduce false positives using sentiment-aware logic

Provide real-time moderation decisions

Offer an admin dashboard for visualization and monitoring

monitoring

✨ Key Features

🤖 AI-Based Harassment Detection
Predicts harassment probability using a supervised ML classifier.

😊 Sentiment-Aware Severity Logic
Uses NLP sentiment analysis to prevent false positives for positive or neutral content.

⚠️ Threat Detection Module
Detects explicit violent threats using rule-based NLP logic.

🧠 Administrative Decision Engine
Generates actions such as:

ALLOW

WARN

TEMP_BLOCK

ESCALATE

📊 Admin Dashboard
Live visualization of analysis results and moderation decisions.

☁️ Cloud Deployed
FastAPI backend deployed on Render with real-time inference.

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


⚙️ Installation & Local Setup
git clone https://github.com/alubillijyaneswarrao-creator/Cipher-trace.git
cd Cipher-trace
pip install -r requirements.txt
uvicorn app:app --reload
Open:http://localhost:8000/docs
