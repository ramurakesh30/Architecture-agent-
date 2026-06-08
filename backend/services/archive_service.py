import zipfile
import tempfile
import os


class ArchiveService:

    def extract(
        self,
        zip_path
    ):

        temp_dir = tempfile.mkdtemp()

        with zipfile.ZipFile(
            zip_path,
            "r"
        ) as zip_ref:

            zip_ref.extractall(
                temp_dir
            )

        return temp_dir