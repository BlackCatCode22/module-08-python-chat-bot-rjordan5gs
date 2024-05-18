import openai
import time
from flask import Flask, request, jsonify

# OpenAI API key
openai.api_key = "OPENAI_API_KEY"

# Initialize chat history
chat_history = []

# Function to interact with GPT
def chat_with_gpt(prompt):
    global chat_history  # Access the global chat history variable
    while True:
        try:
            # Include the chat history in the prompt
            messages = [{"role": "user", "content": p} for p in chat_history]
            messages.append({"role": "user", "content": prompt})
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            response_content = response.choices[0].message['content'].strip()
            
            # Update chat history with the current prompt and response
            chat_history.append(prompt)
            chat_history.append(response_content)
            
            return response_content
        except openai.error.RateLimitError as e:
            print("Rate limit exceeded. Waiting before retrying...")
            time.sleep(60)  # Wait for 60 seconds before retrying
        except Exception as e:
            print(f"An error occurred: {e}")
            break

# Flask app setup
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get('prompt')
    response = chat_with_gpt(prompt)
    return jsonify({'response': response})

if __name__ == "__main__":
    import sys

    # Determine if the script is run with 'console' or 'web' argument
    if len(sys.argv) > 1 and sys.argv[1] == 'console':
        # Console-based interaction
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["quit", "exit", "bye"]:
                break

            response = chat_with_gpt(user_input)
            if response:
                print("Chatbot: ", response)
    else:
        # Run the Flask web server
        app.run(debug=True)
