"""
Hindi Proverb Generator using Google Gemini API
Author: HARSH SHARMA 
Description: Enter a topic and get 5 famous Hindi proverbs with meaning.
Requirements: pip install google-genai
"""

import os  # For reading environment variables
from google import genai  # Google's new Gemini client library
from google.genai import errors  # For error handling

def get_api_client():
    """
    Gets API key from environment variable and creates Gemini client.
    For Colab: os.environ['GOOGLE_API_KEY'] = 'your_key'
    For Local: export GOOGLE_API_KEY='your_key'
    """
    api_key = os.environ.get("GOOGLE_API_KEY") # Read key from environment
    
    if not api_key: # Check if key is missing
        raise ValueError(
            "GOOGLE_API_KEY not found! \n"
            "Colab: os.environ['GOOGLE_API_KEY'] = 'your_key'\n"
            "Local: export GOOGLE_API_KEY='your_key'"
        )
    
    try:
        client = genai.Client(api_key=api_key) # Initialize Gemini client
        return client
    except Exception as e: # Catch any connection error
        raise ConnectionError(f"Failed to connect to Gemini: {e}")

def generate_proverbs(client, topic):
    """
    Generates 5 famous Hindi proverbs for the given topic.
    """
    prompt = f"""
    You are a Hindi literature expert.
    Topic: "{topic}"
    
    Give me 5 famous Hindi proverbs on this topic.
    Format:
    1. Proverb: ...
       Meaning: ...
    
    Answer only in Hindi language, simple and easy words.
    """
    
    try:
        response = client.models.generate_content( # Call Gemini API
            model='gemini-1.5-flash-latest',
            contents=prompt
        )
        return response.text
    except errors.APIError as e: # Handle API errors
        return f"API Error: {e}"
    except Exception as e: # Handle other errors
        return f"Something went wrong: {e}"

def main():
    print("="*50)
    print("    Hindi Proverb Generator - Powered by Gemini")
    print("="*50)
    
    try:
        client = get_api_client() # Get the client first
    except ValueError as e:
        print(e)
        return
    
    while True: # Loop to take multiple topics
        topic = input("\nEnter a topic for proverbs (type 'exit' to quit): ")
        
        if topic.lower() == 'exit': # Exit condition
            print("Thank you! See you again 😊")
            break
        
        if not topic.strip(): # Check for empty input
            print("Please enter a topic!")
            continue
            
        print("\nGenerating...")
        result = generate_proverbs(client, topic)
        
        print("\n" + "-"*50)
        print(result)
        print("-"*50)

if __name__ == "__main__": # Entry point of the program
    main()