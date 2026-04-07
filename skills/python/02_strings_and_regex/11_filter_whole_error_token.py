"""
Filter records containing the whole token ERROR

Task:
Keep only records where ERROR appears
as a whole token, not as part of a larger word.

Useful for:
- precise log filtering
- avoiding false positives
- regex boundary matching
- text rule validation
"""

import re


ERROR_TOKEN_PATTERN = re.compile(r"\bERROR\b")


def contains_error_token(text: str) -> bool:
    """
    Return True if text contains the whole token ERROR.
    """
    return bool(ERROR_TOKEN_PATTERN.search(text))


def filter_error_logs(logs: list) -> list[str]:
    """
    Return only logs containing the whole ERROR token.
    """
    result = []

    for log in logs:
        if isinstance(log, str) and contains_error_token(log):
            result.append(log)

    return result


if __name__ == "__main__":

    logs = [
        "ERROR in module payments",
        "WARNING before ERROR",
        "SUPERERROR happened",
        "error in lowercase",
        "ERROR123 is code",
        "status=ERROR",
        "NO_ERROR found",
    ]

    print(filter_error_logs(logs))