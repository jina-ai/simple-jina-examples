from typing import Protocol
from jina import Flow
from docarray import Document, DocumentArray
from helper import print_search_results
import sys

PORT = 12345 # Port for RESTful interface

docs = DocumentArray.from_csv("data/anime.csv", field_resolver={"Description": "text"})

flow = (
    Flow(protocol='http', port_expose=PORT)
    .add(
        uses="jinahub+sandbox://CLIPEncoder",
    )
    .add(
        uses="jinahub+sandbox://SimpleIndexer/v0.15",
        uses_metas={"workspace": "workspace"},
        volumes="./workspace:/workspace/workspace",
        name="indexer",
    )
)

def index():
    with flow:
        flow.index(inputs=docs)

def search():
    with flow:
        query = Document(text=input("Please enter your search term: "))
        response = flow.search(inputs=query)

    print_search_results(response)

def search_restful():
    with flow:
        # Keep Flow open until terminated by user
        flow.block()

argument = sys.argv[1]

if argument == "index":
    index()
elif argument == "search_restful":
    search_restful()
