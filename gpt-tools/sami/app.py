
import streamlit as st
import openai

st.set_page_config(page_title="SAMI AI", layout="wide")

st.title("SAMI AI – Advanced Analytical Tool")

openai.api_key = st.secrets["OPENAI_API_KEY"]

user_input = st.text_area("Ask SAMI AI anything about data, Excel, or analytics:")

if st.button("Submit"):
    with st.spinner("Analyzing..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are SAMI AI, an expert in analyzing Excel data and uncovering insights."},
                {"role": "user", "content": user_input}
            ]
        )
        st.markdown(response['choices'][0]['message']['content'])
