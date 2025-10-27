import streamlit as st
import llm
import json

# request LLM to generate questions in JSON format
def generate_questions(topic, num_questions):
    system_prompt = "You are proficient quiz generator."
    with open("prompt.txt", "r") as f:  # read user_prompt from prompt.txt
        user_prompt = f.read()
    # replace the placeholders with the actual values
    user_prompt = user_prompt.replace("{topic}", topic)
    user_prompt = user_prompt.replace("{num_questions}", str(num_questions))
    # Invoke LLM to generate the output based on user and system prompts
    result = llm.answer(system_prompt, user_prompt)
    return json.loads(result)

# handle the button click event
def generate_question_handler():
    # get the topic and num_questions from st.session_state
    topic = st.session_state["topic"]
    num_questions = st.session_state["num_questions"]
    # generate questions
    questions = generate_questions(topic, num_questions)
    # show questions generated
    st.session_state["questions"] = questions

with st.sidebar:  # the input widgets are placed in the sidebar
    topic = st.text_input("Enter the topic", key="topic")
    num_questions = st.number_input("Enter the number of questions", min_value=1, key="num_questions")
    st.button("Generate Questions", on_click=generate_question_handler)

if "questions" in st.session_state:
    st.write("Generated Questions:")
    st.json(st.session_state["questions"])