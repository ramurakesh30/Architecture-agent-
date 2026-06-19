import shutil
import tempfile

from git import Repo


class GithubService:
    def clone_repository(self, repo_url: str):

        temp_dir = tempfile.mkdtemp()

        Repo.clone_from(repo_url, temp_dir)

        return temp_dir

    def cleanup(self, path: str):

        shutil.rmtree(path, ignore_errors=True)
