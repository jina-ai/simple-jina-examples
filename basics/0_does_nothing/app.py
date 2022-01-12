from jina import Flow
from docarray import Document, DocumentArray

print("This example is to test that the most basic Jina stuff works without issues. The example isn't intended to do anything at all beyond that")

docs = DocumentArray(
    [
        Document(),
        Document()
    ]
)

flow = Flow().add().add()

with flow:
    flow.index(inputs=docs)
