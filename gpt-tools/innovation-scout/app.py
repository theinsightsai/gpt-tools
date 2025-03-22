
import streamlit as st
import openai

st.set_page_config(page_title="Innovation Scout AI", layout="wide")

st.title("Innovation Scout AI – Discover Unmet Needs & Trends")

openai.api_key = st.secrets["OPENAI_API_KEY"]

user_input = st.text_area("Ask Innovation Scout AI about trends, market gaps, or opportunities:")

if st.button("Submit"):
    with st.spinner("Scanning industry trends..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Innovation Scout AI, an expert in identifying unmet market needs, trends, and innovation opportunities."},
                {"role": "user", "content": user_input}
            ]
        )
        st.markdown(response['choices'][0]['message']['content'])
