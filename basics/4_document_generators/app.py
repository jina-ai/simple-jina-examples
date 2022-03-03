# In this example we do the following:
# 1. Use "from_csv" to load Documents
# 2. Remove our original "docs" DocumentArray

from jina import Flow
from docarray import Document, DocumentArray
from helper import print_search_results

# Pull Documents from a CSV file. For each line of the file, create one Document where `Document.text` comes from the line's content.
docs = DocumentArray.from_csv("data.csv")

flow = (
    Flow()
    .add(
        uses="jinahub://SpacyTextEncoder",
        uses_with={"model_name": "en_core_web_md", 'traversal_paths': 'r'},
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

with flow:
    flow.index(inputs=docs)
    query = Document(text=input("Please enter your search term: "))
    response = flow.search(inputs=query)

print_search_results(response)
