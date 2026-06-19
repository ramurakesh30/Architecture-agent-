from dataclasses import dataclass


@dataclass
class InfrastructureSummary:
    total_deployments: int = 0

    total_replicas: int = 0

    public_security_groups: int = 0

    public_s3_buckets: int = 0

    uses_hpa: bool = False

    has_ingress: bool = False
