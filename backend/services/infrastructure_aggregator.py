from app.domain.infrastructure_summary import InfrastructureSummary


class InfrastructureAggregator:
    def summarize(self, package):

        summary = InfrastructureSummary()

        summary.total_deployments = len(package.kubernetes_configs)

        for k8s in package.kubernetes_configs:
            summary.total_replicas += k8s.replicas

            if k8s.has_hpa:
                summary.uses_hpa = True

            if k8s.has_ingress:
                summary.has_ingress = True

        for tf in package.terraform_configs:
            if tf.public_security_group:
                summary.public_security_groups += 1

            if tf.public_s3_bucket:
                summary.public_s3_buckets += 1

        return summary
