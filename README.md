# AI Assistant Readme

This repository contains an AI Assistant designed to assist users with various tasks, such as extracting information from text, providing feedback on resumes and cover letters, and generating Taylor Swift-style song lyrics.

## Features and Use Cases

### Extract Information from a Piece of Text

#### Extract Date, Time, Item, Price from a PDF Receipt
- Utilize the AI Assistant to extract structured information, such as date, time, items, and prices, from a PDF receipt.
- The assistant employs natural language processing techniques to understand and extract relevant details.

#### Extract Name, Address, Phone Number from a Piece of Text and Insert into Postgres
- Leverage the assistant to extract specific information, such as names, addresses, and phone numbers, from unstructured text.
- The extracted data can be seamlessly inserted into a PostgreSQL database for further analysis or storage.

### AI Resume Feedback Bot

#### Upload Resume and Receive Feedback
- Users can upload their resumes, and the AI Assistant will provide constructive feedback on the content, formatting, and overall quality.
- The feedback can assist users in improving their resumes to increase their chances in job applications.

#### Upload Cover Letter and Receive Feedback
- Similar to the resume feedback feature, users can upload cover letters and receive feedback on structure, language, and effectiveness.
- The AI Assistant aims to enhance the quality of cover letters for job applications.

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

