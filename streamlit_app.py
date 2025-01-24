import streamlit as st

import tempfile
api_secret_key = st.secrets["secret_key"]  
from openai import OpenAI  # Ensure the OpenAI library is installed
st.title("Emanuel comagnion Friend Chat")
# Initialise openIA cleant
client = OpenAI(
    api_key=api_secret_key,  # Replace with your API key
    base_url="https://api.deepseek.com"
    )



# Initialize session state to store messages
if "messages"  not in  st.session_state:
    st.session_state.messages = [
        {"role":"assistant","content":"You are helpfull assistant  you act as a concierge"}
    ]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user imput
user_input = st.chat_input("Ask a Question")
# Ge the user imput( messsage) and  add to the user history
if user_input:
    st.session_state.messages.append({"role":"user","content":user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
# Generate the  response from openai
with st.chat_message("assistant"):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages = st.session_state.messages,
        stream = False
    )

 # Diaplay the chat to the  UI
    assistant_message = response.choices[0].message.content
    st.markdown(assistant_message)
    # Add assistant message to chat history
    st.session_state.messages.append({"role":"assistant","content":assistant_message})
    