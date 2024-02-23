# AI Assistant Readme

This repository contains an AI Assistant designed to assist users with various tasks, such as extracting information from text, providing feedback on resumes and cover letters, and generating Taylor Swift-style song lyrics.

## Features and Use Cases


### AI Taylor Swift Song Generator

#### Generate Taylor Swift-Style Song Lyrics
- Users can input an example of Taylor Swift song lyrics, and the AI Assistant will generate new lyrics in a similar style.
- This feature is for entertainment purposes and showcases the capabilities of natural language generation.

## Getting Started

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/shawa84326/lab6.git
    ```

2. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

     ```bash
    source venv/bin/activate
    ```
Example of activiting vortual environment in local machine 

ankitshaw --- username on local pc
lab6------ folder name in which file is created

source /Users/ankitshaw/lab6/venv/bin/activate  (For Macos local machine, activating virtual environment)

/Users/ankitshaw/lab6/venv/Scripts/activate (For windows)

pip install -r requirements.txt


cp .env.sample .env


Change the .env file to match your environment


streamlit run app-2.py
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    streamlit run app-2.py
    ```

5. Access the AI Assistant through a web browser at `http://127.0.0.1:5000/`.





## Acknowledgments

- This AI Assistant is built using [OpenAI's GPT-3.5](https://www.openai.com/) for natural language understanding and generation.

