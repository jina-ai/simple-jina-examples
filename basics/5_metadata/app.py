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
        uses="jinahub://SpacyTextEncoder",
        uses_with={"model_name": "en_core_web_md", 'traversal_paths': 'r'}, 
        name="encoder",
        install_requirements=True
    )
    .add(
        uses="jinahub://SimpleIndexer/v0.15",
        uses_metas={"workspace": "workspace"},
        volumes="./workspace:/workspace/workspace",
        name="indexer",
    )
)

with flow:
    flow.index(inputs=docs)
    query = Document(text=input("Please enter your search term: "))
    response = flow.search(inputs=query)

# This is re-written in helper.py
print_search_results(response)
