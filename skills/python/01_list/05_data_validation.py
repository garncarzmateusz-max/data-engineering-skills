"""
Data validation and filtering

Task:
Validate input data and separate valid integers
from invalid values.

Useful for:
- input validation
- ETL pipelines
- data cleaning
- API / file processing
"""


def contains_only_integers(values: list) -> bool:
    """
    Check if all elements are integers (excluding bool).
    """

    for item in values:
        if not isinstance(item, int) or isinstance(item, bool):
            return False

    return True


def filter_integers(values: list) -> list:
    """
    Return list containing only valid integers.
    """

    result = []

    for item in values:
        if isinstance(item, int) and not isinstance(item, bool):
            result.append(item)

    return result


def split_valid_invalid(values: list) -> tuple[list, list]:
    """
    Split data into valid integers and invalid values.
    """

    valid = []
    invalid = []

    for item in values:

        if isinstance(item, int) and not isinstance(item, bool):
            valid.append(item)

        else:
            invalid.append(item)

    return valid, invalid


if __name__ == "__main__":

    data = [3, 12, "7", None, "", "abc", -4, 5, 0, 18, True]

    print(contains_only_integers(data))

    print(filter_integers(data))

    good, bad = split_valid_invalid(data)

    print(good)
    print(bad)