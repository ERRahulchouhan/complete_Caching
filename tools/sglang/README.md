# SGLang experiment

## What this tool is

An LLM serving framework with RadixAttention and prefix/KV reuse.

## Why use it

It can reuse shared prompt prefixes in multi-turn and repeated-context workloads.

## When to use it

Choose SGLang when its serving features and supported models fit your deployment and repeated-prefix workload.

## When not to use it

Its native inference cache does not replace a key/value cache for RAG answers or agent session state.

## Sample document used in the notebook

The notebook uses this short document for every tool experiment:

> RAG retrieves relevant passages from documents before answering a question.  
> A cache stores frequently requested RAG retrieval results so repeated questions return faster.  
> Agent memory stores task progress and tool results so later steps can continue the task.  
> Redis stores values by key and can expire them automatically using a time-to-live.

The notebook searches this text for the passage most relevant to the question and passes it with the question to the model endpoint. It demonstrates native model-side KV/prefix caching where supported; it does not cache application-level answer keys.

## Setup

Start an SGLang OpenAI-compatible server at localhost:30000 and install `pip install openai` in the client environment.

Install the notebook dependency:

```bash
pip install openai
```

## Run the experiment

Run the setup cell after the model endpoint is available. The notebook retrieves the matching passage from the shared sample document, sends the question and context to the model, and repeats requests to illustrate the engine-side cache opportunity.

Notebook: [`experiment.ipynb`](./experiment.ipynb)

The common workflow covers RAG retrieval, model requests with repeated context, agent questions, freshness, and application-cache integration notes.

## Tool-specific behavior

- **TTL:** The model engine manages KV-cache capacity and eviction; it does not expose per-answer TTL in this example.
- **Deletion:** Use the engine?s cache lifecycle controls for model state. Use an application key/value cache for per-answer deletion.

This is an inference engine, not an application key/value cache. The example retrieves a passage from the common sample document and sends it to the model. Native KV/prefix reuse is managed by the engine; it does not provide arbitrary answer-key TTL or deletion.
