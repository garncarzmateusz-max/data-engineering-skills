"""
Deduplication preserving order

Task:
Create a new list containing only unique elements
while preserving the original order.

Restrictions:
- no set()
- no dict
- use only lists and loops

This pattern is useful when order matters,
for example in data processing pipelines.
"""


def unique_preserve_order(values: list) -> list:
    """
    Return list of unique values preserving original order.
    """

    result = []

    for item in values:
        if item not in result:
            result.append(item)

    return result


if __name__ == "__main__":

    data = [1, 3, 5, 3, 6, 1, 7, 5, 2]

    unique_values = unique_preserve_order(data)

    print(unique_values)