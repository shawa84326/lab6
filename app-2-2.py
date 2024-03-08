from tempfile import NamedTemporaryFile
import os
import streamlit as st
from llama_index.core import VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_index.readers.file import PDFReader
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Generate Lyrics",
    page_icon="🎵",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

if "messages" not in st.session_state.keys():  # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Here we go for your lrics!"}
    ]

uploaded_file = st.file_uploader("Upload a file")
generate_lyrics_button = st.button("Generate Lyrics")

if uploaded_file and generate_lyrics_button:
    bytes_data = uploaded_file.read()
    with NamedTemporaryFile(delete=False) as tmp:  # open a named temporary file
        tmp.write(bytes_data)  # write data from the uploaded file into it
        with st.spinner(
            text="Loading and processing the lyrics from the document – please wait."
        ):
            reader = PDFReader()
            docs = reader.load_data(tmp.name)
            llm = OpenAI(
                api_key=os.getenv("OPENAI_API_KEY"),
                base_url=os.getenv("OPENAI_API_BASE"),
                model="gpt-3.5-turbo",
                temperature=1.0,
                system_prompt="You are an expert on the content of the document, provide detailed answers to the questions. Use the document to support your answers.",
            )
            index = VectorStoreIndex.from_documents(docs)
    os.remove(tmp.name)  # remove temp file

    if "lyrics_engine" not in st.session_state.keys():  # Initialize the lyrics engine
        st.session_state.lyrics_engine = index.as_chat_engine(
            chat_mode="condense_question", verbose=False, llm=llm
        )

    # Predefined prompt for the assistant
    predefined_prompt = "Generate a long creative lyrics similar to the input pdf document."

    # Generate a new response
    with st.spinner("Thinking..."):
        response = st.session_state.lyrics_engine.stream_chat(predefined_prompt)
        st.write_stream(response.response_gen)
        message = {"role": "assistant", "content": response.response}
        st.session_state.messages.append(message)  # Add response to message history

# Display the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
