import streamlit as st
import google.generativeai as genai


# Configure Google Gemini API Key
GEMINI_API_KEY = "AIzaSyAjilXep3mwyuo0vmMy3EM0J4bzsUxsa-E"
genai.configure(api_key=GEMINI_API_KEY)

def review_code(code):
    """Send code to Gemini API for review."""
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
    Analyze the following Python code for bugs, optimizations, and best practices.
    Provide a review with necessary improvements:

    ```python
    {code}
    ```
    """
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="AI Code Reviewer", layout="wide")
st.title("🔍 AI Code Reviewer")
st.markdown("Upload or paste your Python code to get an AI-powered review.")

# Text area for code input
code = st.text_area("Paste your Python code here:", height=250)

if st.button("Review Code"):
    if code.strip():
        with st.spinner("Analyzing your code..."):
            review = review_code(code)
            st.subheader("AI Review Report")
            st.markdown(review)
    else:
        st.warning("Please enter some Python code for review.")
