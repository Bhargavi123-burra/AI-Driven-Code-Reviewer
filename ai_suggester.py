from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

print("HF TOKEN:", os.getenv("HUGGINGFACEHUB_API_TOKEN"))  # 👈 ADD THIS LINE

llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-large",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    temperature=0.3
)


model = ChatHuggingFace(llm=llm)


def get_ai_suggestions(code_string):
    """
    WHAT IT DOES: Asks AI improvement ideas
    """
    prompt = f"""
Review this Python code and suggest improvements: 
{code_string}

Provide 2-3 brief suggestions for:
1. Code readability
2. Performance
3. Best practices
"""

    try:
        response = model.invoke([HumanMessage(content=prompt)])
        ai_message = response.content

        return [{
            "type": "AISuggestion",
            "message": ai_message,
            "severity": "Info"
        }]

    except Exception as e:
        return [{
            "type": "Error",
            "message": str(e),   # convert exception to string
            "severity": "Info"
        }]

    
