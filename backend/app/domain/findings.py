from enum import Enum
from dataclasses import dataclass


class Category(str, Enum):
    AVAILABILITY = "availability"
    SECURITY = "security"
    SCALABILITY = "scalability"
    COST = "cost"
    OBSERVABILITY = "observability"
    RELIABILITY = "reliability"


class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

SEVERITY_WEIGHTS = {
    Severity.LOW: 2,
    Severity.MEDIUM: 5,
    Severity.HIGH: 10,
    Severity.CRITICAL: 20
}


@dataclass
class Finding:
    category: Category
    severity: Severity
    message: str


@dataclass
class Recommendation:
    category: Category
    message: str