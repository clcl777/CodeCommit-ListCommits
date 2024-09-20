from CodeCommitListCommits import CodeCommitListCommits


def main():
    username = "xxxxxxx"
    password = "xxxxxxx"
    region = "ap-northeast-1"
    repository_name = "repository_name"

    list_commits = CodeCommitListCommits(username, password, region)
    commits = list_commits.list_commits(repository_name)
    print(commits)


if __name__ == "__main__":
    main()
