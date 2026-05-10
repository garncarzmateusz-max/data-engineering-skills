"""
Numeric type filtering, missing-value normalization and safe aggregation.

This module demonstrates basic numeric data-cleaning patterns:
- filtering real numeric values without accidentally accepting bool
- parsing numeric strings into int / float
- normalizing common missing-value markers to None
- calculating an average while safely ignoring missing values
"""


def is_real_number(value):
    """Return True for int/float values, but exclude bool."""
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def filter_real_numbers(values):
    """Return only real numeric values from a mixed input list."""
    real_numbers = []

    for value in values:
        if is_real_number(value):
            real_numbers.append(value)

    return real_numbers


def parse_numeric_value(value):
    """
    Convert a single value into int, float or None.

    Rules:
    - common missing markers become None
    - int-like strings become int
    - float-like strings become float
    - invalid values become None
    - bool is not treated as a number
    """
    missing_markers = {"", "n/a", "null", "none"}

    if value is None:
        return None

    if isinstance(value, bool):
        return None

    if is_real_number(value):
        return value

    if not isinstance(value, str):
        return None

    cleaned_value = value.strip().lower()

    if cleaned_value in missing_markers:
        return None

    try:
        return int(cleaned_value)
    except ValueError:
        pass

    try:
        return float(cleaned_value)
    except ValueError:
        return None


def normalize_numeric_values(values):
    """Normalize a list of mixed values into int, float or None."""
    normalized_values = []

    for value in values:
        normalized_values.append(parse_numeric_value(value))

    return normalized_values


def calculate_average(values):
    """
    Calculate the average of numeric values, ignoring None.

    Returns None when there are no valid numeric values.
    """
    total = 0
    count = 0

    for value in values:
        if is_real_number(value):
            total += value
            count += 1

    if count == 0:
        return None

    return total / count


if __name__ == "__main__":
    raw_values = [
        10,
        3.14,
        True,
        False,
        None,
        "7",
        " 42 ",
        "3.14",
        "",
        "N/A",
        "null",
        "abc",
        0,
        -5,
        2.0,
    ]

    real_numbers = filter_real_numbers(raw_values)
    normalized_values = normalize_numeric_values(raw_values)
    average_value = calculate_average(normalized_values)

    print("Real numbers:", real_numbers)
    print("Normalized values:", normalized_values)
    print("Average:", average_value)