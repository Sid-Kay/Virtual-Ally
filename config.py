# config.py
# Simple configuration helper. For safety, DO NOT put API keys here.
# To use a real LLM (OpenAI), store your key in an environment variable or a local `.env` file (never commit `.env`).
#
# Example `.env` contents (do NOT commit):
# OPENAI_API_KEY=sk-...
#
# This project will use a simulated LLM when OPENAI_API_KEY is not present.

import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', None)
