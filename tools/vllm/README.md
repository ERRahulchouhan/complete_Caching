# vLLM experiment

## What this tool is

An LLM serving engine with Automatic Prefix Caching for reusable prompt prefixes.

## Why use it

It can avoid recomputing shared prompt prefixes, such as common RAG context or conversation history.

## When to use it

Choose vLLM for serving compatible open models with high throughput and reusable prompt prefixes.

## When not to use it

Its native KV cache is not an application cache for arbitrary query keys, TTLs, or session state.

## Sample document used in the notebook

The notebook uses this short document for every tool experiment:

> RAG retrieves relevant passages from documents before answering a question.  
> A cache stores frequently requested RAG retrieval results so repeated questions return faster.  
> Agent memory stores task progress and tool results so later steps can continue the task.  
> Redis stores values by key and can expire them automatically using a time-to-live.

The notebook searches this text for the passage most relevant to the question and passes it with the question to the model endpoint. It demonstrates native model-side KV/prefix caching where supported; it does not cache application-level answer keys.

## Setup

Install and start vLLM in a supported Linux/GPU environment. This notebook's offline example downloads a small model and may require significant memory.

Install the notebook dependency:

```bash
pip install vllm
```

## Run the experiment

Run the setup cell after the model endpoint is available. The notebook retrieves the matching passage from the shared sample document, sends the question and context to the model, and repeats requests to illustrate the engine-side cache opportunity.

Notebook: [`experiment.ipynb`](./experiment.ipynb)

The common workflow covers RAG retrieval, model requests with repeated context, agent questions, freshness, and application-cache integration notes.

## Tool-specific behavior

- **TTL:** The model engine manages KV-cache capacity and eviction; it does not expose per-answer TTL in this example.
- **Deletion:** Use the engine?s cache lifecycle controls for model state. Use an application key/value cache for per-answer deletion.

This is an inference engine, not an application key/value cache. The example retrieves a passage from the common sample document and sends it to the model. Native KV/prefix reuse is managed by the engine; it does not provide arbitrary answer-key TTL or deletion.
