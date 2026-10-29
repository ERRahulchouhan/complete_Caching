# Valkey experiment

## What this tool is

A distributed, Redis-compatible key-value store.

## Why use it

Use it when an application needs fast shared RAG-result and agent-session storage with TTLs.

## When to use it

Choose Valkey for a Redis-compatible service that you can operate as a distributed cache. It works well for shared cache entries across multiple application workers.

## When not to use it

Do not choose it when you need an embedded, process-only cache or when you cannot operate a cache service.

## Sample document used in the notebook

The notebook uses this short document for every tool experiment:

> RAG retrieves relevant passages from documents before answering a question.  
> A cache stores frequently requested RAG retrieval results so repeated questions return faster.  
> Agent memory stores task progress and tool results so later steps can continue the task.  
> Redis stores values by key and can expire them automatically using a time-to-live.

The notebook searches this text for the passage most relevant to the question. It caches the retrieved context with a document-versioned key. It demonstrates retrieval caching; connect your own LLM after retrieval when you want to cache generated answers too.

## Setup

Start a Valkey server reachable at localhost:6379, then run `pip install valkey`.

Install the notebook dependency:

```bash
pip install valkey
```

## Run the experiment

Run the setup cell, then run the RAG workflow cell. The first run retrieves and stores the passage; running it again should use the selected cache tool. Later cells reuse that passage for agent state, prompt data, and tool-result examples.

Notebook: [`experiment.ipynb`](./experiment.ipynb)

The common workflow covers RAG retrieval, agent session state, prompt/result reuse, TTL/freshness, reading cached values, and invalidation.

## Tool-specific behavior

- **TTL:** Per-entry TTL is demonstrated.
- **Deletion:** The notebook demonstrates deleting a key through the tool API.

The example runs a small keyword retriever against the same sample document, then stores and reads the retrieved passage using this tool's own cache API. It does not create a mock LLM answer.
