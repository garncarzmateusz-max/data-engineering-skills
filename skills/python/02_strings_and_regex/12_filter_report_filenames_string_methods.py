"""
Filter report filenames with string methods

Task:
Keep only filenames matching the format:
report_YYYY.csv

Useful for:
- string-based validation
- choosing simple tools for simple patterns
- file filtering
- comparing string methods with regex-based validation
"""


def is_valid_report_filename(filename: str) -> bool:
    """
    Validate filenames in the format:
    report_YYYY.csv
    """
    if not isinstance(filename, str):
        return False

    prefix = "report_"
    suffix = ".csv"

    if not filename.startswith(prefix):
        return False

    if not filename.endswith(suffix):
        return False

    middle = filename[len(prefix):-len(suffix)]

    return len(middle) == 4 and middle.isdigit()


def split_report_filenames(filenames: list) -> tuple[list[str], list[str]]:
    """
    Split filenames into valid and invalid groups.
    """
    valid_files = []
    invalid_files = []

    for filename in filenames:
        if is_valid_report_filename(filename):
            valid_files.append(filename)
        else:
            invalid_files.append(filename)

    return valid_files, invalid_files


if __name__ == "__main__":

    files = [
        "report_2024.csv",
        "report_2023.csv",
        "report_final.csv",
        "summary_2024.csv",
        "report_2024.txt",
        "report_ABC.csv",
    ]

    valid_files, invalid_files = split_report_filenames(files)

    print(valid_files)
    print(invalid_files)