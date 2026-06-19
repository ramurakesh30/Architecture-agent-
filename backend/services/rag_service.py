class RAGService:
    def __init__(self, vector_store):

        self.vector_store = vector_store

    def enrich(self, findings):

        context = []

        for finding in findings:
            docs = self.vector_store.retrieve(finding.message)

            context.extend(docs)

        return "\n".join(context)
