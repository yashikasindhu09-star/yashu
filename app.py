import streamlit as st
from openai import OpenAI

# 🔑 Replace with your own OpenAI API key
client = OpenAI(api_key="sk-...mNgA")

# App title
st.set_page_config(page_title="YashBot 💬", page_icon="🤖", layout="centered")
st.title("💬 YashBot — Your Personal Chat Assistant")
st.caption("Powered by OpenAI GPT-4")

# Session state to keep chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are YashBot, a helpful and friendly assistant created by Yashika Sindhu."}
    ]

# Display chat messages
for msg in st.session_state["messages"][1:]:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)

    # Add user message to history
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Generate assistant response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state["messages"]
    )

    reply = response.choices[0].message.content

    # Display bot message
    st.chat_message("assistant").markdown(reply)

    # Add assistant reply to history
    st.session_state["messages"].append({"role": "assistant", "content": reply})
