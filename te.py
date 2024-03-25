import base64
import tkinter as tk
from tkinter import simpledialog
from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, AIMessage
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

def encode_image(image_path):
    """Encode an image to base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Initialize your chat model
chain = ChatOpenAI(model="gpt-4-vision-preview", max_tokens=1024)
# Example image encoding
# image = encode_image("test.jpeg")

# Initialize conversation history
conversation_history = []

# Setup the initial message for the chatbot scenario
initial_message = AIMessage(
    content="You will be a tutor for math students and will help them solve the questions. The student will upload the question with the working out and you will be guiding students through problem-solving steps, offering hints instead of direct answers to encourage critical thinking don't make the hints give away the answer."
)
conversation_history.append(initial_message)

# Function to update conversation with user input and get response
def update_conversation(user_input):
    user_message = HumanMessage(content=[{"type": "text", "text": user_input}])
    conversation_history.append(user_message)
    response = chain.invoke(conversation_history)
    conversation_history.append(response)
    return response.content

# Tkinter GUI setup
class ChatbotUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot Tutor")

        self.text_widget = tk.Text(master, state='disabled', width=80, height=20)
        self.text_widget.pack(padx=5, pady=5)

        self.entry_widget = tk.Entry(master, width=80)
        self.entry_widget.pack(padx=5, pady=5)
        self.entry_widget.bind("<Return>", self.handle_return)

    def handle_return(self, event):
        user_input = self.entry_widget.get()
        self.entry_widget.delete(0, tk.END)
        self.update_chat_window(f"You: {user_input}\n")
        bot_response = update_conversation(user_input)
        self.update_chat_window(f"Bot: {bot_response}\n")

    def update_chat_window(self, message):
        self.text_widget.configure(state='normal')
        self.text_widget.insert(tk.END, message)
        self.text_widget.configure(state='disabled')
        self.text_widget.see(tk.END)

root = tk.Tk()
chat_ui = ChatbotUI(root)
root.mainloop()
