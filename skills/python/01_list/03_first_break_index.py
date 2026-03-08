"""
First break index in an ascending sequence

Task:
Find the index where a list stops being strictly increasing.

Example:
[1, 3, 8, 2] -> first break at index 2,
because 8 >= 2.

Useful for:
- sequence validation
- trend checks
- detecting anomalies in ordered data
"""


def first_break_index(values: list) -> int | None:
    """
    Return the index where the sequence stops being strictly increasing.
    Return None if the whole sequence is increasing.
    """

    for i in range(len(values) - 1):
        if values[i] >= values[i + 1]:
            return i

    return None


if __name__ == "__main__":

    data_ok = [1, 3, 5, 8]
    data_bad = [1, 3, 8, 2]
    data_bad_2 = [5, 3, 8, 1]

    print(first_break_index(data_ok))     # None
    print(first_break_index(data_bad))    # 2
    print(first_break_index(data_bad_2))  # 0