import re

def markdown_to_blocks(markdown):
    return list(map(lambda a: a.strip(), re.split("\n{2,}", markdown)))