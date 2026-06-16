from pydantic import BaseModel


class GithubRepositoryRequest(
    BaseModel
):

    repository_url: str