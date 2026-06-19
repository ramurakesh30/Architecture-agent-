from typing import List, Optional

from pydantic import BaseModel


class KubernetesConfig(BaseModel):
    replicas: int = 1
    has_liveness_probe: bool = False
    has_readiness_probe: bool = False
    cpu_limit: bool = False
    memory_limit: bool = False


class TerraformConfig(BaseModel):
    public_s3_bucket: bool = False
    encryption_enabled: bool = True
    iam_wildcard_permissions: bool = False


class CloudConfig(BaseModel):
    autoscaling_enabled: bool = False
    estimated_monthly_cost: int = 0


class ArchitectureRequest(BaseModel):
    services: List[str]

    database: Optional[str] = None

    replicas: int = 1

    public_api: bool = False

    kubernetes: Optional[KubernetesConfig] = None

    terraform: Optional[TerraformConfig] = None

    cloud: Optional[CloudConfig] = None


class ArchitectureResponse(BaseModel):
    review_id: str
    status: str


class ArchitectureResult(BaseModel):
    review_id: str
    findings: list[str]
    recommendations: list[str]
