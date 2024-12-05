import google.generativeai as genai
import datetime
import traceback
import os

"""
Configuration:
Choose between:
    - gemini-1.5-flash
    - gemini-1.5-pro
    - gemini-pro
"""
def initialize_chat(api_key, generation_config, safety_settings):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash', 
        generation_config=generation_config, 
        safety_settings=safety_settings
    )
    return model.start_chat(history=[])

def send_and_print_message(session_name, chat, message):  # Retrieve session_name for debugging
    try:
        response = chat.send_message(message, stream=False)  # stream false sends the message all at once
        response_text = ""
        for chunk in response:
            response_text += chunk.text
        logs(session_name, message, response_text)  # Save the message and response to the log

        return response_text
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()  # Affiche l'endroit précis de l'erreur

        return None

def create_chat_session(api_key):
    # Load API key and configurations
    if not api_key:
        raise ValueError("API key not found. Please set your GEMINI_API_KEY in the environment.")

    generation_config = {
        "temperature": 0.7,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = {
        "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
        "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
        "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",
    }

    # Initialize and return the chat session
    return initialize_chat(api_key, generation_config, safety_settings)

def logs(session_name, user_message, response_text):
    """
    Save messages and responses in a log file with a timestamp.
    """
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y_%H:%M:%S")

    log_entry = f"{timestamp} |\nFunction: {session_name}\nUser:\n{user_message}\n{'*'*50}\nResponse: {response_text}\n{'-'*50}\n\n\n"
    
    # Generate the path to the log file
    log_file_path = "logs/gemini_discuss/prompts_log.log"
    
    # Create directories if necessary
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    
    with open(log_file_path, "a") as log_file:
        log_file.write(log_entry)