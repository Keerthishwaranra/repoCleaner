from github import Github, GithubException
from retrying import retry

class GitHubClient:
    def __init__(self, token):
        self.github = Github(token)

    @retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000, wait_exponential_max=10000)
    def get_repo(self, repo_name):
        return self.github.get_repo(repo_name)

    @retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000, wait_exponential_max=10000)
    def get_branches(self, repo):
        return repo.get_branches()

    @retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000, wait_exponential_max=10000)
    def delete_branch(self, repo, branch_name):
        ref = repo.get_git_ref(f"heads/{branch_name}")
        ref.delete()