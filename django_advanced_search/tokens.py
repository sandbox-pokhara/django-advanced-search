import re


def get_tokens(search_term):
    """
    extracts advanced tokens from search_term
    >>> get_tokens("id:234 hello world")
    >>> ('hello world', [{'key': 'id', 'value': '234', 'type': 'equal'}])
    """
    token = []
    advanced_tokens = []
    for q in search_term.split(" "):
        # TODO: support other type of comparisions
        match = re.fullmatch("(\w+):(.+)", q)
        if match is not None:
            advanced_tokens.append(
                {
                    "key": match.group(1),
                    "value": match.group(2),
                    "type": "equal",
                }
            )
        else:
            token.append(q)
    return " ".join(token), advanced_tokens
