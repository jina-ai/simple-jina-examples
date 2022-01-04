# 4. Working with metadata

Metadata is additional information about a Document that may be relevant. It is **not** encoded in the indexing process, so makes no difference to a Document's searchability.

In this unit, we:

- Switch to a [more complicated, real-world dataset](https://www.kaggle.com/thunderz/anime-dataset?select=anime_data.csv)
- Tell `from_csv()` to extract our main data from the "Description field" (setting `Document.text` to `Description`). `from_csv()` extracts all other fields and sets them as metadata in `Document.tags` ([docs reference](https://docs.jina.ai/fundamentals/document/document-api/#document-tags))
- Rewrite our `print_search_results()` function in `helper.py` to show some relevant metadata
