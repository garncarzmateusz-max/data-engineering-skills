"""
Frequency count without dict

Task:
Count how many times each integer appears in the list.
Use only lists and loops (no dict, no Counter).

This pattern is useful for:
- basic aggregation
- manual grouping
- understanding how counting works internally
"""


def count_integers_frequency(values: list) -> tuple[list, list]:
    """
    Return two lists:
    - unique integers
    - counts for each integer
    """

    numbers = []
    counts = []

    for item in values:

        if isinstance(item, int):

            if item not in numbers:
                numbers.append(item)
                counts.append(1)

            else:
                index = numbers.index(item)
                counts[index] += 1

    return numbers, counts


def count_value(values: list, target) -> int:
    """
    Count how many times target appears.
    """

    count = 0

    for item in values:
        if item == target:
            count += 1

    return count


if __name__ == "__main__":

    data = [3, 12, 7, 3, 10, 3, "Python", "abc", "", None, 12, "Python", 5, 3]

    nums, cnts = count_integers_frequency(data)

    print(nums)
    print(cnts)

    print(count_value(data, 5))
    print(count_value(data, "Python"))