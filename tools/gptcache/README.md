# GPTCache experiment

## What this tool is

A cache library for exact or semantically similar LLM queries and responses.

## Why use it

It can reduce repeated LLM work when prompts or questions recur; semantic mode can match similar wording.

## When to use it

Choose GPTCache when reducing repeated model calls is more important than simply storing arbitrary session fields.

## When not to use it

Avoid assuming its simple adapter provides per-key deletion or TTL; check the selected storage and eviction configuration.

## Sample document used in the notebook

The notebook uses this short document for every tool experiment:

> RAG retrieves relevant passages from documents before answering a question.  
> A cache stores frequently requested RAG retrieval results so repeated questions return faster.  
> Agent memory stores task progress and tool results so later steps can continue the task.  
> Redis stores values by key and can expire them automatically using a time-to-live.

The notebook searches this text for the passage most relevant to the question. It caches the retrieved context with a document-versioned key. It demonstrates retrieval caching; connect your own LLM after retrieval when you want to cache generated answers too.

## Setup

No separate service is required for the simple local example; run `pip install gptcache`. GPTCache initializes its local backend.

Install the notebook dependency:

```bash
pip install gptcache
```

## Run the experiment

Run the setup cell, then run the RAG workflow cell. The first run retrieves and stores the passage; running it again should use the selected cache tool. Later cells reuse that passage for agent state, prompt data, and tool-result examples.

Notebook: [`experiment.ipynb`](./experiment.ipynb)

The common workflow covers RAG retrieval, agent session state, prompt/result reuse, TTL/freshness, reading cached values, and invalidation.

## Tool-specific behavior

- **TTL:** The notebook notes that this API does not expose per-entry TTL; use its documented versioning, backend policy, or process-wide expiry instead.
- **Deletion:** The simple API used here does not provide per-entry deletion; the notebook demonstrates versioned keys.

The example runs a small keyword retriever against the same sample document, then stores and reads the retrieved passage using this tool's own cache API. It does not create a mock LLM answer.
