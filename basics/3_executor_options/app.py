# This example follows "minimum_example".
# In this example we do the following:
# 1. Move some things to helper.py to keep app.py light
# 2. Use "uses_with", "uses_metas", and "volumes" to pass more parameters to our Executors

from jina import Flow
from docarray import Document
from helper import docs, print_search_results
       
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
    response = flow.search(inputs=query)

print_search_results(response)