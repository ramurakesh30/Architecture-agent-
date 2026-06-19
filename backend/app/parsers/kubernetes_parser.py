import yaml
from app.domain.kubernetes import KubernetesConfig


class KubernetesParser:
    def parse(self, yaml_content: str) -> KubernetesConfig:

        config = KubernetesConfig()

        documents = list(yaml.safe_load_all(yaml_content))

        for doc in documents:
            if not doc:
                continue

            kind = doc.get("kind")

            if kind == "Deployment":
                self._parse_deployment(doc, config)

            elif kind == "Ingress":
                config.has_ingress = True

            elif kind == "HorizontalPodAutoscaler":
                config.has_hpa = True

        return config

    def _parse_deployment(self, deployment, config: KubernetesConfig):

        spec = deployment.get("spec", {})

        config.replicas = spec.get("replicas", 1)

        containers = spec.get("template", {}).get("spec", {}).get("containers", [])
        config.container_count = len(containers)

        metadata = deployment.get("metadata", {})

        namespace = metadata.get("namespace")

        if namespace:
            config.namespaces.append(namespace)

        pod_spec = spec.get("template", {}).get("spec", {})

        if pod_spec.get("nodeSelector"):
            config.has_node_selector = True
        if pod_spec.get("affinity"):
            config.has_affinity_rules = True
        if pod_spec.get("tolerations"):
            config.has_tolerations = True

        for container in containers:
            image = container.get("image", "")

            if ":" in image:
                tag = image.split(":")[-1]

            else:
                tag = "latest"

            config.image_tags.append(tag)

            if "livenessProbe" in container:
                config.has_liveness_probe = True

            if "readinessProbe" in container:
                config.has_readiness_probe = True

            resources = container.get("resources", {})

            limits = resources.get("limits", {})
            requests = resources.get("requests", {})
            if "cpu" in limits:
                config.cpu_limit = True

            if "memory" in limits:
                config.memory_limit = True

            if "cpu" in requests:
                config.cpu_request = True

            if "memory" in requests:
                config.memory_request = True

            security_context = container.get("securityContext")

            if security_context:
                config.has_security_context = True
