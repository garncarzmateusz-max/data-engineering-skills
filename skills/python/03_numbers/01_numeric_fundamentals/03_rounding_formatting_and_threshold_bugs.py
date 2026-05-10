"""
Rounding, display formatting and threshold-related bugs.

This module demonstrates:
- the difference between rounding a number and formatting it for display
- why formatted values should not be used for business logic
- how rounding can move values across thresholds
- why validation and aggregation should usually use raw values first
"""


def format_price(value, currency="PLN"):
    """Return a display-ready price string with exactly two decimal places."""
    return f"{value:.2f} {currency}"


def compare_rounding_and_formatting(value):
    """
    Compare round(value, 2) with f-string formatting.

    round(value, 2) returns a number.
    f"{value:.2f}" returns a string for presentation.
    """
    rounded_value = round(value, 2)
    formatted_value = f"{value:.2f}"

    return {
        "raw_value": value,
        "rounded_value": rounded_value,
        "rounded_type": type(rounded_value).__name__,
        "formatted_value": formatted_value,
        "formatted_type": type(formatted_value).__name__,
    }


def classify_raw_value(value, threshold=10):
    """Classify a value using the raw numeric value."""
    if value < threshold:
        return "below_threshold"

    return "at_or_above_threshold"


def classify_rounded_value(value, threshold=10, digits=2):
    """
    Classify a value after rounding.

    This intentionally demonstrates how rounding before a decision
    can change the classification result.
    """
    rounded_value = round(value, digits)

    if rounded_value < threshold:
        return "below_threshold"

    return "at_or_above_threshold"


def validate_raw_score(score, expected=10):
    """Validate a score using the raw value."""
    return score == expected


def validate_rounded_score(score, expected=10, digits=2):
    """
    Validate a score after rounding.

    This intentionally demonstrates a validation trap:
    a value can pass after rounding even if the raw value is not exact.
    """
    return round(score, digits) == expected


def average_raw_then_round(values, digits=2):
    """Calculate the average from raw values and round only the final result."""
    if not values:
        return None

    average = sum(values) / len(values)
    return round(average, digits)


def round_each_then_average(values, digits=2):
    """
    Round every value first and then calculate the average.

    This demonstrates how early rounding can distort aggregations.
    """
    if not values:
        return None

    rounded_values = []

    for value in values:
        rounded_values.append(round(value, digits))

    return sum(rounded_values) / len(rounded_values)


def demonstrate_carry_cascade(values):
    """
    Show values that cross a magnitude boundary after rounding.

    Example:
    9.999 -> 10.00
    99.995 -> 100.00
    """
    results = []

    for value in values:
        results.append(
            {
                "raw_value": value,
                "rounded_value": round(value, 2),
                "formatted_value": f"{value:.2f}",
            }
        )

    return results


if __name__ == "__main__":
    report_values = [12, 12.5, 12.567, 0, 3.1, 99.999]

    for value in report_values:
        print(format_price(value))

    print()

    print(compare_rounding_and_formatting(12.556))

    print()

    threshold_value = 9.999

    print("Raw classification:", classify_raw_value(threshold_value))
    print("Rounded classification:", classify_rounded_value(threshold_value))

    print()

    score = 9.999

    print("Raw validation:", validate_raw_score(score))
    print("Rounded validation:", validate_rounded_score(score))

    print()

    scores = [9.994, 9.994, 9.994]

    print("Average raw then round:", average_raw_then_round(scores))
    print("Round each then average:", round_each_then_average(scores))

    print()

    boundary_values = [9.999, 99.995, 999.995]

    for item in demonstrate_carry_cascade(boundary_values):
        print(item)