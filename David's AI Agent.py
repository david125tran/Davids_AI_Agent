"""
This script is designed to interact with the OpenAI API to assist in modifying a Python script.
It reads a specified Python file, generates a prompt based on its content and a user message,
and sends this prompt to the OpenAI API. The assistant's response is then saved to a new Python file.

API Integration
- The script uses the OpenAI API to generate responses based on a system prompt and user message.
- It requires the `python-dotenv` package to load environment variables from a `.env` file, specifically for the OpenAI API key.
- The OpenAI API key is loaded from a `.env` file, allowing for secure storage of sensitive information.
- The script uses the `openai` library to interact with the OpenAI API, specifically the chat completion endpoint.

Natural Language Processing
- The script constructs a user prompt that includes the content of a specified Python file and a custom message.
- It sends this prompt to the OpenAI API, which generates a response based on the provided context.
- The assistant's response is expected to be a valid Python script, which is then saved to a specified output file.
"""

# ---------------------------------- Terminal Installations ----------------------------------
# py -m pip install python-dotenv
# py -m pip install openai
# py -m pip install openai[embeddings]
# py -m pip install openai[chat]
# py -m pip install openai[whisper]
# py -m pip install openai[all]
# py -m pip install openai[all] --upgrade
# py -m pip install openai[all] --upgrade --force-reinstall


# ------------------------------------ Imports ----------------------------------   
import os
from dotenv import load_dotenv
from openai import OpenAI


# ------------------------------------ Constants/Variables ----------------------------------
# Specify the path for the output file
output_file_path = r"C:\Users\Laptop\Desktop\Coding Assistant\Output.py"


# ------------------------------------ Functions ---------------------------------- 
def read_python_file(file_path):
    """
    Reads the entire content of a Python file and returns it as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return ""
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return ""


def user_prompt_for(message, python_file):
    user_prompt = message + f"\nHere are the contents of the python file: {python_file}\n"

    return user_prompt


def get_openai_response(system_prompt, message, python_file):
    """
    Generates a response from the OpenAI API using a system prompt and the contents of a specified Python file,
    then saves the assistant's response to a predefined output file.

    Parameters:
        system_prompt (str): The initial system instruction to guide the behavior of the assistant.
        message (str): A custom user message or question to include in the prompt.
        python_file (str): The file path of a Python script whose contents will be included in the prompt.

    Behavior:
        - Reads the content of the specified Python file.
        - Constructs a prompt using the system and user messages.
        - Sends the prompt to OpenAI's chat completion endpoint (model="gpt-4o-mini").
        - Saves the assistant's response to a hardcoded file path (output_file_path).
        - Prints confirmation of success or an error message if saving fails.
    """
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(message, read_python_file(python_file))},
    ]

    # Calling OpenAI with system and user messages:
    response = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)

    # Save the response to a Python file
    try:
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(response.choices[0].message.content)

        print(f"Response saved to {output_file_path}")
    except Exception as e:
        print(f"An error occurred while saving the response: {e}")

    print("Completed!")


# ------------------------------------ Connect to OpenAPI API Platform ----------------------------------  
# Specify the path to your .env file
env_path = r"C:\Users\Laptop\Desktop\Coding Assistant\.env"

# Load the .env file
load_dotenv(dotenv_path=env_path, override=True)

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")

# print(api_key)

# Create an OpenAI instance
openai = OpenAI(api_key=api_key)


# ------------------------------------ Chatting with the Model ---------------------------------- 
system_prompt = """
                You are an assistant software engineer who is helping a colleague
                with their Python script.  You are going to be given a Python script and
                a message from the user.  Your job is to read the script, make changes, and
                then your response is going to be saved to a new Python file.  And so your 
                response should be a valid Python script that can be saved to a file.

                At the top of your response, provide to me a summary of changes and improvements
                that you made to the script.  But this summary should be in a comment at the top
                of the script so that the code will still execute properly.

                After that, provide the entire script so that it can executed properly. 
                """

python_file = r"C:\Users\Laptop\Desktop\IBJJF_Parser\ibjjf_parser.py"

message = """
I am showing you a script to scrape the IBJJF website to create an excel sheet of my Jiu
Jitsu teammates that are going to compete in a tournament.  Show me how I can improve this
script.
"""

get_openai_response(system_prompt, message, python_file)



