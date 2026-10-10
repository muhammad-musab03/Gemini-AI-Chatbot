
from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

# Connect to Gemini
client = genai.Client(
    api_key=os.getenv("Gemini_key")
)

# Create chat session
chat = client.chats.create(
    model="gemini-3.8-flash"
)

print("Gemini Chatbot Started!")
print("Type 'exit' to stop.\n")

# Chatbot loop
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot stopped!")
        break

    # Send message to Gemini
    response = chat.send_message(user_input)

    # Display response
    print("Gemini:", response.text)
