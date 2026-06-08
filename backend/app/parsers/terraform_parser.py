from app.domain.terraform import TerraformConfig



class TerraformParser:

    def parse(
        self,
        tf_content: str
    ):

        config = TerraformConfig()

        if '0.0.0.0/0' in tf_content:
            config.public_security_group = True

        if '"*"' in tf_content:
            config.iam_wildcard_permissions = True

        if 'aws_s3_bucket' in tf_content:
            if 'public-read' in tf_content:
                config.public_s3_bucket = True

        if 'kms_key_id' in tf_content:
            config.encryption_enabled = True

        SECRET_PATTERNS = [
            "password =",
            "secret =",
            "api_key =",
            "access_key ="
        ]

        for pattern in SECRET_PATTERNS:

            if pattern in tf_content.lower():

                config.hardcoded_secrets = True
        DANGEROUS_PORTS = [
            22,
            3389,
            3306,
            5432
        ]
        for port in DANGEROUS_PORTS:

            if f"from_port = {port}" in tf_content:

                config.open_ingress_ports.append(
                    port
                )   
        if "internal = false" in tf_content:

            config.public_load_balancer = True
        if (
            "associate_public_ip_address = true"
            in tf_content
        ):

            config.public_ec2_instances = True 
        if (
            "map_public_ip_on_launch = true"
            in tf_content
        ):

            config.public_subnet_usage = True   
        
        if "tags" not in tf_content:

            config.missing_tags = True
        if (
            "aws_db_instance"
            in tf_content
        ):

            if (
                "storage_encrypted = true"
                not in tf_content
            ):

                config.unencrypted_rds = True
                
        return config