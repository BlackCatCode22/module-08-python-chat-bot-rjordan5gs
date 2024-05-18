# Chat Bot Documentation

This document provides instructions on how to use the provided chat bot powered by OpenAI's GPT-3.5 model. The bot can be interacted with via a console or through HTTP requests to a Flask web server.

## Setup

### Installation

- Ensure you have Python installed on your system.
- Install the required Python packages using pip:

### Obtain OpenAI API Key

- Sign up for an account on the OpenAI platform and obtain an API key.
- Replace `"OPENAI_API_KEY"` in the script with your actual API key.

## Usage

### Console Interaction

To interact with the chat bot via the console, follow these steps:

1. Navigate to the directory containing the script.
2. Run the script with the argument
   python ChatBotAPP.py console (`'console'`:
   `bash`

3. Enter your message when prompted with You:. Press Enter to send your message.
4. The bot will respond with its message.

### Web Server Interaction

To interact with the chat bot via HTTP requests to a Flask web server, follow these steps:

1. Ensure the script is running as a web server:

   - python ChatBotAPP.py

2. Send a POST request to the /chat endpoint with JSON data containing the user's message:

{
"prompt": "Your message here"
}

- For example, using curl:
  curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Your message here"}' http://localhost:5000/chat

### Notes

    - The bot maintains chat history to provide context-aware responses. Each conversation session builds upon the previous messages.
    - Rate limits are enforced by OpenAI's API. If the rate limit is exceeded, the bot will wait before retrying.
    - Ensure that the API key is kept secure and not shared publicly to prevent unauthorized access to the OpenAI services.

### Troubleshooting

    - If encountering errors or unexpected behavior, check the console output for error messages.
    - Ensure that the OpenAI API key is correctly set in the script.
    - Verify that the Flask web server is running and accessible.

Ending Notes: For some reason alot of the dependencies that were required to do this project wouldn't install onto the system I am currently using
So I had to really think outside the box on what it would take for this chatbot to work. For instance, I could not "pip install" anything besides
openai.

I tryed the best I could, but I think this project will require a little TLC on another computer, I will continue to update this program to get it working
even past this class. -RJ
