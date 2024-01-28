from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

st.set_page_config(page_title="QA Bot")
MODEL = "gpt-3.5-turbo-instruct"
load_dotenv()


def get_api_key(key: str) -> str:
    return os.getenv(key)


def get_openai_response(question: str):
    if question:
        llm = OpenAI(
            openai_api_key=get_api_key("OPENAI_API_KEY"),
            model=MODEL,
            temperature=0.5
        )
        response = llm(question)
        return response


user_input = st.text_input(label="Question", key="user_input")

llm_response = get_openai_response(user_input)

st.header("LangChain Bot")

submit = st.button("Ask")

if submit:
    st.subheader("Response:")
    st.write(llm_response)
