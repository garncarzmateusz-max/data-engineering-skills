"""
Tolerance-based float comparisons.

This module demonstrates:
- why direct equality can be unsafe with floats
- how absolute tolerance works
- why epsilon must match the scale of the data
- why relative tolerance is useful for large values
- why relative-only tolerance breaks down near zero
- how to combine absolute and relative tolerance into a more robust rule
"""


def are_equal_absolute(a, b, abs_eps=1e-9):
    """Return True if two numbers are close enough by absolute tolerance."""
    return abs(a - b) <= abs_eps


def relative_difference(a, b):
    """
    Calculate the relative difference between two numbers.

    Returns 0.0 when both values are exactly zero.
    """
    scale = max(abs(a), abs(b))

    if scale == 0:
        return 0.0

    return abs(a - b) / scale


def are_equal_relative(a, b, rel_eps=0.01):
    """Return True if two numbers are close enough by relative tolerance."""
    return relative_difference(a, b) <= rel_eps


def are_equal_combined(a, b, abs_eps=1e-9, rel_eps=0.01):
    """
    Return True if two numbers pass absolute or relative tolerance.

    Absolute tolerance protects near-zero comparisons.
    Relative tolerance protects comparisons across larger scales.
    """
    return are_equal_absolute(a, b, abs_eps) or are_equal_relative(a, b, rel_eps)


def compare_pairs_absolute(pairs, abs_eps):
    """Compare pairs using absolute tolerance."""
    results = []

    for a, b in pairs:
        difference = abs(a - b)

        results.append(
            {
                "a": a,
                "b": b,
                "absolute_difference": difference,
                "abs_eps": abs_eps,
                "passes": difference <= abs_eps,
            }
        )

    return results


def compare_pairs_relative(pairs, rel_eps):
    """Compare pairs using relative tolerance."""
    results = []

    for a, b in pairs:
        rel_diff = relative_difference(a, b)

        results.append(
            {
                "a": a,
                "b": b,
                "relative_difference": rel_diff,
                "rel_eps": rel_eps,
                "passes": rel_diff <= rel_eps,
            }
        )

    return results


def compare_pairs_combined(pairs, abs_eps, rel_eps):
    """Compare pairs using combined absolute and relative tolerance."""
    results = []

    for a, b in pairs:
        abs_diff = abs(a - b)
        rel_diff = relative_difference(a, b)

        passes_absolute = abs_diff <= abs_eps
        passes_relative = rel_diff <= rel_eps

        results.append(
            {
                "a": a,
                "b": b,
                "absolute_difference": abs_diff,
                "relative_difference": rel_diff,
                "passes_absolute": passes_absolute,
                "passes_relative": passes_relative,
                "passes_combined": passes_absolute or passes_relative,
            }
        )

    return results


if __name__ == "__main__":
    print("Naive equality:")
    a = 0.1 + 0.2
    b = 0.3

    print(
        {
            "a": a,
            "b": b,
            "a_equals_b": a == b,
            "absolute_difference": abs(a - b),
            "passes_absolute_tolerance": are_equal_absolute(a, b, abs_eps=1e-9),
        }
    )

    print("\nAbsolute tolerance examples:")
    absolute_pairs = [
        (0.1 + 0.2, 0.3),
        (1.000, 1.009),
        (0.001, 0.002),
        (1_000_000.0, 1_000_000.009),
    ]

    for result in compare_pairs_absolute(absolute_pairs, abs_eps=0.01):
        print(result)

    print("\nRelative tolerance examples:")
    relative_pairs = [
        (10.0, 11.0),
        (1000.0, 1001.0),
        (1_000_000.0, 1_000_001.0),
    ]

    for result in compare_pairs_relative(relative_pairs, rel_eps=0.01):
        print(result)

    print("\nRelative tolerance near zero:")
    near_zero_pairs = [
        (1e-12, 0.0),
        (1e-10, 0.0),
        (1e-8, 0.0),
        (1e-6, 0.0),
    ]

    for result in compare_pairs_relative(near_zero_pairs, rel_eps=0.01):
        print(result)

    print("\nCombined tolerance examples:")
    combined_pairs = [
        (0.0, 0.0000004),
        (1000.0, 1001.0),
        (500.0, 530.0),
    ]

    for result in compare_pairs_combined(
        combined_pairs,
        abs_eps=1e-6,
        rel_eps=0.01,
    ):
        print(result)