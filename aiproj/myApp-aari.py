import os
import sys
import json
import streamlit as st
from openai import OpenAI


client = OpenAI(
	api_key=os.environ.get("OPENAI_API_KEY")
)

role = f"""
You are a hilarious joke-teller. Process the given topic given in the input prompt and tell a related joke.
Don't repeat jokes.
"""

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
        response = client.chat.completions.create(
        messages=[
                {
                "role": "user",
                "content": prompt,
                }
        ],
        model="gpt-3.5-turbo",
                temperature=temperature
        )
        return response.choices[0].message.content

def main():
	
	st.write("# My Web App")
	inputPrompt = st.text_input("Give me a topic: ")
	prompt = f"""
	{role}.
	{inputPrompt}.
	"""
	isClicked = st.button("Tell me a joke")
	
	while(isClicked):	
		#prompt = input("Enter your input: ")
		myResponse = get_completion(prompt, 0)
		st.write(f"Response from OpenAI: {myResponse}")
		#print(myResponse)
		isClicked = False		

if __name__ == "__main__":
	main()
	
	
	
	
	
	

