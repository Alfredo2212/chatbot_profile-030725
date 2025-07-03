import json
from dotenv import load_dotenv
from langchain.docstore.document import Document

import os 

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

  
