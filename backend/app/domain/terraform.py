from typing import List

from pydantic import BaseModel


class TerraformConfig(BaseModel):
    public_s3_bucket: bool = False

    encryption_enabled: bool = False

    iam_wildcard_permissions: bool = False

    public_security_group: bool = False

    hardcoded_secrets: bool = False

    public_load_balancer: bool = False

    unencrypted_rds: bool = False

    missing_tags: bool = False

    open_ingress_ports: List[int] = []

    public_ec2_instances: bool = False

    public_subnet_usage: bool = False
