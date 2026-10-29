# Memcached experiment

## What this tool is

A simple distributed memory cache for short-lived objects.

## Why use it

It is useful for caching repeated RAG retrieval outputs when simple key/value operations are sufficient.

## When to use it

Choose Memcached for straightforward ephemeral caching with expiration and no need for rich data structures.

## When not to use it

Do not use it as durable storage or where Redis data structures and persistence are required.

## Sample document used in the notebook

The notebook uses this short document for every tool experiment:

> RAG retrieves relevant passages from documents before answering a question.  
> A cache stores frequently requested RAG retrieval results so repeated questions return faster.  
> Agent memory stores task progress and tool results so later steps can continue the task.  
> Redis stores values by key and can expire them automatically using a time-to-live.

The notebook searches this text for the passage most relevant to the question. It caches the retrieved context with a document-versioned key. It demonstrates retrieval caching; connect your own LLM after retrieval when you want to cache generated answers too.

## Setup

Start Memcached at localhost:11211, then run `pip install pymemcache`.

Install the notebook dependency:

```bash
pip install pymemcache
```

## Run the experiment

Run the setup cell, then run the RAG workflow cell. The first run retrieves and stores the passage; running it again should use the selected cache tool. Later cells reuse that passage for agent state, prompt data, and tool-result examples.

Notebook: [`experiment.ipynb`](./experiment.ipynb)

The common workflow covers RAG retrieval, agent session state, prompt/result reuse, TTL/freshness, reading cached values, and invalidation.

## Tool-specific behavior

- **TTL:** Per-entry TTL is demonstrated.
- **Deletion:** The notebook demonstrates deleting a key through the tool API.

The example runs a small keyword retriever against the same sample document, then stores and reads the retrieved passage using this tool's own cache API. It does not create a mock LLM answer.
