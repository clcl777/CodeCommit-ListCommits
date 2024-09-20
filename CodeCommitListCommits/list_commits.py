import os
import shutil
import time

from dulwich.objects import Commit
from dulwich.porcelain import clone
from dulwich.repo import Repo
from dulwich.walk import Walker


class RepositoryCloneError(Exception):
    pass


class RepositoryOpenError(Exception):
    pass


class CodeCommitListCommits:
    def __init__(self, username: str, password: str, region: str, target_dir: str = "./tmp"):
        self.username = username
        self.password = password
        self.region = region
        self.target_dir = target_dir

    def _clone_repository(self) -> None:
        """Clone the repository to the target directory."""
        repo_url = f"https://git-codecommit.{self.region}.amazonaws.com/v1/repos/{self.repository_name}"
        if os.path.exists(self.target_dir):
            shutil.rmtree(self.target_dir)
        try:
            clone(repo_url, target=self.target_dir, username=self.username, password=self.password)
        except Exception as e:
            raise RepositoryCloneError(f"Failed to clone repository: {e}")

    def _delete_repository(self) -> None:
        """Delete the cloned repository."""
        if os.path.exists(self.target_dir):
            shutil.rmtree(self.target_dir)

    def _extract_commit_details(self, commit: Commit) -> dict[str, str | list[str]]:
        """Extract details from a commit."""
        committer_name, committer_email = commit.committer.decode("utf-8").split("<")
        author_name, author_email = commit.author.decode("utf-8").split("<")
        return {
            "commit_id": commit.id.decode("utf-8"),
            "tree_id": commit.tree.decode("utf-8"),
            "parent_ids": [parent.decode("utf-8") for parent in commit.parents],
            "author_name": author_name.strip(),
            "author_email": author_email.strip(">"),
            "author_date": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(commit.commit_time)),
            "committer_name": committer_name.strip(),
            "committer_email": committer_email.strip(">"),
            "commit_date": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(commit.commit_time)),
            "timezone_offset": commit.commit_timezone,
            "message": commit.message.decode("utf-8"),
        }

    def list_commits(self, repository_name: str, branch_name: str | None = None) -> list[dict[str, str | list[str]]]:
        self.repository_name = repository_name
        try:
            self._clone_repository()
            repo = Repo(self.target_dir)
            refs = repo.get_refs()
            if branch_name:
                branch_ref = f"refs/remotes/origin/{branch_name}".encode("utf-8")
                if branch_ref not in refs:
                    raise ValueError(f"Branch '{branch_name}' not found in the repository.")
                walker = Walker(repo, [refs[branch_ref]])
            else:
                walker = Walker(repo, [repo.head()])
            commits_list = [self._extract_commit_details(entry.commit) for entry in walker]
        except Exception as e:
            raise RepositoryOpenError(f"Failed to open repository: {e}")
        finally:
            self._delete_repository()
        return commits_list
