from jina import Document, DocumentArray, Flow

docs = DocumentArray(
    [
        Document(),
        Document()
    ]
)

flow = Flow().add().add()

with flow:
    flow.index(inputs=docs)
