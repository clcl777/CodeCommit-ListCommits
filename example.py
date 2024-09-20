from CodeCommitListCommits import CodeCommitListCommits


def main():
    USERNAME = "xxxxxxx"
    PASSWORD = "xxxxxxx"
    region = "ap-northeast-1"
    repository_name = "repository_name"

    list_commits = CodeCommitListCommits(USERNAME, PASSWORD, region)
    commits_main = list_commits.list_commits(repository_name)
    print(commits_main)
    commits_branch1 = list_commits.list_commits(repository_name, "branch1")
    print(commits_branch1)


if __name__ == "__main__":
    main()
