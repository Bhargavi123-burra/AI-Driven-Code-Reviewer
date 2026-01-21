from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model = 'gemini-embedding-001')

result = embeddings.embed_query('delhi is the captial of india')
print(str(result))
