import streamlit as st
import random
import time

st.caption("คุยไรก็ได้แต่ไม่ใช่ของแท้")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "คนว่างมาคุยกันน! 👇"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("ไงเพื่อน!!"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = random.choice(
            [
                "หวัดดีเพื่อน สบายดีไหม",
                "ไม่เป้นไรเพื่อน อยากให้ช่วยอะไรเพิ่มไหม?",
                "มีอะไรให้ช่วยบอกได้เลยนะ.",
                "หวัดดี วันนี้มีอะไรให้ช่วยมั้ย?",
                "ยินดีเพื่อน สอบถามอะไรได้เลยเพื่อน"
            ]
        )
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
