import streamlit as st
from googletrans import Translator

# 1. Setup the Website Title and Icon
st.set_page_config(page_title="Anuvaad Pro", page_icon="🌐")

# 2. Design the Header
st.title("🌐 Anuvaad Pro")
st.markdown("### Translate documents and text into Indian Languages")

# 3. Create a sidebar for Language Selection
language_option = st.sidebar.selectbox(
    "Select Target Language",
    ("Marathi", "Telugu", "Hindi")
)

# Map names to language codes
lang_codes = {"Marathi": "mr", "Telugu": "te", "Hindi": "hi"}

# 4. Main Input Area
user_text = st.text_area("Enter text to translate:", placeholder="Type something here...")

if st.button("Translate Now"):
    if user_text:
        translator = Translator()
        # Perform translation
        translation = translator.translate(user_text, dest=lang_codes[language_option])
        
        # 5. Show the Result
        st.success(f"**Translated to {language_option}:**")
        st.write(translation.text)
    else:
        st.warning("Please enter some text first!")

# 6. Future Feature Placeholder
st.divider()
st.info("Coming Soon: Upload a 40-page PDF to translate the whole document!")