import streamlit as st
import openai
st.title("Translate")
user_input = st.text_input("Text to translate:")
api = st.secrets["openai"]
def translate(Language_to_translate):
    client = openai.OpenAI(api_key= api)
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
           
            {"role": "user", "content": f"Translate the following text to {Language_to_translate}: {user_input}"}
        ]
    )
    
    translated_text = response.choices[0].message.content
    return translated_text
    

# Creating a button
options = ["Spanish", "German", "French", "Farsi"]

# Create a dropdown
selected_option = "Spanish"
selected_option = st.selectbox("Choose an option:", options)
if st.button("Click Me"):

    st.write("Translated text:", translate(selected_option))
    
