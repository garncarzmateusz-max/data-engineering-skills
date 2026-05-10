"""
Float precision, rounding behavior and Decimal comparison.

This module demonstrates:
- why exact equality can be unsafe with floats
- how decimal-looking values may not be exact float values
- how Python's half-to-even rounding works
- why Decimal should be created from strings for decimal accuracy
- why Decimal is a different numeric model, not just a better round()
"""

from decimal import Decimal, ROUND_HALF_EVEN


def compare_float_sum(amounts, expected):
    """
    Compare a float sum with an expected value.

    Returns diagnostic information showing raw equality and rounded equality.
    """
    total = sum(amounts)

    return {
        "amounts": amounts,
        "total": total,
        "expected": expected,
        "raw_equal": total == expected,
        "rounded_equal": round(total, 2) == round(expected, 2),
    }


def inspect_float_values(values):
    """
    Return detailed decimal representations of float values.

    format(value, ".17f") helps reveal the actual stored float approximation.
    """
    inspected_values = []

    for value in values:
        inspected_values.append(
            {
                "value": value,
                "repr": repr(value),
                "decimal_view": format(value, ".17f"),
                "rounded_2": round(value, 2),
            }
        )

    return inspected_values


def demonstrate_half_to_even(values):
    """
    Demonstrate Python's half-to-even rounding for true .5 ties.
    """
    rounded_values = []

    for value in values:
        rounded_values.append(
            {
                "value": value,
                "rounded": round(value),
            }
        )

    return rounded_values


def compare_float_and_decimal(value_as_text, quant="0.01"):
    """
    Compare float rounding with Decimal quantization.

    Decimal is created from a string to preserve the intended decimal value.
    """
    float_value = float(value_as_text)
    decimal_value = Decimal(value_as_text)
    decimal_quant = Decimal(quant)

    return {
        "input": value_as_text,
        "float_value": float_value,
        "float_decimal_view": format(float_value, ".17f"),
        "float_rounded": round(float_value, 2),
        "decimal_value": decimal_value,
        "decimal_quantized": decimal_value.quantize(
            decimal_quant,
            rounding=ROUND_HALF_EVEN,
        ),
    }


if __name__ == "__main__":
    sum_checks = [
        ([0.1, 0.2, 0.3], 0.6),
        ([0.1] * 6, 0.6),
    ]

    for amounts, expected in sum_checks:
        result = compare_float_sum(amounts, expected)
        print(result)

    print()

    suspicious_values = [12.555, 12.545, 12.565]
    for item in inspect_float_values(suspicious_values):
        print(item)

    print()

    true_ties = [1.5, 2.5, 3.5, 4.5, 5.5]
    for item in demonstrate_half_to_even(true_ties):
        print(item)

    print()

    for value in ["12.555", "12.545", "12.565"]:
        result = compare_float_and_decimal(value)
        print(result)