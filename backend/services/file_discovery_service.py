import os


class DiscoveryService:

    def discover(
        self,
        directory: str
    ):

        files = []

        for root, _, filenames in os.walk(
            directory
        ):

            for file in filenames:

                files.append(
                    os.path.join(
                        root,
                        file
                    )
                )

        return files