"""
Extract email domains safely

Task:
Extract the domain part from email-like strings.
Return None when the domain cannot be extracted safely.

Useful for:
- simple text parsing
- preprocessing email-like data
- safe handling of mixed input
- controlled nulls in ETL pipelines
"""


def extract_domain(value: str) -> str | None:
    """
    Return the substring after the first '@' or None if invalid.
    """
    if not isinstance(value, str):
        return None

    position = value.find("@")

    if position == -1:
        return None

    domain = value[position + 1:]

    if domain == "":
        return None

    return domain


def extract_domains(values: list) -> list[str | None]:
    """
    Extract domains from a list of values.
    """
    result = []

    for item in values:
        result.append(extract_domain(item))

    return result


if __name__ == "__main__":

    emails = [
        "jan.kowalski@gmail.com",
        "admin@company.pl",
        "no-at-symbol.com",
        "@missingname.com",
        "missingdomain@",
        None,
        123,
        "test@@example.com",
    ]

    print(extract_domains(emails))