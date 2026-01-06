import streamlit as st
import requests

API_URL = "https://harassment-detection-api.onrender.com/analyze"

st.set_page_config(
    page_title="AI Harassment Detection – Admin",
    layout="centered"
)

st.title("🛡️ AI Harassment Detection – Admin Dashboard")
st.caption("Live analysis powered by cloud-deployed AI models")

text = st.text_area(
    "Enter text to analyze",
    placeholder="Type a message here...",
    height=120
)

analyze_btn = st.button("Analyze")

if analyze_btn:
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"text": text},
                    timeout=15
                )
                data = response.json()

                analysis = data["analysis"]
                decision = data["decision"]

                st.subheader("📊 Analysis")

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Harassment Probability", f"{analysis['harassment_prob']:.2f}")
                    st.metric("Sentiment Score", f"{analysis['sentiment']:.2f}")

                with col2:
                    st.metric("Severity", analysis["severity"])
                    st.metric("Threat", str(analysis["threat"]))

                if analysis["threat"]:
                    st.error(f"🚨 Threat Detected ({analysis['threat_confidence']})")

                st.subheader("🧠 Administrative Decision")
                if decision["decision"] == "ESCALATE":
                    st.error(decision["decision"] + " — " + decision["reason"])
                elif decision["decision"] == "TEMP_BLOCK":
                    st.warning(decision["decision"] + " — " + decision["reason"])
                elif decision["decision"] == "WARN":
                    st.warning(decision["decision"] + " — " + decision["reason"])
                else:
                    st.success(decision["decision"] + " — " + decision["reason"])

            except Exception as e:
                st.error(f"Error connecting to API: {e}")
