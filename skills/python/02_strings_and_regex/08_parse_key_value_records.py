"""
Parse key=value records

Task:
Parse text records in key=value format,
keep valid entries and collect invalid lines separately.

Useful for:
- parsing config-like data
- ETL preprocessing
- validating semi-structured text
- building simple dictionaries from raw input
"""


def parse_key_value_line(line: str) -> tuple[str, str] | None:
    """
    Parse a single key=value line.

    Return (key, value) if valid, otherwise None.
    """
    key, separator, value = line.partition("=")

    if separator != "=":
        return None

    if not key or not value:
        return None

    return key, value


def parse_key_value_records(lines: list) -> tuple[dict[str, str], list]:
    """
    Parse valid key=value records into a dictionary
    and collect invalid lines separately.
    """
    parsed_data = {}
    invalid_lines = []

    for line in lines:
        if not isinstance(line, str):
            invalid_lines.append(line)
            continue

        parsed = parse_key_value_line(line)

        if parsed is None:
            invalid_lines.append(line)
            continue

        key, value = parsed
        parsed_data[key] = value

    return parsed_data, invalid_lines


def build_summary(total_lines: int, valid_count: int, invalid_count: int) -> str:
    """
    Build a simple processing summary.
    """
    return (
        f"Processed {total_lines} lines\n"
        f"Valid: {valid_count}\n"
        f"Invalid: {invalid_count}"
    )


if __name__ == "__main__":

    lines = [
        "user=Jan",
        "status=OK",
        "env=prod",
        "debug",
        "timeout=30",
        "user=Anna=Admin",
        "=invalid",
        "region=EU",
    ]

    parsed_data, invalid_lines = parse_key_value_records(lines)
    valid_count = len(lines) - len(invalid_lines)

    print(parsed_data)
    print(invalid_lines)
    print(build_summary(len(lines), valid_count, len(invalid_lines)))