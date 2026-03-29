"""
Parse valid integers from mixed input

Task:
Convert only valid string values to integers
and skip invalid records safely.

Useful for:
- defensive parsing
- ETL preprocessing
- cleaning raw user input
- safe type conversion
"""


def parse_int(value: str) -> int | None:
    """
    Convert a string to int if possible.
    Return None for invalid values.
    """
    if not isinstance(value, str):
        return None

    try:
        return int(value)
    except ValueError:
        return None


def extract_valid_integers(values: list) -> list[int]:
    """
    Return only successfully parsed integer values.
    """
    result = []

    for item in values:
        parsed = parse_int(item)
        if parsed is not None:
            result.append(parsed)

    return result


if __name__ == "__main__":

    data = ["10", " 20 ", "x", None, "3.5", "0", "-7", ""]

    print(extract_valid_integers(data))