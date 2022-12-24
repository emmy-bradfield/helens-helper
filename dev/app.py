# Simple chatbot app using openAI. Takes input from the user on the command line and responds by suggesting minecraft 
# mods which they may like

# Import the necessary modules
import os
import random as rand
from time import sleep
import dotenv as env
import openai as ai

# Load the environment variables from the .env file
env.load_dotenv()
OPENAI_API_KEY = os.getenv("API_KEY")
ai.api_key = OPENAI_API_KEY

# Define the welcome text to appear on load
WELCOME = """

                                               _|                                                                  
 _|    _|            _|                      _|              _|    _|            _|                                
 _|    _|    _|_|    _|    _|_|    _|_|_|        _|_|_|      _|    _|    _|_|    _|  _|_|_|      _|_|    _|  _|_|  
 _|_|_|_|  _|_|_|_|  _|  _|_|_|_|  _|    _|    _|_|          _|_|_|_|  _|_|_|_|  _|  _|    _|  _|_|_|_|  _|_|      
 _|    _|  _|        _|  _|        _|    _|        _|_|      _|    _|  _|        _|  _|    _|  _|        _|        
 _|    _|    _|_|_|  _|    _|_|_|  _|    _|    _|_|_|        _|    _|    _|_|_|  _|  _|_|_|      _|_|_|  _|        
                                                                                     _|                            
                                                                                     _|                            
"""

# Start the application
if __name__ == '__main__':
    # Print out the welcome text to the consol
    print(WELCOME)
    print("\n\n\n\n")
    sleep(1)
    print("Bot: Hi there, Helen! I'm your personal minecraft mod advisor")
    sleep(1)
    print("Bot: Tell me all about what you want from a minecraft mod to get recommendations and advice")
    sleep(1)
    print("Bot: And when you're done, just say 'goodbye'")
    sleep(2)
    print("Bot: So, what are you looking for today?")
    
    # Create an empty array to save mods to, and an empty string for LAST_RESPONSE from the AI, and an empty 
    # array of RESPONSES to later append responses to
    SAVED_MODS = []
    LAST_RESPONSE = ""
    RESPONSES = []
    
    # Define the API Call Function
    def SEND_REQ():
    # Make an API call to the OpenAI model
        RESPONSE = ai.Completion.create(
            engine='text-davinci-003', #text-davinci-003 is a text/NL processing model which we want to use
            prompt=PROMPT, #this is the information we wish to send to the model
            max_tokens=128, #maximum number of API calls to make
            temperature=0.8, #amount of randomness, with 0.7 being slightly but not too random
            top_p=0.9, #select a response from the reponses with a summative likelyhood of accuracy of 90% (aka the best 90% of responses)
            frequency_penalty=-0.2, #increase the chances of a word being selected again if it has been used
            presence_penalty=0.3 #decrease the chances of a word being selected again if it exists already in the text
        )
        return RESPONSE
    
    # Start a loop so the ChatBot will continue to respond to user input
    while True:        
        USER = input("You: ")
        LAST_REQ = USER
        # If the user's input is 'goodbye', say "goodbye" and exit the program
        if USER.lower() == "goodbye":
            print("Bot: Okay, goodbye!")
            os._exit(0)
        elif "EXPLORE" in USER:
            # Create a prompt to send to the AI which includes the user's input (USER) and specified mod requesting 
            # more information about that mod
            PROMPT = f"""
            I would like to learn more about the minecraft mod {USER.split("EXPLORE", 1)[1]}. Can you please tell me
            all that you know about it
            """
            # Call SEND_REQ with the PROMPT
            MSG = SEND_REQ()
            print(f"Bot: {MSG['choices'][0]['text']}")
            sleep(4)
            # Ask the User for input
            print(f"Bot: So, what are you looking for today?")
        elif USER == "MORE":
            # Append the last recommendation the AI gave to the RESPONSES array
            RESPONSES.append(LAST_RESPONSE)
            # Create a prompt to send to the AI which includes the user's input (USER) and requests recommendations 
            # back in a structured format, specifically refusing responses which have already been recieved
            PROMPT = f"""
            I would like you to recommend me some minecraft mods. My criteria is {USER}.
            For each mod you recommend, please respond with the mod's name, a brief description, information on where
            to download it, and why you recommended it in the following format:
            Mod Name | Mod Description
            Download Information
            - Why you recommended it
            Please do NOT recommend the following Mods:
            {RESPONSES}
            """
            # Call SEND_REQ with the PROMPT
            MSG = SEND_REQ()
            print(f"Bot: {MSG['choices'][0]['text']}")
            sleep(1)
            # Instructs the User of the additional options they can make now they've requested a mod
            print("Bot: To learn more about a mod, respond with EXPLORE <Mod-Name>")
            sleep(1)
            print("Bot: To view more recommended mods, respond with MORE")
            sleep(1)
            print("Bot: To save a mod to your saved_mods file, respond with SAVE <Mod-Name>")
            sleep(1)
            print("Bot: Or, simply type a new request")         
        else:       
            # Clear the RESPONSES array, as we only want to store recommended mods if they are for the same request
            RESPONSES.clear()
            # Create a prompt to send to the AI which includes the user's input (USER) and requests recommendations 
            # back in a structured format
            PROMPT = f"""
            I would like you to recommend me some minecraft mods. My criteria is {USER}.
            For each mod you recommend, please respond with the mod's name, a brief description, information on where
            to download it, and why you recommended it in the following format:
            Mod Name | Mod Description
            Download Information
            - Why you recommended it
            """
            # Call SEND_REQ with the PROMPT
            MSG = SEND_REQ()
            print(f"Bot: {MSG['choices'][0]['text']}")
            sleep(1)
            # Instructs the User of the additional options they can make now they've requested a mod
            print("Bot: To learn more about a mod, respond with EXPLORE <Mod-Name>")
            sleep(1)
            print("Bot: To view more recommended mods, respond with MORE")
            sleep(1)
            print("Bot: Or, simply type a new request")
        
        # Store the last response the Bot gave, regardless of which option was chosen, just in case the 
        # next option the user chooses is "MORE" having previously chosen "MORE"
        LAST_RESPONSE = MSG['choices'][0]['text']
