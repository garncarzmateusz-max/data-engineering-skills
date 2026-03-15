"""
Data cleaning and normalization pipeline

Task:
Normalize mixed input data and keep only values
that can be interpreted as numbers.

Rules:
- accept int and float values (excluding bool)
- accept numeric strings such as "2", " 3 ", "2.5", "2,5"
- reject invalid values such as None, "abc", "", "2,5,7", "1.2.3"

Useful for:
- data cleaning
- input normalization
- ETL preprocessing
- validating raw user data
"""


def to_number(value) -> float | None:
    """
    Convert a value to float if it can be safely interpreted as a number.
    Return None for invalid values.
    """

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return float(value)

    if isinstance(value, str):
        normalized = value.strip().replace(",", ".")

        if normalized == "":
            return None

        if normalized.count(".") > 1:
            return None

        try:
            return float(normalized)
        except ValueError:
            return None

    return None


def count_usable_numbers(values: list) -> int:
    """
    Count how many values can be interpreted as numbers.
    """

    count = 0

    for item in values:
        if to_number(item) is not None:
            count += 1

    return count


def extract_usable_numbers(values: list) -> list:
    """
    Return normalized numeric values as floats.
    """

    result = []

    for item in values:
        number = to_number(item)
        if number is not None:
            result.append(number)

    return result


def extract_usable_with_index(values: list) -> list[tuple[int, float]]:
    """
    Return pairs of (index, normalized_number)
    for values that can be interpreted as numbers.
    """

    result = []

    for index, item in enumerate(values):
        number = to_number(item)
        if number is not None:
            result.append((index, number))

    return result


if __name__ == "__main__":

    data = [1, "2", None, 5, "abc", 10, " 3 ", "2,5", "1.2.3", True]

    print(count_usable_numbers(data))
    print(extract_usable_numbers(data))
    print(extract_usable_with_index(data))