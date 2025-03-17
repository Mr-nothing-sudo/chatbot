Clone the Repository: If you haven't already, clone the repository to your local machine:

git clone cd Set Up a Virtual Environment: Create a virtual environment to manage dependencies:

python3 -m venv venv Activate the Virtual Environment:

source venv/bin/activate Install Required Packages: Install the necessary Python packages:

pip install PyPDF2 requests Add Your ChatGPT API Key: Open the chatbot/chatbot_logic.py file and replace YOUR_API_KEY with your actual ChatGPT API key:

CHATGPT_API_KEY = "YOUR_API_KEY" # Highlighted area for API key Prepare Data Files:

Place your PDF files in the data directory. Ensure the data/data.json file is present with the necessary question-answer pairs. Add Application Icon: If you have an icon.jpg file, place it in the chatbot directory. This will be used as the application icon.

Run the Application: Start the chatbot GUI:

python3 gui/chatbot_gui.py Notes: Ensure that you have Python 3 installed on your system. If you encounter any issues, check the console for error messages and ensure all paths are correct. By following these steps, you should be able to install and run the chatbot software successfully.
