# Python Strings and Regex

This section contains selected string- and regex-based exercises focused on practical text processing patterns in Python.

## Topics covered

- text normalization
- safe string-to-number conversion
- punctuation cleaning with configurable rules
- CSV-like text normalization
- splitting multiline text safely
- extracting domains from email-like strings
- mapping string flags to boolean values
- parsing `key=value` records
- regex-based field extraction
- regex-based filename validation
- whole-token matching with word boundaries
- choosing string methods vs regex depending on the task

## Why this section matters

Text data appears in many real-world workflows:
raw files, logs, configuration records, CSV-like input, API payloads,
and mixed user-provided values.

This section focuses on building practical patterns for:

- cleaning raw text
- normalizing input before processing
- validating formats
- parsing semi-structured records
- separating valid and invalid data
- using regex only where it adds clarity or precision

The goal is not only to practice string methods and regex syntax,
but to develop reusable text-processing patterns useful in ETL
and general data work.

## Included exercises

- `01_normalize_decimal_strings.py`  
  Normalize decimal strings and keep only valid numeric values.

- `02_remove_punctuation_with_rules.py`  
  Remove selected punctuation characters using configurable cleaning rules.

- `03_normalize_csv_like_text.py`  
  Normalize CSV-like text by trimming whitespace around fields.

- `04_split_multiline_text.py`  
  Split multiline text into logical lines with a cross-platform approach.

- `05_extract_email_domains.py`  
  Extract domains safely from email-like strings.

- `06_parse_valid_integers.py`  
  Convert valid string values to integers and skip invalid input safely.

- `07_map_string_flags_to_bool.py`  
  Map normalized string flags to boolean values and collect unknown cases.

- `08_parse_key_value_records.py`  
  Parse `key=value` records into a dictionary and separate invalid lines.

- `09_extract_record_fields_regex.py`  
  Use regex groups to extract multiple fields from a structured record.

- `10_validate_report_filenames_regex.py`  
  Validate report filenames using a full-format regex pattern.

- `11_filter_whole_error_token.py`  
  Filter log records containing `ERROR` as a whole token only.

- `12_filter_report_filenames_string_methods.py`  
  Validate simple report filenames using string methods instead of regex.

## Key patterns practiced

- normalization before validation
- validation before conversion
- defensive parsing of mixed input
- controlled nulls with `None`
- rules-as-data for text cleaning
- splitting and rebuilding structured text
- line-based text processing
- parsing semi-structured records
- separating valid and invalid data
- regex extraction with groups
- full-format validation with regex
- avoiding false positives in text matching
- choosing simple tools for simple patterns