import streamlit as st
import google.generativeai as genai
import base64
from langchain_core.messages import HumanMessage, SystemMessage

# def ai(txt):
    
#     for m in genai.list_models():
#         if 'generateContent' in m.supported_generation_methods:
#             print(m.name)
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content("from now your name is gamkers and your a ethical hacker and cloud data engineer , your real name is akash m and reply to this in short: "+txt)
#     return response.text



def ai(text):
    # Convert text to bytes
    bytes_text = text.encode('utf-8')
    
    # Encode bytes to Base64
    base64_text = base64.b64encode(bytes_text)
    
    encoded_text = base64_text.decode('utf-8')
    model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True, google_api_key="AIzaSyC7hJmlRUBDT6HeE1RPT7ovY1fBjgxs1jM")
    data = model(
    [
        SystemMessage(content="your task is to 1st decrypt the given base64 value and 2nd you need to create a code for the question and 3rd give a proper refrence too. Exclude how to decrypt from the out put  "),
        HumanMessage(content= encoded_text),
    ]
    )
    
    return data.content


st.title("Gamkers Ai Assistant")

command = st.chat_input("how can I help you?")

if "message" not in st.session_state:
    st.session_state.message = []

for chat in st.session_state.message:
    with st.chat_message(chat["role"]):
        st.write(chat["message"])


if command:
    with st.chat_message("USER"):
        st.write(command)
        st.session_state.message.append({"role":"USER","message":command})
    if "hello" in command:
        with st.chat_message("BOT"):
            st.write("Hi How are you?")
            st.session_state.message.append({"role":"BOT","message":"Hi How are you?"})
    elif "who" in command:
        with st.chat_message("BOT"):
            st.write("Im gamkers AI Assistant")
            st.session_state.message.append({"role":"BOT","message":"Im gamkers AI Assistant"})
    else:
        with st.chat_message("BOT"):
            data = ai(command)
            st.write(data)
            st.session_state.message.append({"role":"BOT","message":data})




print(st.session_state.message)
