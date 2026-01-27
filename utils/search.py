import re

def parse_definitions(markdown_text: str) -> dict:
    pattern = r"- \*\*(.*?)\*\* ?: ?(.*)"
    matches = re.findall(pattern, markdown_text)

    return {term.lower(): definition for term, definition in matches}
