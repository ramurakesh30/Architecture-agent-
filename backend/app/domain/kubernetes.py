from dataclasses import dataclass, field


@dataclass
class KubernetesConfig:
    replicas: int = 1

    container_count: int = 0

    has_liveness_probe: bool = False

    has_readiness_probe: bool = False

    cpu_limit: bool = False

    memory_limit: bool = False

    cpu_request: bool = False

    memory_request: bool = False

    has_ingress: bool = False

    has_hpa: bool = False

    has_security_context: bool = False

    has_node_selector: bool = False

    has_affinity_rules: bool = False

    has_tolerations: bool = False

    namespaces: list = field(default_factory=list)

    image_tags: list = field(default_factory=list)
