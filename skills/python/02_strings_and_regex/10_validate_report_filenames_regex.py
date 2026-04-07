"""
Validate report filenames with regex

Task:
Keep only filenames matching the format:
raport_YYYY_MM.csv

Useful for:
- naming convention validation
- file input filtering
- ETL file selection
- regex-based full-format validation
"""

import re


REPORT_FILENAME_PATTERN = re.compile(
    r"^raport_\d{4}_(0[1-9]|1[0-2])\.csv$"
)


def is_valid_report_filename(filename: str) -> bool:
    """
    Return True if filename matches the expected report format.
    """
    return bool(REPORT_FILENAME_PATTERN.search(filename))


def filter_valid_report_filenames(filenames: list) -> list[str]:
    """
    Return only valid report filenames.
    """
    result = []

    for filename in filenames:
        if isinstance(filename, str) and is_valid_report_filename(filename):
            result.append(filename)

    return result


if __name__ == "__main__":

    files = [
        "raport_2024_01.csv",
        "raport_2023_12.csv",
        "raport_24_01.csv",
        "raport_2024_1.csv",
        "Raport_2024_01.csv",
        "raport_2024_01.CSV",
        "raport_2024_01.csv.backup",
        "raport_2024_13.csv",
        "raport_2024_00.csv",
        "raport_2024_09.csv",
    ]

    print(filter_valid_report_filenames(files))