# In this example we do the following:
# 1. Use "from_csv" to load Documents
# 2. Remove our original "docs" DocumentArray

from jina import Document, DocumentArray, Flow
from jina.types.document.generators import from_csv
from helper import print_search_results

# Pull Documents from a CSV file. For each line of the file, create one Document where `Document.text` comes from the line's content.
with open("data.csv") as file:
    docs = DocumentArray(from_csv(file))

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

with flow:
    flow.index(inputs=docs)
    query = Document(text=input("Please enter your search term: "))
    response = flow.search(inputs=query, return_results=True)

print_search_results(response)
