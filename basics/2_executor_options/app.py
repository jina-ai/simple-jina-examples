# This example follows "minimum_example".
# In this example we do the following:
# 1. Move some things to helper.py to keep app.py light
# 2. Use "uses_with", "uses_metas", and "volumes" to pass more parameters to our Executors

from jina import Document, Flow
from helper import docs, print_search_results

flow = (
    Flow()
    .add(
        uses="jinahub://SpacyTextEncoder",
        # Change to "medium" model for better encoding
        uses_with={"model_name": "en_core_web_md"},
        name="encoder",
        install_requirements=True
    )
    .add(
        # Switch `uses` to pull from Docker, so we can pass `metas`
        uses="jinahub+docker://SimpleIndexer",
        # Set workspace directory name
        uses_metas={"workspace": "workspace"},
        # Use external volume otherwise Docker can't see our index
        volumes="./workspace:/workspace/workspace",
        name="indexer",
    )
)

with flow:
    flow.index(inputs=docs)
    query = Document(text=input("Please enter your search term: "))
    response = flow.search(inputs=query, return_results=True)

print_search_results(response)
