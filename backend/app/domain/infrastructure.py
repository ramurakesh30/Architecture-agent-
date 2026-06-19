from dataclasses import dataclass, field


@dataclass
class InfrastructurePackage:
    kubernetes_configs: list = field(default_factory=list)

    terraform_configs: list = field(default_factory=list)
