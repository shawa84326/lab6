from tempfile import NamedTemporaryFile
import os
import streamlit as st

from llama_index.core import VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_index.readers.file import PDFReader
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Taylor Swift Lyrics Generator",
    page_icon="🎤",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me anything about Taylor Swift's lyrics or request new lyrics!"}
    ]

uploaded_file = st.file_uploader("Upload a PDF file containing Taylor Swift lyrics")
if uploaded_file:
    bytes_data = uploaded_file.read()
    with NamedTemporaryFile(delete=False) as tmp:
        tmp.write(bytes_data)
        with st.spinner(
            text="Loading and indexing Taylor Swift lyrics. This may take a minute or two."
        ):
            reader = PDFReader()
            docs = reader.load_data(tmp.name)
            llm = OpenAI(
                api_key="YOUR_OPENAI_API_KEY",
                model="gpt-3.5-turbo",
                temperature=0.0,
                system_prompt="You are an expert on Taylor Swift lyrics. Provide detailed answers to questions or ask me to generate new lyrics in her style.",
            )
            index = VectorStoreIndex.from_documents(docs)
    os.remove(tmp.name)

    if "chat_engine" not in st.session_state.keys():
        st.session_state.chat_engine = index.as_chat_engine(
            chat_mode="condense_question", verbose=False, llm=llm
        )

if prompt := st.chat_input("Your question or request related to Taylor Swift lyrics"):
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.stream_chat(prompt)
            st.write_stream(response.response_gen)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message)
