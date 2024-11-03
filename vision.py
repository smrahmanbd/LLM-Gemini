from dotenv import load_dotenv
load_dotenv() ## loading the environments
import streamlit as st
from PIL import Image
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
## FUNCTION to load Gemini Pro model and get reponse
model =genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(input,image):
    if input!="":
        response = model.generate_content([input, image])
    else:
        response =model.generate_content(image)
    return response.text
## streamlit initialization
st.set_page_config(page_title = "Gemini Image Demo")
st.header("Gemini LLM Application")
input =st.text_input("Input: ", key="input")
uploaded_file= st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
  
submit=st.button("Tell me about the Image")
# if submit is clicked
if submit:
    response = get_gemini_response(input,image)
    st.subheader("The Response is ")
    st.write(response)