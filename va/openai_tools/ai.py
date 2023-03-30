import openai
import os
from . import env_variable_name as env
from .error import OpenAIAPIKeyError
import logging

logging.basicConfig(level = logging.DEBUG)

"""
Base class for any OpenAI implementations
"""
class OpenAI:
    def __init__(self, model:str):
        self.model = model
        openai.api_key = get_api_key(env)

def get_api_key(env_variable_name:str):
    api_key = str(os.getenv(env_variable_name))
    if len(api_key) < 1 or api_key == 'None':
        message = "Env variable is not set or cannot be read"
        logging.debug(message)
        raise OpenAIAPIKeyError(message)
    return api_key