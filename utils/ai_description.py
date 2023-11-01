import openai
import os


openai.api_key="open-api-key"

def create_prompt(list_of_services):
    prompt = f"These are  the services used in an architecture diagram.Create a detailed description based on these services: {', '.join(list_of_services)}.\n" \
             + f"Additionally,explain the architectural flow based on the services used in the architecture diagram."
    
    return prompt

def description_prompt(text):
    
    description_prompt = create_prompt([f"{text}"])
    

    response = openai.Completion.create(engine="text-davinci-003",
                                                prompt= description_prompt,
                                                max_tokens=1024,
                                                temperature=0.7)
    
    formatted_response=response["choices"][0]["text"]
    
    
    
    return formatted_response
    
    