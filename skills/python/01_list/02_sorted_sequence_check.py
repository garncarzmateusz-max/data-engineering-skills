"""
Sequence sorted check

Task:
Check if a list is sorted in ascending order
without using sorted() or comparing to a copy.

Useful for:
- data validation
- monotonic checks
- detecting errors in sequences
"""


def is_sorted_ascending(values: list) -> bool:
    """
    Return True if the list is sorted in ascending order.
    """

    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False

    return True


if __name__ == "__main__":

    data_ok = [1, 2, 3, 5, 6, 7]
    data_bad = [1, 3, 2, 5]

    print(is_sorted_ascending(data_ok))
    print(is_sorted_ascending(data_bad))