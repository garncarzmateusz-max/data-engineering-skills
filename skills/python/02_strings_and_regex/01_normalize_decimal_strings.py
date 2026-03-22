"""
Normalize decimal strings

Task:
Normalize numeric strings by converting comma to dot
and keep only values that match the expected format.

Useful for:
- input normalization
- validating raw numeric text
- ETL preprocessing
- defensive parsing
"""


def normalize_decimal_string(value: str) -> str | None:
    """
    Return a normalized numeric string or None if invalid.

    Rules:
    - trim surrounding whitespace
    - convert comma to dot
    - reject empty values
    - reject incomplete values such as "10," or "10."
    """
    if not isinstance(value, str):
        return None

    normalized = value.strip().replace(",", ".")

    if normalized == "":
        return None

    if normalized.endswith("."):
        return None

    try:
        float(normalized)
        return normalized
    except ValueError:
        return None


def extract_valid_decimal_strings(values: list) -> list[str]:
    """
    Return only valid normalized numeric strings.
    """
    result = []

    for item in values:
        normalized = normalize_decimal_string(item)
        if normalized is not None:
            result.append(normalized)

    return result


if __name__ == "__main__":

    data = ["12,5", "3.14", "7", "0,25", "abc", "", "10,"]

    print(extract_valid_decimal_strings(data))