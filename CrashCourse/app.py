from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

def get_openai_response(question:str):
    pass