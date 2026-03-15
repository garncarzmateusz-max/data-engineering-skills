# Python Lists

This section contains selected list-based exercises focused on practical data processing patterns in Python.

## Topics covered

- deduplication with preserved order
- sequence validation
- finding the first break in an ordered sequence
- frequency counting without `dict`
- data validation and filtering
- robust average with edge case handling
- cleaning and normalizing mixed input data

## Why this section matters

Lists are one of the most commonly used data structures in Python.
They are often used in:

- data cleaning
- preprocessing
- simple ETL steps
- validation logic
- basic aggregation and reporting

The goal of this section is not only to practice list operations,
but also to build problem-solving patterns useful in real data workflows.

## Included exercises

- `01_deduplication_preserve_order.py`  
  Remove duplicates while preserving the original order.

- `02_sequence_sorted_check.py`  
  Check whether a sequence is sorted in ascending order.

- `03_first_break_index.py`  
  Find the index where a sequence stops being increasing.

- `04_frequency_count.py`  
  Count integer frequency using lists and loops only.

- `05_data_validation.py`  
  Validate input data and split valid vs invalid values.

- `06_robust_average.py`  
  Calculate an average safely with edge case handling.

- `07_data_cleaning_pipeline.py`  
  Normalize mixed input data and keep only usable numeric values.

## Key patterns practiced

- iteration over lists
- building result lists
- filtering by condition
- validation before processing
- aggregation with counters
- index-based reasoning
- safe handling of edge cases
- reusable helper functions