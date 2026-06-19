import os

import chromadb
from sentence_transformers import SentenceTransformer

from backend.app.config.settings import Settings


class VectorStoreService:
    def __init__(self):

        self.model = SentenceTransformer(Settings.EMBEDDING_MODEL)

        self.client = chromadb.PersistentClient(path="./chroma_db")

        self.collection = self.client.get_or_create_collection("architecture_knowledge")

    def index_documents(self):

        knowledge_path = "backend/knowledge"

        for file_name in os.listdir(knowledge_path):
            text = open(
                os.path.join(knowledge_path, file_name), encoding="utf-8"
            ).read()

            embedding = self.model.encode(text).tolist()

            self.collection.add(
                ids=[file_name], documents=[text], embeddings=[embedding]
            )

    def retrieve(self, query):

        embedding = self.model.encode(query).tolist()

        result = self.collection.query(query_embeddings=[embedding], n_results=3)

        return result["documents"][0]
