import streamlit as st
from hugchat.login import Login
from hugchat import hugchat


st.logo(
    "https://cdn-icons-png.flaticon.com/512/9029/9029906.png",
    size="large",
    icon_image="https://cdn-icons-png.flaticon.com/512/1256/1256449.png",
)


st.set_page_config(page_title="Chat", layout="wide")

st.title("Feel free to ask any question that BearCare hasn't answered already!")


@st.cache_resource
def connect_to_hugging_face():
    hf_email = st.secrets['email']
    hf_pass = st.secrets['password']

    # connect to hugging face
    sign = Login(hf_email, hf_pass)
    cookies = sign.login()

    return cookies

def generate_response(prompt):
    cookies = connect_to_hugging_face()
    # Create ChatBot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt)

# user message
prompt = st.chat_input("Enter a Prompt")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt)
            st.write(response)