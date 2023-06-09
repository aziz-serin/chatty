import requests
import logging
from requests import Response
from . import moderation_url, env_variable_name
from .error import VAError
from .ai import get_api_key

logger = logging.getLogger("chatty")

"""
Return a dict which contains 2 keys:
    - flagged: if the message is flagged
    - reasons: reasons why the message was flagged  
"""
def isValidPrompt(message:str) -> dict:
    response = __request(message)
    json = response.json()
    flagged = json["results"][0]["flagged"]
    logger.info(f'\nGiven message: {message} \nFlagged status: {flagged}')
    categories = json["results"][0]["categories"]
    if not flagged:
        return {
            "flagged": flagged,
            "reasons": []
        }
    reasons = __parse_reasons(categories)
    return {
        "flagged": flagged,
        "reasons": reasons
    }

def __parse_reasons(categories:dict) -> list:
    reasons = []
    for key, value in categories.items():
        if value:
            reasons.append(key)
    return reasons

def __request(message:str) -> Response:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_api_key(env_variable_name)}"
    }
    data = {
        "input": message
    }
    try:
        response = requests.post(moderation_url, headers=headers, json=data)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as err:
        logger.error(err.response)
        raise VAError(err.response)
    except requests.exceptions.RequestException as err:
        logger.debug(err.response)
        raise VAError(err.response)
