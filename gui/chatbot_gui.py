import tkinter as tk
from tkinter import scrolledtext
from chatbot.chatbot_logic import Chatbot  # Updated import statement

class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Chatbot")
        self.master.geometry("400x400")
        self.master.iconphoto(False, tk.PhotoImage(file='chatbot/icon.jpg'))  # Set application icon

        self.chatbot = Chatbot('data/chatbot.db', 'data/data.json')  # Placeholder for API key

        self.text_area = scrolledtext.ScrolledText(master, state='disabled')
        self.text_area.pack(pady=10)

        self.entry = tk.Entry(master, width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(pady=10)

    def send_message(self, event=None):
        user_input = self.entry.get()
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, "You: " + user_input + "\n")
        self.entry.delete(0, tk.END)

        answer = self.chatbot.get_answer(user_input)
        if answer is None:
            self.chatbot.save_question(user_input)
            answer = self.chatbot.query_chatgpt(user_input)
        
        if answer:
            self.text_area.insert(tk.END, "Chatbot: " + answer + "\n")
        else:
            self.text_area.insert(tk.END, "Chatbot: I don't know the answer to that.\n")

        self.text_area.config(state='disabled')
        self.text_area.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatbotGUI(root)
    root.mainloop()
