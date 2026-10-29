RAG caching types you should learn
Cache	What is cached	Example
Exact Cache	Same query → same response	Redis
Semantic Cache ⭐	Similar query → previous response	Redis / vector search
Embedding Cache ⭐	Text → embedding	Redis / local DB
Retrieval Cache ⭐	Query → retrieved chunks	Redis
Vector Search Cache	Search results	Redis
Reranking Cache	Query + docs → ranked docs	Redis
Context Cache	Final retrieved context	Redis
LLM Response Cache ⭐	Prompt → output	Redis / LangChain
Prompt Cache	Reusable prompt prefix	Model/inference layer
KV Cache ⭐	Attention K/V states	vLLM/SGLang
Prefix Cache ⭐	Common prompt prefix KV	vLLM/SGLang
Session Cache	Conversation/session data	Redis
Document Processing Cache	parsed/chunked docs	filesystem/DB
Tool Cache ⭐	tool(args) → result	Redis
Agent Step Cache	intermediate agent results	Redis/DB