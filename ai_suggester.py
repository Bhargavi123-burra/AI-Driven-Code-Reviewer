from langchain_huggingface import HuggingFaceEndpoint

def get_ai_suggestion(code_string):
    """
    WHAT IT DOES: Asks AI for improvement
    """
    llm= HuggingFaceEndpoint(
        repo_id="codellama/CodeLlama-7b-Python-hf",
        huggingfacehub_api_token="your_token"
    
    )

    prompt = f"""Review this Python code and suggest improvements:
{code_string}

Provide 2-3brief suggestion for:
1.Code readability
2.Performance
3.Best practices"""
    
    response = llm.invoke(prompt)

    return [{
        "type": "AISuggestion",
        "message": response,
        "severity": "Info"
    }]
"""
**Example:**
```
INPUT CODE:
def add(x,y):
    return x+y

OUTPUT:
[{
    "message": "Consider adding type hints: def add(x: int,y:int)-> int"
}]"""    

    