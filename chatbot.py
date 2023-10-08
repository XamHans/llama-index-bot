import os

import openai
import streamlit as st
from dotenv import load_dotenv
from llama_index import SimpleDirectoryReader, VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI


load_dotenv()

# Constants
TEMPERATURE = 0
PATH_TO_DOCS = "./resources"
MODEL = "gpt-3.5-turbo"

# Global variables
chat_engine = None
llm_predictor = None


@st.cache_resource(show_spinner=False)
def construct_index():
    documents = SimpleDirectoryReader(
        input_dir=PATH_TO_DOCS, recursive=True
    ).load_data()
    service_context = ServiceContext.from_defaults(llm=OpenAI(
        model=MODEL, temperature=TEMPERATURE))
    index = VectorStoreIndex.from_documents(
        documents, service_context=service_context)
    return index


def handle_user_input():
    global chat_engine
    # Prompt for user input and save to chat history
    if prompt := st.chat_input("Your question"):
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display the prior chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        # If last message is not from assistant, generate a new response
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Searching..."):
                    response = chat_engine.chat(prompt)
                    st.write(response.response)
                    message = {"role": "assistant",
                               "content": response.response}
                    # Add response to message history
                    st.session_state.messages.append(message)


def init_openai():
    openai.api_key = os.getenv("OPENAI_API_KEY")


def build_ui():
    global chat_engine
    st.set_page_config(
        page_title="Do you need help with your onboarding? Ask me!",
        page_icon=":books:",
    )

    # Initialize the chat messages history
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hi there! I'm your personal cloud assistant. How can I help you?",
            }
        ]


def init_chat_engine():
    global chat_engine
    index = construct_index()
    chat_engine = index.as_chat_engine(chat_mode="context")


def main():
    init_openai()
    init_chat_engine()
    build_ui()
    handle_user_input()


if __name__ == "__main__":
    main()
