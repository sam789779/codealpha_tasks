import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon', quiet=True)
st.set_page_config(page_title="Sentiment Analyzer", page_icon="📊")
st.title("📊 Text Sentiment Analysis Tool")
sia = SentimentIntensityAnalyzer()
user_text = st.text_area("Enter text to analyze sentiment:", height=150)
if st.button("Analyze Sentiment", type="primary"):
    if user_text.strip():
        scores = sia.polarity_scores(user_text)
        compound = scores['compound']

        st.subheader("Results:")
        if compound >= 0.05:
            st.success(f"Positive Sentiment 😊 (Score: {compound:.2f})")
        elif compound <= -0.05:
            st.error(f"Negative Sentiment 😞 (Score: {compound:.2f})")
        else:
            st.info(f"Neutral Sentiment 😐 (Score: {compound:.2f})")

        st.json(scores)
    else:
        st.warning("Please enter text for analysis.")