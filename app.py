
"""
Title: Langchain Apps
--------------------------------------------------------------------------------
Author: Chris Wilson
Email: chris@cirrostrata.cloud
Date Created: 2024-03-29
Last Modified: 2024-03-29
--------------------------------------------------------------------------------
Purpose:
This script is designed to give an overview of getting started using langchain. It provides
code snippets building up from accessing the OpenAI api through to implementing chains to do something. 
This script is intended for following the courses and tutorials of aibychris.com.

Detailed Description:
The script was put together useing the langchain tutorial and various youtube videos
I highly reccomend usig pipenv and black to control the virtual environment and format your code
This script relies on a .env file to contain the relevant API keys and on langchain and openai libraries to be installed

Usage:
python3 app.py
or with pipenv installed
pipenv run python3 app.py

Examples:
N/A

Notes:
The current version is a work in progress check back later for more info.
As I am working through I will comment out previous examples to keept things neat in the terminal
I also want to reduce the cost of api calls by not calling already working snippets during testing
--------------------------------------------------------------------------------
"""


# imports in order to get started.  OS imports the environment variables and requests is for if we decide to do external api calls for linkedin or google etc
import os
import requests

from langchain_openai import ChatOpenAI

# set up our llm with a nice cheap model for testing
llm = ChatOpenAI(temperature=0.9, model_name='gpt-3.5-turbo')

# Simple no chain model. Just to get used to making the OpenAI calls
text =  "What are 5 vacation destinations for someone who likes to eat pasta?"
#output = llm.invoke(text)
#print(output.content)

# Now we add in prompt templates in order to start making dynamic requests
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
	input_variables=['food'],
	template="What are 5 vacation destinations for someone who likes to eat {food}?"
)

# In this example the output of invoking the llm is a class so we access the content of 
# it through dot notation

# print(prompt.format(food='dessert'),"\n")

#output = llm.invoke(prompt.format(food='dessert'))
#print(output.content)


# Lets make our first chain
from langchain.chains import LLMChain

# we will reuse the llm and prompt variables from above

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.invoke("fruit")["text"])


# Now lets plug agents into the mix and access google search api

from langchain.agents import load_tools
from langchain.agents import initialize_agent
