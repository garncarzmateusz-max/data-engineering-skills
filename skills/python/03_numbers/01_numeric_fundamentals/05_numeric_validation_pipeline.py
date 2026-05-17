"""
Numeric validation pipeline examples.

This module demonstrates practical numeric validation patterns:
- finding max value with its original index in messy data
- threshold-based classification
- clamping values into a valid range
- calculating percent change with a zero-division guard
- validating transaction-like records with error tags
- comparing numeric outputs with tolerance-based checks
"""


def is_real_number(value):
    """Return True for int/float values, but exclude bool."""
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def find_max_with_index(values):
    """
    Find the maximum numeric value and its original index.

    Non-numeric values are ignored.
    Returns (None, None) when no valid numeric value exists.
    """
    max_value = None
    max_index = None

    for index, value in enumerate(values):
        if not is_real_number(value):
            continue

        if max_value is None:
            max_value = value
            max_index = index
            continue

        if value > max_value:
            max_value = value
            max_index = index

    return max_value, max_index


def classify_score(score):
    """
    Classify a score into a label.

    Rules:
    - None -> "missing"
    - score < 50 -> "fail"
    - 50 <= score < 80 -> "ok"
    - score >= 80 -> "great"
    """
    if score is None:
        return "missing"

    if not is_real_number(score):
        return "invalid"

    if score < 50:
        return "fail"

    if score < 80:
        return "ok"

    return "great"


def clamp(value, lower=0, upper=100):
    """
    Clamp a numeric value into the selected range.

    Example:
    clamp(120, 0, 100) -> 100
    clamp(-5, 0, 100) -> 0
    """
    return min(max(value, lower), upper)


def percent_change(old, new):
    """
    Calculate percent change from old to new.

    Returns None when old is zero, because the change is undefined.
    """
    if old == 0:
        return None

    return (new - old) / old * 100


def parse_amount(amount_text):
    """
    Convert amount text into float.

    Returns None when conversion fails.
    """
    try:
        return float(amount_text)
    except (TypeError, ValueError):
        return None


def validate_transaction(record, max_amount=1_000_000):
    """
    Validate a transaction-like record.

    Input record format:
    (amount_text, currency)

    Returns:
    - ("valid", normalized_record)
    - ("invalid", original_record_with_error_tag)
    """
    amount_text, currency = record
    amount = parse_amount(amount_text)

    if amount is None:
        return "invalid", (amount_text, currency, "NOT_A_NUMBER")

    if amount < 0:
        return "invalid", (amount_text, currency, "NEGATIVE_AMOUNT")

    if amount > max_amount:
        return "invalid", (amount_text, currency, "AMOUNT_TOO_LARGE")

    return "valid", (amount, currency)


def split_transactions(records, max_amount=1_000_000):
    """
    Split transaction-like records into valid and invalid lists.
    """
    valid_records = []
    invalid_records = []

    for record in records:
        status, result = validate_transaction(record, max_amount=max_amount)

        if status == "valid":
            valid_records.append(result)
        else:
            invalid_records.append(result)

    return valid_records, invalid_records


def are_close(a, b, abs_eps=1e-6, rel_eps=0.01):
    """
    Compare two numeric values using combined absolute and relative tolerance.
    """
    absolute_difference = abs(a - b)

    if absolute_difference <= abs_eps:
        return True

    scale = max(abs(a), abs(b))

    if scale == 0:
        return True

    relative_difference = absolute_difference / scale

    return relative_difference <= rel_eps


def compare_result_lists(results_a, results_b, abs_eps=1e-6, rel_eps=0.01):
    """
    Compare two lists of numeric results.

    Returns:
    - comparison flags for each pair
    - failed pairs with index and values

    Raises ValueError if the lists have different lengths.
    """
    if len(results_a) != len(results_b):
        raise ValueError("Both result lists must have the same length.")

    comparison_flags = []
    failed_pairs = []

    for index, (value_a, value_b) in enumerate(zip(results_a, results_b)):
        passes = are_close(value_a, value_b, abs_eps=abs_eps, rel_eps=rel_eps)
        comparison_flags.append(passes)

        if not passes:
            failed_pairs.append(
                {
                    "index": index,
                    "value_a": value_a,
                    "value_b": value_b,
                    "absolute_difference": abs(value_a - value_b),
                }
            )

    return comparison_flags, failed_pairs


def validate_source_consistency(records, abs_eps=1e-6, rel_eps=0.01):
    """
    Validate consistency between values from two data sources.

    Input record format:
    (record_id, source_a_value, source_b_value)
    """
    validation_results = []

    for record_id, value_a, value_b in records:
        passes = are_close(value_a, value_b, abs_eps=abs_eps, rel_eps=rel_eps)

        validation_results.append(
            {
                "record_id": record_id,
                "source_a_value": value_a,
                "source_b_value": value_b,
                "absolute_difference": abs(value_a - value_b),
                "passes_validation": passes,
            }
        )

    return validation_results


if __name__ == "__main__":
    mixed_values = [None, 10, 3, None, 25, 7, -2, "100", True]
    print("Max with index:", find_max_with_index(mixed_values))

    print()

    scores = [95, 80, 79, 50, 49, 0, None, 100, "bad"]
    score_labels = []

    for score in scores:
        score_labels.append(classify_score(score))

    print("Score labels:", score_labels)

    print()

    raw_values = [120, 100, 85, 0, -5, -20, 50, 130]
    clamped_values = []

    for value in raw_values:
        clamped_values.append(clamp(value))

    print("Clamped values:", clamped_values)

    print()

    change_pairs = [
        (100, 120),
        (200, 150),
        (0, 50),
        (50, 50),
        (80, 0),
    ]

    for old, new in change_pairs:
        print(
            {
                "old": old,
                "new": new,
                "percent_change": percent_change(old, new),
            }
        )

    print()

    transactions = [
        ("100.50", "PLN"),
        ("-20", "EUR"),
        ("999999.99", "USD"),
        ("1000001", "PLN"),
        ("abc", "PLN"),
        ("0", "EUR"),
    ]

    valid_transactions, invalid_transactions = split_transactions(transactions)

    print("Valid transactions:", valid_transactions)
    print("Invalid transactions:", invalid_transactions)

    print()

    results_a = [0.15 + 0.15, 0.1 + 0.2, 1.0 - 0.9, 0.3 - 0.2]
    results_b = [0.3, 0.3, 0.1, 0.1]

    flags, failed = compare_result_lists(results_a, results_b, abs_eps=1e-9)

    print("Comparison flags:", flags)
    print("Failed pairs:", failed)

    print()

    source_records = [
        ("sensor_A", 1000.0, 1001.0),
        ("sensor_B", 0.0, 0.0000004),
        ("sensor_C", 500.0, 530.0),
    ]

    for result in validate_source_consistency(source_records):
        print(result)