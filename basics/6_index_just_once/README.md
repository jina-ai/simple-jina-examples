# 5. Indexing just once

In this unit, we:

- Break indexing and searching into different functions
- Call each function based on a command line argument, i.e. `python app.py index` or `python app.py search`

Previously both indexing and querying were run every time, meaning data got re-indexed every time. By switching to functions and arguments we can index once and query many times.
