import ast, json
from pathlib import Path
root = Path(r'e:\Udemy Security\caching\tools')
kv_tools = {
    'valkey','redis-open-source','dragonfly','memcached','diskcache','cachetools',
    'gptcache','langchain-cache','apache-ignite','hazelcast','keydb'
}
for path in sorted(root.glob('*/experiment.ipynb')):
    nb = json.loads(path.read_text(encoding='utf-8'))
    cells = nb['cells']
    name = path.parent.name
    if name in kv_tools:
        cells[4]['source'] = (
            f"## 1. Cache an actual RAG answer using {name.replace('-', ' ')}\n\n"
            "Enter a real question and the answer produced by your RAG application. This notebook does not create sample documents or simulate retrieval; it demonstrates the cache tool's real write/read calls."
        )
        cells[5]['source'] = "import hashlib\n\nquestion = input('Enter the RAG question: ').strip()\nanswer = input('Paste the answer returned by your RAG application: ').strip()\nquery_hash = hashlib.sha256(question.lower().encode()).hexdigest()\nrag_cache_key = f'rag:answer:v1:{query_hash}'\n\ncache_set(rag_cache_key, answer, ttl=3600)\nprint('Stored value:', cache_get(rag_cache_key))"
        cells[6]['source'] = '## 2. Store agent session state\n\nUse the cache tool to store real agent state from your application. Keep session data in a separate namespace and set a short expiration.'
        cells[7]['source'] = "session_id = input('Agent session ID: ').strip()\nlast_tool = input('Last tool used by the agent: ').strip()\nstate_key = f'agent:session:{session_id}:last_tool'\ncache_set(state_key, last_tool, ttl=1800)\nprint('Stored session state:', cache_get(state_key))"
        cells[8]['source'] = '## 3. Cache a prompt result\n\nPass an actual prompt and its real response from your model call. The cache stores the response using the tool configured above.'
        cells[9]['source'] = "prompt = input('Enter the prompt: ').strip()\nprompt_response = input('Paste the actual model response: ').strip()\nprompt_hash = hashlib.sha256(prompt.encode()).hexdigest()\nprompt_key = f'agent:prompt:v1:{prompt_hash}'\ncache_set(prompt_key, prompt_response, ttl=600)\nprint('Stored prompt response:', cache_get(prompt_key))"
        cells[10]['source'] = '## 4. TTL and freshness\n\nSet expiration on the cache entry where this tool supports it. The TTL behavior or limitation for this specific tool is described above.'
        cells[11]['source'] = "ttl_key = f'{rag_cache_key}:ttl-check'\ncache_set(ttl_key, 'temporary cache value', ttl=60)\nprint('Temporary value:', cache_get(ttl_key))"
        cells[12]['source'] = '## 5. Cache an agent tool result\n\nCache a real tool result under a namespaced key so the agent can reuse it instead of repeating an expensive call.'
        cells[13]['source'] = "tool_result = input('Paste the actual tool result to cache: ').strip()\ntool_result_key = f'agent:tool-result:{session_id}:{last_tool}'\ncache_set(tool_result_key, tool_result, ttl=600)\nprint('Stored tool result:', cache_get(tool_result_key))"
        cells[14]['source'] = '## 6. Delete cached data\n\nDelete the exact cache key after its answer or session state is no longer valid. Some tools do not expose per-entry deletion; the setup cell and tool-specific note explain those limitations.'
        if name == 'gptcache':
            cells[15]['source'] = "# GPTCache's simple API does not expose per-entry deletion. Use a new versioned key/prompt for fresh results.\nnew_rag_cache_key = f'v2:{rag_cache_key}'\nprint('Use this new versioned key:', new_rag_cache_key)"
        elif name == 'langchain-cache':
            cells[15]['source'] = "# LangChain InMemoryCache exposes clear() rather than portable per-key deletion.\ncache_delete(rag_cache_key)\nprint('LangChain cache cleared.')"
        else:
            cells[15]['source'] = "was_deleted = cache_delete(rag_cache_key)\nprint('Deleted RAG answer:', bool(was_deleted))"
        cells[16]['source'] = '## 7. Read a cached RAG answer\n\nEnter the same question used when storing the answer. The code creates the same key and calls the cache tool to read it.'
        cells[17]['source'] = "question_to_read = input('Enter the same RAG question: ').strip()\nquery_hash = hashlib.sha256(question_to_read.lower().encode()).hexdigest()\nrag_cache_key = f'rag:answer:v1:{query_hash}'\nprint('Cached answer:', cache_get(rag_cache_key))"
        cells[18]['source'] = '## 8. Use in an application\n\nBefore retrieval/model work, look up the question key. On a hit, return the value. On a miss, run your real retriever and model, then pass their result to the cache write call. No documents or retrieval results are mocked in this notebook.'
        cells[19]['source'] = f"print('{name.replace('-', ' ')} cache calls are ready. Connect the required cache service and enter values from your application.')"
    else:
        cells[4]['source'] = (
            f"## 1. Send real RAG inputs through {name.replace('-', ' ')}\n\n"
            "Paste the actual retrieved context and question from your RAG application. This notebook does not create sample documents or mock retrieval; the configured model tool handles inference and its own native cache."
        )
        cells[5]['source'] = "retrieved_context = input('Paste context returned by your RAG retriever: ').strip()\nquestion = input('Enter the RAG question: ').strip()\nprint(ask_rag(question, retrieved_context))"
        cells[6]['source'] = '## 2. Reuse the retrieved context\n\nAsk a second real question about the same retrieved context. The inference engine may reuse shared prompt/KV state where supported.'
        cells[7]['source'] = "second_question = input('Enter another question about the same context: ').strip()\nprint(ask_rag(second_question, retrieved_context))"
        cells[8]['source'] = '## 3. Agent conversation context\n\nPaste the current real context assembled by your agent. Native model cache reuse may apply to repeated prefixes; durable agent state belongs in a separate application cache.'
        cells[9]['source'] = "agent_context = input('Paste current context assembled by your agent: ').strip()\nagent_question = input('Enter the agent question: ').strip()\nprint(ask_rag(agent_question, agent_context))"
        cells[18]['source'] = '## 8. Production notes\n\nUse actual retrieved content and inspect the server cache metrics/logs to confirm native KV/prefix reuse. Use an application-side cache separately for answer-level TTL and deletion.'
        cells[19]['source'] = f"print('{name.replace('-', ' ')} inference call is ready. Start the model service and provide actual application inputs.')"
    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print('Updated', path)

# Validate JSON, 20 cells, and syntax for each code cell.
for path in root.glob('*/experiment.ipynb'):
    nb = json.loads(path.read_text(encoding='utf-8'))
    assert len(nb['cells']) == 20, (path, len(nb['cells']))
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            ast.parse(cell['source'], filename=f'{path} cell {i + 1}')
print('All 17 notebooks validated: exactly 20 cells and valid Python syntax.')
