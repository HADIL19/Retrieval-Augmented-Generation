#pip install langchain faiss-cpu openai tiktoken

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI

# 1. Your data
text = """
NumPy is a Python library for numerical computing.
It supports arrays, matrices, and linear algebra.
"""

# 2. Split text
splitter = CharacterTextSplitter(chunk_size=100)
docs = splitter.create_documents([text])

# 3. Embeddings
embeddings = OpenAIEmbeddings()

# 4. Vector store
db = FAISS.from_documents(docs, embeddings)

# 5. Ask a question
query = "What is NumPy used for?"
docs = db.similarity_search(query)

# 6. Generate answer
llm = OpenAI()
answer = llm(f"Answer using this context:\n{docs[0].page_content}")

print(answer)
