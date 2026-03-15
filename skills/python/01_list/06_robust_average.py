"""
Robust average with edge case handling

Task:
Calculate the average of valid integers in a list.

Rules:
- ignore invalid values
- ignore bool values
- return None if no valid integers are available

Useful for:
- data cleaning
- ETL pipelines
- safe aggregation
- defensive programming
"""


def average_valid_integers(values: list) -> float | None:
    """
    Return average of valid integers.
    Return None if no valid integers are found.
    """

    total = 0
    count = 0

    for item in values:
        if isinstance(item, int) and not isinstance(item, bool):
            total += item
            count += 1

    if count == 0:
        return None

    return total / count


if __name__ == "__main__":

    data_empty = []
    data_single = [7]
    data_with_none = [10, None, 30]
    data_mixed = [10, True, None, 20, "30", 40]

    print(average_valid_integers(data_empty))      # None
    print(average_valid_integers(data_single))     # 7.0
    print(average_valid_integers(data_with_none))  # 20.0
    print(average_valid_integers(data_mixed))      # 23.333...