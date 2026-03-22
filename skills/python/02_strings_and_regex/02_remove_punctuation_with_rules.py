"""
Remove selected punctuation from text

Task:
Remove selected punctuation characters from text records
using configurable cleaning rules.

Useful for:
- text cleaning
- preprocessing before tokenization
- ETL transformations
- rules-as-data pattern
"""


CHARS_TO_REMOVE = [".", ",", ";", ":"]


def remove_selected_punctuation(text: str, chars_to_remove: list[str]) -> str:
    """
    Remove selected characters from a single text value.
    """
    cleaned = text

    for char in chars_to_remove:
        cleaned = cleaned.replace(char, "")

    return cleaned


def clean_text_records(values: list) -> list:
    """
    Clean string records and keep non-string values unchanged.
    """
    result = []

    for item in values:
        if isinstance(item, str):
            result.append(remove_selected_punctuation(item, CHARS_TO_REMOVE))
        else:
            result.append(item)

    return result


if __name__ == "__main__":

    data = [
        "Jan, Anna; Piotr.",
        "Bez znaków",
        "Test: jeden, dwa; trzy.",
        None,
        123,
    ]

    print(clean_text_records(data))