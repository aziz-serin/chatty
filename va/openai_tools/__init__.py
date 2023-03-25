import os
import logging

logging.basicConfig(level = logging.DEBUG)

env_variable_name = "OPENAI_API_KEY"
moderation_url = "https://api.openai.com/v1/moderations"
api_key = str(os.getenv(env_variable_name))

if len(api_key) < 1 or api_key == 'None':
    logging.debug("Env variable is not set or cannot be read")
    quit(-1)
