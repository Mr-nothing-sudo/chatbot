import json
import sqlite3
import requests

# Add your ChatGPT API key here
CHATGPT_API_KEY = "add_your_API"  # Highlighted area for API key

class Chatbot:
    def __init__(self, db_path, json_path):
        self.db_path = db_path
        self.json_path = json_path
        self.load_data()

    def load_data(self, pdf_path=None):
        # Load data from SQLite database
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        
        # Load data from JSON file and PDF file if provided
        if pdf_path:
            self.extract_text_from_pdf(pdf_path)

        with open(self.json_path, 'r') as f:
            self.json_data = json.load(f)

    def get_answer(self, question):
        # Check SQLite database for answer
        answer = self.query_database(question)
        if answer:
            return answer
        
        # Check JSON data for answer
        answer = self.query_json(question)
        if answer:
            return answer
        
        # If no answer found, return None
        return None

    def extract_text_from_pdf(self, pdf_path):
        import PyPDF2
        text = ""
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text

    def query_database(self, question):
        # Implement database query logic here
        self.cursor.execute("SELECT answer FROM chatbot WHERE question=?", (question,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def query_json(self, question):
        # Implement JSON query logic here
        return self.json_data.get(question)

    def save_question(self, question):
        # Save unanswered question to a file or database
        with open('unanswered_questions.txt', 'a') as f:
            f.write(question + '\n')

    def query_chatgpt(self, question):
        # Implement API call to ChatGPT here
        response = requests.post('https://api.openai.com/v1/chat/completions', json={
            'model': 'gpt-3.5-turbo',
            'messages': [{'role': 'user', 'content': question}]
        }, headers={'Authorization': f'Bearer {CHATGPT_API_KEY}'})  # Using the API key
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        return None
