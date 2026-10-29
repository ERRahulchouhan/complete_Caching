# Prompt: Create Course Notebook Examples

Create complete, runnable examples for every course notebook in this Redis AI caching project. Cover these files in order:

1. `Module_01_Introduction_and_Setup.ipynb` — Redis and course introduction, environment setup, and connection check.
2. `Module_02_Exact_Match_Caching.ipynb` — exact-match LLM caching, cache hits/misses, TTL, batch requests, inspection, and invalidation.
3. `Module_03_Semantic_Caching.ipynb` — embeddings, similarity thresholds, semantic cache implementation, and examples with differently worded queries.
4. `Module_04_Agent_Memory.ipynb` — Redis-backed conversation history, separate sessions, sliding-window memory, and persistent user facts.
5. `Module_05_Rate_Limiting.ipynb` — fixed- and sliding-window rate limiting and its use with LLM requests.
6. `Module_06_RAG_Caching.ipynb` — embedding cache, retriever, and a complete RAG pipeline with answer caching.
7. `Module_07_Final_Gradio_App.ipynb` — a Gradio app demonstrating exact caching, semantic caching, agent memory, RAG, and a dashboard.

For each notebook, provide clearly ordered Markdown explanations and executable code cells, including realistic examples and expected outputs where useful. Use the existing project dependencies and `.env` variables (`OPENAI_API_KEY`, `GROQ_API_KEY`, `REDIS_HOST`, and `REDIS_PORT`). Never hard-code or expose API keys. Handle missing configuration or Redis connections clearly, and keep each notebook consistent with the earlier modules.

**Do not create or modify `README.md`, any `requirements*` file, or any Dockerfile/Docker Compose file.**
