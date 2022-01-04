from jina import Document, DocumentArray, Flow
from docarray.document.generators import from_csv
from helper import print_search_results
import sys

PORT = 12345 # Port for RESTful interface

with open("data/anime.csv") as file:
    docs = DocumentArray(from_csv(file, field_resolver={"Description": "text"}))

flow = (
    Flow()
    .add(
        uses="jinahub://SpacyTextEncoder",
        uses_with={"model_name": "en_core_web_md"},
        name="encoder",
        install_requirements=True
    )
    .add(
        uses="jinahub+docker://SimpleIndexer",
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
        response = flow.search(inputs=query, return_results=True)

    print_search_results(response)

def search_restful():
    with flow:
        flow.protocol = "http"
        flow.port_expose = PORT
        # Keep Flow open until terminated by user
        flow.block()


argument = sys.argv[1]

if argument == "index":
    index()
elif argument == "search":
    search()
