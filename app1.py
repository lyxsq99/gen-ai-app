import streamlit as st
import llm
# Create a text input box
text_input = st.text_input("Input your question")
# Create a submit button
if st.button("Submit"):
    user_prompt = text_input
    system_prompt = "Answer questions in funny tone with Emoji"
    result = llm.answer(system_prompt, user_prompt)
    st.markdown("## Response")
    st.write("Response:", result)