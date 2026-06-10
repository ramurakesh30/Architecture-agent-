class AIReviewService:

    def __init__(self, provider):

        self.provider = provider

    def generate_architecture_review(
        self,
        findings,
        knowledge_context=""
    ):

         return (
            self.provider
            .generate_architecture_review(
                findings,
                knowledge_context
            )
        )
    def ask(
        self,
        prompt
    ):

        return (
            self.provider
            .generate(
                prompt
            )
        )