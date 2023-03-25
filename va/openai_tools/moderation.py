import requests
import logging
from requests import Response
from . import api_key, moderation_url
from .util import str2bool

logging.basicConfig(level = logging.DEBUG)

"""
Return a dict which contains 2 keys:
    - flagged: if the message is flagged
    - reasons: reasons why the message was flagged  
"""
def isValidPrompt(message:str) -> dict:
    response = __request(message)
    json = response.json()
    flagged = json["results"][0]["flagged"]
    logging.info(f'\nGiven message: {message} \nFlagged status: {flagged}')
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
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "input": message
    }
    return requests.post(moderation_url, headers=headers, json=data)
