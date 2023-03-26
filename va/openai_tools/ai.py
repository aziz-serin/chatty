from . import api_key
import openai

"""
Base class for any OpenAI implementations
"""
class OpenAI:
    def __init__(self, model:str):
        self.model = model
        openai.api_key = api_key