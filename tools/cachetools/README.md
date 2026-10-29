# cachetools experiment

## What this tool is

Python utilities for in-memory TTL and LRU caches.

## Why use it

It is lightweight for caching retrieval results inside one Python process.

## When to use it

Choose cachetools for local prototypes or per-worker caches where losing entries on restart is acceptable.

## When not to use it

Avoid it when multiple workers must share entries or when cache data must persist across restarts.

## Sample document used in the notebook

The notebook uses this short document for every tool experiment:

> RAG retrieves relevant passages from documents before answering a question.  
> A cache stores frequently requested RAG retrieval results so repeated questions return faster.  
> Agent memory stores task progress and tool results so later steps can continue the task.  
> Redis stores values by key and can expire them automatically using a time-to-live.

The notebook searches this text for the passage most relevant to the question. It caches the retrieved context with a document-versioned key. It demonstrates retrieval caching; connect your own LLM after retrieval when you want to cache generated answers too.

## Setup

No cache service is required; run `pip install cachetools`. This notebook configures a one-hour process-local TTL.

Install the notebook dependency:

```bash
pip install cachetools
```

## Run the experiment

Run the setup cell, then run the RAG workflow cell. The first run retrieves and stores the passage; running it again should use the selected cache tool. Later cells reuse that passage for agent state, prompt data, and tool-result examples.

Notebook: [`experiment.ipynb`](./experiment.ipynb)

The common workflow covers RAG retrieval, agent session state, prompt/result reuse, TTL/freshness, reading cached values, and invalidation.

## Tool-specific behavior

- **TTL:** The notebook notes that this API does not expose per-entry TTL; use its documented versioning, backend policy, or process-wide expiry instead.
- **Deletion:** The notebook demonstrates deleting a key through the tool API.

The example runs a small keyword retriever against the same sample document, then stores and reads the retrieved passage using this tool's own cache API. It does not create a mock LLM answer.
