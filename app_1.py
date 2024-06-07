import streamlit as st
from langchain.llms import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()


def get_text(question):
    llm  = HuggingFaceEndpoint(repo_id ="mistralai/Mistral-7B-Instruct-v0.2")
    answer = llm.invoke(question)
    return answer


# UI code start here 

st.set_page_config(page_title="Marketing Tool",
                    page_icon='✅',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Hey, please put your query here :")

input = st.text_area('Enter Text:' , height=270)


task_type = st.selectbox('Please select the option to be performed?', 
                            ('Write a sales copy', 'Create a tweet', 'Write a product description'),key=1)


age_option = st.selectbox ('Please select your age here?' , 
                            ('Kid', 'Adult', 'senior Citizen'),key=2)

word_count = st.slider('Select your wordcount here ?' , 1 , 200 , 20)


submit = st.button("Generate")   

if submit:
    if not input.strip():
        st.write("Please enter a question. ")

    else:
        # Combine all user inputs into a single input
        # user_input = f"Task: {task_type}\nAge: {age_option}\nWord Count: {word_count}\nText: {user_input_text}"
        user_input = f"you are {age_option} and do task {task_type} within wordcount {word_count} of text {input}"
        response = get_text(user_input)
        st.subheader("Answer:")
        st.write(response)


        