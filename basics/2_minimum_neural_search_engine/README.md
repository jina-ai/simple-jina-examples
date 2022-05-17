# 1. Minimum working example

This is the starting example, in which we create the minimum viable Jina application. This will give you idea of the absolute basics, and then in following units we'll build up from there.

## Documents

We're using 5 quotes selected from "Squid Game". This would be a terrible real world dataset, but for the sake of our tutorial it teaches you what you need to know about how Documents work.

## Executors

We're using two Executors from Jina Hub. Why Hub? It means we don't have to worry about writing them ourselves - we can just use them out of the box. We'll look at writing Executors in an intermediate unit. Our Executors are:

- CLIPEncoder: Encodes each Document into vector embeddings using the CLIP model. We run it on the cloud using [Jina's Executor Sandbox](https://medium.com/jina-ai/jina-executor-sandbox-processing-data-in-the-cloud-cb9f12ee4715) 
- SimpleIndexer: 
  - When indexing: Builds a basic index of all the Documents (their text and embeddings)
  - When searching: Looks up the nearest neighbor to the search term

## Flow

The Flow uses Jina's default gRPC gateway. You don't need to worry about this for now. We'll build upon the Flow in other units.
