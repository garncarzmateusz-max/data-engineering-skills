# Python Numeric Fundamentals

This section contains selected numeric exercises focused on safe and practical work with numeric data in Python.

## Topics covered

- numeric type filtering
- excluding `bool` from numeric checks
- missing-value normalization
- safe string-to-number conversion
- average calculation with missing values
- floating-point precision
- rounding behavior
- half-to-even rounding
- `Decimal` as a different numeric model
- display formatting vs calculation logic
- threshold bugs caused by rounding
- tolerance-based float comparisons
- absolute and relative tolerance
- numeric validation pipelines
- valid and invalid record separation
- error tagging for invalid numeric input

## Why this section matters

Numeric data appears in many real-world workflows:
CSV files, reports, logs, API payloads, financial-like values,
metrics, validation checks, and ETL pipelines.

This section focuses on building practical patterns for:

- validating numeric input before using it
- normalizing missing and invalid values
- avoiding common float precision traps
- separating presentation formatting from business logic
- comparing float values safely with tolerance
- detecting boundary-related bugs
- building small validation pipelines for numeric records

The goal is not only to practice `int`, `float`, `round()` and basic operators,
but to develop reliable numeric-data handling patterns useful in ETL
and general data processing.

## Included exercises

- `01_numeric_type_filtering_and_missing_values.py`  
  Filter real numeric values, normalize missing markers, parse numeric strings,
  and calculate averages safely.

- `02_float_precision_rounding_and_decimal.py`  
  Demonstrate floating-point precision issues, half-to-even rounding,
  and the difference between `float` and `Decimal`.

- `03_rounding_formatting_and_threshold_bugs.py`  
  Show the difference between rounding for calculation and formatting for display,
  including threshold, validation and aggregation pitfalls.

- `04_tolerance_based_float_comparisons.py`  
  Compare float values using absolute tolerance, relative tolerance,
  and a combined tolerance strategy.

- `05_numeric_validation_pipeline.py`  
  Build practical validation patterns for numeric records, including clamping,
  percent change guards, valid/invalid splits, error tags and consistency checks.

## Key patterns practiced

- validation before conversion
- normalization before aggregation
- safe handling of missing values with `None`
- excluding `bool` from numeric type checks
- defensive parsing of mixed input
- separating raw values from display values
- avoiding early rounding in business logic
- preserving original indexes during filtering
- threshold-based classification
- range clamping
- zero-division guards
- valid and invalid data separation
- structured error tagging
- tolerance-based comparison of computed values
- distinguishing real differences from floating-point noise
- recognizing when tolerance is useful and when it can hide bugs