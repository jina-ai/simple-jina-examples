# In this example we do the following:
# 1. Change to a more "real-world" csv
# 2. Extract text and metadata from the csv
# 3. Rewrite print_search_results() in helper.py to show "Title" metadata tag

from jina import Flow
from docarray import Document, DocumentArray
from helper import print_search_results

# Map "Description" field to our `Document.text`
docs = DocumentArray.from_csv("data/anime.csv", field_resolver={"Description": "text"})

flow = (
    Flow()
    .add(
        uses="jinahub+sandbox://CLIPEncoder",
    )
    .add(
        uses="jinahub+sandbox://SimpleIndexer",
    )
)

with flow:
    flow.index(inputs=docs)
    query = Document(text=input("Please enter your search term: "))
    response = flow.search(inputs=query, return_results=True)

# This is re-written in helper.py
print_search_results(response)