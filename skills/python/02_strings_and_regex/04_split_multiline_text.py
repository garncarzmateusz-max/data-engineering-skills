"""
Split multiline text into lines

Task:
Split multiline text into logical lines
using a cross-platform approach.

Useful for:
- text file parsing
- log preprocessing
- ETL input handling
- working with multiline payloads
"""


def split_text_into_lines(text: str) -> list[str]:
    """
    Split multiline text into lines.
    """
    return text.splitlines()


def split_string_records(values: list) -> list[list[str]]:
    """
    Split only string records into lists of lines.
    """
    result = []

    for item in values:
        if isinstance(item, str):
            result.append(split_text_into_lines(item))

    return result


if __name__ == "__main__":

    text = "Jan\nAnna\r\nPiotr"

    print(split_text_into_lines(text))