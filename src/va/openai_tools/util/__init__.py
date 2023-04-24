import tiktoken

def str2bool(string:str) -> bool:
    return string.lower() in ("true", "1", "yes")

def get_token_count(messages:list, model:str) -> int:
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = 0
    for message in messages:
        num_tokens += len(encoding.encode(message["content"]))
    return num_tokens
