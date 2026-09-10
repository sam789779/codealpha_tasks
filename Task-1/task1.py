import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translation Tool", page_icon="🌐")
st.title("🌐 Language Translation Tool")

# Supported languages dictionary
LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Urdu": "ur",
    "Chinese (Simplified)": "zh-CN",
    "Arabic": "ar"
}

# UI Input Layout
col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("Source Language", list(LANGUAGES.keys()), index=0)
with col2:
    target_lang = st.selectbox("Target Language", list(LANGUAGES.keys()), index=1)

text_input = st.text_area("Enter text to translate:", height=150)

if st.button("Translate Text", type="primary"):
    if text_input.strip():
        try:
            translator = GoogleTranslator(
                source=LANGUAGES[src_lang], 
                target=LANGUAGES[target_lang]
            )
            translated_text = translator.translate(text_input)
            
            st.success("Translation Complete!")
            st.subheader("Translated Output:")
            st.text_area("Result:", value=translated_text, height=150)
        except Exception as e:
            st.error(f"Error during translation: {e}")
    else:
        st.warning("Please enter some text to translate.")