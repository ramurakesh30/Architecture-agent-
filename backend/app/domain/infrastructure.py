from dataclasses import dataclass, field
from typing import Optional

from app.domain.kubernetes import KubernetesConfig
from app.domain.terraform import TerraformConfig


@dataclass
class InfrastructurePackage:

    kubernetes_configs: list = field(
        default_factory=list
    )

    terraform_configs: list = field(
        default_factory=list
    )