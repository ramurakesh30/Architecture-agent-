from backend.app.domain.findings import (
    Finding,
    Recommendation,
    Category,
    Severity
)


class TerraformAgent:

    def analyze(
        self,
        tf,
        result
    ):

        if tf.public_s3_bucket:

            result.add_finding(
                Finding(
                    category=Category.SECURITY,
                    severity=Severity.CRITICAL,
                    message="Public S3 bucket detected"
                )
            )

            result.add_recommendation(
                Recommendation(
                    category=Category.SECURITY,
                    message="Restrict public access to S3"
                )
            )

        if tf.iam_wildcard_permissions:

            result.add_finding(
                Finding(
                    category=Category.SECURITY,
                    severity=Severity.CRITICAL,
                    message="IAM wildcard permissions detected"
                )
            )

        if tf.public_security_group:

            result.add_finding(
                Finding(
                    category=Category.SECURITY,
                    severity=Severity.HIGH,
                    message="Public security group detected"
                )
            )
        
        if tf.hardcoded_secrets:

            result.add_finding(
                Finding(
                    category=Category.SECURITY,
                    severity=Severity.CRITICAL,
                    message="Hardcoded secrets detected"
                )
            )

            result.add_recommendation(
                Recommendation(
                    category=Category.SECURITY,
                    message="Use AWS Secrets Manager or Vault"
                )
            )
        
        for port in tf.open_ingress_ports:

            result.add_finding(
                Finding(
                    category=Category.SECURITY,
                    severity=Severity.HIGH,
                    message=f"Sensitive port {port} exposed"
                )
            )
        
        if tf.public_load_balancer:

            result.add_finding(
                Finding(
                    category=Category.SECURITY,
                    severity=Severity.MEDIUM,
                    message="Public load balancer detected"
                )
            )
        
        if tf.public_ec2_instances:

            result.add_finding(
                Finding(
                    category=Category.SECURITY,
                    severity=Severity.HIGH,
                    message="Public EC2 instance detected"
                )
            )
        
        if tf.missing_tags:

            result.add_finding(
                Finding(
                    category=Category.RELIABILITY,
                    severity=Severity.LOW,
                    message="Resource tagging not detected"
                )
            )
        
        if tf.unencrypted_rds:

            result.add_finding(
                Finding(
                    category=Category.SECURITY,
                    severity=Severity.CRITICAL,
                    message="RDS encryption disabled"
                )
            )