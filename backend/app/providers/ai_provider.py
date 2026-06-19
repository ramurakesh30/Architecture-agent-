from abc import ABC, abstractmethod


class AIProvider(ABC):
    @abstractmethod
    def generate_architecture_review(self, findings):
        pass

    @abstractmethod
    def generate(self, prompt):
        pass
