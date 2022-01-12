# A Document is the primitive data type of Jina. It can hold any kind of data.
# We use the docarray library for handling Documents (https://docarray.jina.ai)

from docarray import Document

# Let's create any empty Document to start
text_doc = Document()

# Let's set this Document to include some basic text
text_doc.text = "hello world!"

# Whatever kind of content is stored in the Document, you can access it with
# the .content attribute
print(text_doc.content)  # returns "hello world!"

# Let's see what else we can store

# URIs...
image_doc = Document(uri="image.png")

# Binary data
binary_doc = Document(buffer=b"\f1")

# Numpy ndarrays
import numpy as np
ndarray_doc = Document(blob=np.array([1, 2, 3]))

# Jina is a neural search framework, so it makes sense for us to include vector
# embeddings in the Document. We do this in the .embedding attribute, typically
# by passing the Document through an Executor (more on those in later examples)
image_doc.embedding = np.ndarray([1, 2, 3])

# We typically work with multiple Documents at once in Jina. 
# That's where the DocumentArray comes in. Typically we would convert the
# dataset we want to search into a DocumentArray

from docarray import DocumentArray

docs = DocumentArray(
    [
        Document(text="foo"),
        Document(text="bar"),
        Document(text="baz"),
    ]
)

# We'll talk more about Documents in DocumentArrays in future, including
# metadata and syntactic sugar to make DocumentArray creation easier
