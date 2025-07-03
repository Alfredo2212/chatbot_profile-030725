from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
import os, json

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

    with open("characters.json", "r") as f:
        characters = json.load(f)

    # Convert into langchain document
    docs = []
    for char in characters:
        content = f"Name: {char['name']} \nTags: {', '.join(char['tags'])}\n"
        content += f"Genre: {char['taxonomy'].get('genre')}, Species: {char['taxonomy'].get('species')}\n"
        content += f"Likes: {char['likes']}, Saves: {char['saves']}, Comments: {char['comments']}"
        docs.append(Document(page_content=content, metadata={"name": char["name"]}))

    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embedding_model)

    llm = HuggingFaceEndpoint(
        repo_id = "google/flan-t5-small", 
        temperature= 0.5, 
        max_new_tokens= 100
        )

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())
    query = "Which character has the most likes and is tagged as dominant?"
    response = qa_chain.invoke({"query": query})

    print("\nAnswer:", response)
