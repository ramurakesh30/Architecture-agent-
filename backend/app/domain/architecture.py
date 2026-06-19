from dataclasses import dataclass


@dataclass
class Finding:
    category: str
    severity: str
    message: str


@dataclass
class Recommendation:
    category: str
    message: str
