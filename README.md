# Gemini AI Chatbot

A simple, command-line AI chatbot built with Google's Gemini API and Python. It allows users to interact with Google's Gemini model through a continuous conversation, receive AI-generated responses, and end the session whenever they want.

This project demonstrates the practical use of Generative AI, Large Language Models (LLMs), API integration, and conversational AI using Python.

## Overview

The Gemini AI Chatbot connects a Python application to Google's Gemini API. Users can type questions or messages in the terminal, and the chatbot sends them to Gemini to generate a response.

The conversation continues until the user types `exit`.

The project is designed as a beginner-friendly implementation of an AI-powered conversational application.

## Features

- **AI-Powered Responses:** Generates responses using Google's Gemini API.
- **Interactive Chat:** Accepts user input directly through the terminal.
- **Continuous Conversation:** Maintains a chat session while the program is running.
- **Simple Python Implementation:** Uses a straightforward structure that is easy to understand.
- **Environment-Based API Key:** Loads the API key from a `.env` file instead of hardcoding it in the source code.
- **Exit Command:** Allows users to end the conversation by typing `exit`.

## Technology Stack

- **Python** — Core programming language
- **Google Gemini API** — AI response generation
- **Google Gen AI SDK** — Communication with the Gemini API
- **python-dotenv** — Loading environment variables from a `.env` file

## How It Works

The chatbot follows a simple workflow:

1. Loads the API key from the environment configuration.
2. Initializes the Gemini API client.
3. Creates a chat session with the configured Gemini model.
4. Accepts a message from the user.
5. Sends the message to Gemini and receives a response.
6. Displays the response in the terminal.
7. Repeats the process until the user types `exit`.

## Project Structure

```text
Gemini-AI-Chatbot/
│
├── Gemini .py    # Main chatbot application
├── README.md     # Project documentation
└── .env          # Private API key configuration (created locally)
```

**Note:** The `.env` file should remain private and should not be uploaded to GitHub.

## Requirements

Before running the project, make sure you have:

- Python installed on your computer
- A Google account
- A Gemini API key
- An active internet connection

## Installation and Setup

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/muhammad-musab03/Gemini-AI-Chatbot.git
```

Move into the project directory:

```bash
cd Gemini-AI-Chatbot
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install google-genai python-dotenv
```

### 3. Get a Gemini API Key

1. Open [Google AI Studio](https://aistudio.google.com/).
2. Sign in with your Google account.
3. Find the API key section.
4. Create or obtain an API key according to the available options.

For official instructions, visit the [Gemini API documentation](https://ai.google.dev/gemini-api/docs).

### 4. Configure the Environment Variable

Create a file named `.env` in the project's root directory.

Add your API key using the variable name expected by the Python code:

```env
Gemini_key=your_actual_api_key_here
```

Replace `your_actual_api_key_here` with your own API key.

**Important:** Keep your API key private. Never publish it in your Python code, README, screenshots, or public repositories.

### 5. Run the Chatbot

Run the following command from the project directory:

```bash
python "Gemini .py"
```

If your Python installation uses the `python3` command, you can use:

```bash
python3 "Gemini .py"
```

## Usage

After starting the program, the terminal displays a welcome message and waits for your input.

Example interaction:

```text
Gemini Chatbot Started!
Type 'exit' to stop.

You: What is Artificial Intelligence?
Gemini: Artificial Intelligence (AI) is a field of computer science
that focuses on creating systems capable of performing tasks
that typically require human intelligence.

You: What is Python?
Gemini: Python is a high-level programming language known for
its simple syntax and wide range of applications.

You: exit
Chatbot stopped!
```

*The responses shown above are illustrative examples. Actual responses depend on the Gemini model and your input.*

## API Integration

This project uses Google's official Gen AI Python SDK to communicate with the Gemini API.

The main components are:

- **API Client:** Connects the Python application to Google's AI service.
- **API Key:** Authenticates requests to the API.
- **Chat Session:** Manages the conversation during the running session.
- **Message Handling:** Sends user messages to Gemini and displays the generated text.

The configured model name is specified in the Python source code. Model availability may change, so check the official [Gemini API documentation](https://ai.google.dev/gemini-api/docs) if you encounter a model-related error.

## Error Handling and Troubleshooting

**1. Missing API key**

Make sure the `.env` file exists in the project directory and contains the correct variable name:

```env
Gemini_key=your_actual_api_key_here
```

**2. Module not found**

Install the dependencies:

```bash
pip install google-genai python-dotenv
```

**3. API or authentication error**

Verify that your API key is valid and that your API access and usage limits permit the request.

**4. Model not found**

Check whether the model name configured in the source code is currently available to your API project. Update it to a supported model if necessary.

**5. Internet connection error**

Check your internet connection and try again.

## Security and Privacy

- Never commit your `.env` file or expose your API key publicly.
- Add `.env` to `.gitignore` to help prevent accidental uploads.
- If an API key is exposed, revoke or rotate it through the provider's official tools.
- Avoid sending passwords, confidential documents, or other sensitive personal information to the chatbot.

## Learning Objectives

This project provides practical experience with:

- Python programming
- API integration
- Environment variables and configuration
- Generative AI and Large Language Models
- Conversational AI workflows
- Managing an interactive command-line application

## Future Improvements

Possible improvements for future versions include:

- A graphical user interface
- Improved error handling
- Configurable model selection
- Conversation history export
- Support for additional input types where supported by the selected model

These are potential enhancements, not features currently claimed by this version.

## Limitations

- An internet connection is required to communicate with the Gemini API.
- API usage is subject to Google's applicable limits, availability, and pricing terms.
- Response quality and accuracy may vary.
- The current implementation is a command-line chatbot rather than a web-based application.

## Author

**Muhammad Musab**

GitHub: [@muhammad-musab03](https://github.com/muhammad-musab03)

## License

No license has been specified for this repository yet. Unless a license is added, the default copyright rules apply.

---

This project was created as a hands-on learning experience in Python, Generative AI, and Large Language Models, with the goal of building a foundation for more advanced AI applications.
