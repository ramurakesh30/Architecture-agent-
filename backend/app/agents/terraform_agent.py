from app.domain.findings import (
    Finding,
    Recommendation,
    Category,
    Severity
)


class TerraformAgent:

    def analyze(self, request, result):

        if request.terraform is None:
            return

        tf = request.terraform

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
                    message="Restrict public access"
                )
            )

        if not tf.encryption_enabled:


            result.add_finding(
                Finding(
                    category=Category.SECURITY,
                    severity=Severity.HIGH,
                    message="Storage encryption disabled"
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