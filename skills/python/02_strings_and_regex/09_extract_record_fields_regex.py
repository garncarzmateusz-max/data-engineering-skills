"""
Extract multiple fields from a structured record

Task:
Use regex groups to extract multiple values
from a single structured text record.

Useful for:
- parsing semi-structured records
- regex group extraction
- log-like text processing
- simple schema-based parsing
"""

import re


RECORD_PATTERN = re.compile(
    r"^user=(\w+)\s+id=(\d+)\s+status=(\w+)$"
)


def parse_record(record: str) -> tuple[str, str, str] | None:
    """
    Extract user, id and status from a record.
    """
    match = RECORD_PATTERN.search(record)

    if not match:
        return None

    user = match.group(1)
    user_id = match.group(2)
    status = match.group(3)

    return user, user_id, status


if __name__ == "__main__":

    record = "user=mateusz id=483 status=ok"

    print(parse_record(record))
