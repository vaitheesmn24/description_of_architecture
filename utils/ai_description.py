import openai
import os

# openai.api_key=os.getenv("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")

# openai.api_key = "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"
openai.api_key="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"

def create_prompt(list_of_services):
    prompt = f"These are  the services used in an architecture diagram.Create a detailed description based on these services: {', '.join(list_of_services)}.\n" \
             + f"Additionally,explain the architectural flow based on the services used in the architecture diagram."
    
    return prompt

def description_prompt(text):
    
    description_prompt = create_prompt([f"{text}"])
    # description_prompt = create_prompt([text])
    
    # print(description_prompt,'--------------------------------------------------------')

    response = openai.Completion.create(engine="text-davinci-003",
                                                prompt= description_prompt,
                                                max_tokens=1024,
                                                temperature=0.7)
    
    formatted_response=response["choices"][0]["text"]
    
    
    # first_part = formatted_response.split("The architectural flow")[0]
    # second_part=formatted_response.split("The architectural flow")[1]
    
    # formatted_flow=first_part.strip()
    # formatted_res=second_part.strip()
    
    # complete_des=f"{formatted_flow} \n {formatted_res}"
        
    
    return formatted_response
    
    