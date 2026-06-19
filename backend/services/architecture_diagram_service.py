class ArchitectureDiagramService:
    def generate(self, summary):

        lines = []

        lines.append("graph TD")

        #
        # External traffic
        #

        if summary.has_ingress:
            lines.append("Internet --> Ingress")

            lines.append("Ingress --> Application")

        else:
            lines.append("Internet --> Application")

        #
        # Kubernetes
        #

        lines.append(
            f"Application --> Deployments[{summary.total_deployments} Deployments]"
        )

        lines.append(f"Deployments --> Replicas[{summary.total_replicas} Replicas]")

        #
        # Scaling
        #

        if summary.uses_hpa:
            lines.append("HPA --> Deployments")

        #
        # Cloud resources
        #

        if summary.public_s3_buckets > 0:
            lines.append("Application --> S3")

        #
        # Security
        #

        if summary.public_security_groups > 0:
            lines.append("Internet --> SecurityGroup")

            lines.append("SecurityGroup --> Application")

        return "\n".join(lines)
