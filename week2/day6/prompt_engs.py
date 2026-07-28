import os
from pathlib import Path 
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"


def llm_answer(prompt):
    message={
        "role":"user",
        "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model, messages=messages)
    ans=response.choices[0].message.content
    return ans

bad_prompt="""
#ROLE:
you are a support assistant at a mobile/laptop company
#TASK
you have to classify the issue in a category
#CONSTRAINT
you have to classify the issue in on of the three categories namely billing,technical or return
#OUTPUT FORMAT
your answer should be in one word only . The one word should be one of the classification options 
#example
For instance if a user complain says he wants a refund then the category is return
#FALLBACK
if the issue is unrelated to any of the categories mentioned in constraints above then answer should be other
This is a user complaint:
my girlfriend is not talking to me


"""


print(llm_answer(bad_prompt))