"""
Normalize CSV-like text

Task:
Normalize comma-separated text by trimming whitespace
around fields and rebuilding a canonical comma-separated line.

Useful for:
- text normalization
- CSV-like preprocessing
- ETL cleaning steps
- preparing data for comparison or storage
"""


def normalize_csv_line(line: str) -> str:
    """
    Normalize a CSV-like text line.
    """
    raw_fields = line.strip().split(",")
    cleaned_fields = [field.strip() for field in raw_fields]
    return ",".join(cleaned_fields)


def normalize_csv_lines(lines: list) -> list[str]:
    """
    Normalize multiple CSV-like text lines.
    """
    result = []

    for line in lines:
        if isinstance(line, str):
            result.append(normalize_csv_line(line))

    return result


if __name__ == "__main__":

    data = [
        " Jan , Anna , Piotr ",
        " A ,B , C",
        " one,two , three ",
    ]

    print(normalize_csv_lines(data))