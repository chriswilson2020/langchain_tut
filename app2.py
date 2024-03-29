#!/usr/bin/env python3

"""
Title: Langchain Apps Number 2
--------------------------------------------------------------------------------
Author: Chris Wilson
Email: chris@cirrostrata.cloud
Date Created: 2024-03-29
Last Modified: 2024-03-29
--------------------------------------------------------------------------------
Purpose:
This script is designed to give an overview of getting started using langchain. 
This is the second script in the series 
It provides code snippets and functions building on the previous app.py
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

import os
import requests
