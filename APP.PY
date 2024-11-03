from dotenv import load_dotenv
load_dotenv() ## loading the environments
import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
## FUNCTION to load Gemini Pro model and get reponse
model =genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

## streamlit initialization
st.set_page_config(page_title = "Q&A Demo")
st.header("Gemini LLM Application")
input =st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

## When submit is clicekd
if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is ")
    st.write(response)