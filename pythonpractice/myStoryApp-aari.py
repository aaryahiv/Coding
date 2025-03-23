import os
import sys
import json
import streamlit as st

from openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")


role = f"""

You are a creative storyteller. Process the given topic in the input prompt and write a story as specified.

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
    instruction = " "


    story = st.radio(
        "Select a story type:",
        options=["1-Line Story", "2-Line Story", "3-Line Story", "Freeform Story"]
    )

    if inputPrompt: 
        if story == "1-Line Story":
            instruction = f"Create a one-line story about {inputPrompt}."
        elif story == "2-Line Story":
            instruction = f" Create a two-line story about {inputPrompt}."
        elif story == "3-Line Story":
            instruction = f"Create a three-line story about {inputPrompt}."
        elif story == "Freeform Story":
            instruction = f"Create a freeform story about {inputPrompt}."

    prompt = f"""
    {role}.
    {instruction}.
    {inputPrompt}.
    """

    response = get_completion(prompt)
    st.write(f"Response from OpenAI: {response}")


if __name__ == "__main__":
    main()
