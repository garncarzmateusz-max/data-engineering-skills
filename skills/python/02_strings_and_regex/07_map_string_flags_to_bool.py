"""
Map string flags to boolean values

Task:
Map known string representations of true and false
to boolean values and collect unknown values separately.

Useful for:
- rules-as-data
- input normalization
- ETL preprocessing
- data quality diagnostics
"""


TRUE_VALUES = {"true", "yes", "1"}
FALSE_VALUES = {"false", "no", "0"}


def normalize_string(value: str) -> str:
    """
    Normalize a string for rule-based comparison.
    """
    return value.strip().lower()


def map_string_to_bool(value: str) -> bool | None:
    """
    Map a normalized string to True, False or None.
    """
    normalized = normalize_string(value)

    if normalized in TRUE_VALUES:
        return True

    if normalized in FALSE_VALUES:
        return False

    return None


def extract_boolean_flags(values: list) -> tuple[list[bool], set[str]]:
    """
    Convert known string flags to booleans
    and collect unknown normalized values.
    """
    mapped = []
    unknown = set()

    for item in values:
        if not isinstance(item, str):
            continue

        normalized = normalize_string(item)
        result = map_string_to_bool(item)

        if result is None:
            unknown.add(normalized)
        else:
            mapped.append(result)

    return mapped, unknown


if __name__ == "__main__":

    data = ["True", "false", "YES", "0", "1", "No", "maybe"]

    result, unknown = extract_boolean_flags(data)

    print(result)
    print(unknown)