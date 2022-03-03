# In this example we do the following:
# 1. Break indexing and searching into two seperate functions
# 2. Set a command line argument to run one or other other
#
# This means we can create the index ONCE and search it many times

from jina import Flow
from docarray import Document, DocumentArray
from helper import print_search_results
import sys

docs = DocumentArray.from_csv("data/anime.csv", field_resolver={"Description": "text"})

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
        response = flow.search(inputs=query)

    print_search_results(response)


argument = sys.argv[1]

if argument == "index":
    index()
elif argument == "search":
    search()
