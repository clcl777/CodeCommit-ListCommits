![Welcome PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![MIT license](https://img.shields.io/github/license/hermgerm29/qdbg?color=blue)

# CodeCommit-ListCommits

CodeCommit-ListCommitsは、Dulwichライブラリを使用してAWS CodeCommitリポジトリからコミット履歴を取得するためのPythonライブラリです。boto3ではリポジトリから全てのコミットを一括で取得することができませんが、このライブラリを使用すると、リポジトリをクローンして全てのコミット情報を一括で抽出でき、効率的にコミット履歴を分析することができます。

## 特徴

- **コミットの一括取得:** 特定のリポジトリから全てのコミットを一括で取得可能
- **ブランチの指定:** デフォルトブランチまたは指定されたブランチからコミットを取得可能
- **セキュアなリポジトリクローン:** HTTPS認証情報を使用してAWS CodeCommitリポジトリを安全にクローン
- **自動クリーンアップ:** 処理が完了した後、ローカル環境からクローンしたリポジトリを自動的に削除し、ファイルを残さない

## デモ

```Python
from CodeCommitListCommits import CodeCommitListCommits

USERNAME = "xxxxxxx"
PASSWORD = "xxxxxxx"
region = "ap-northeast-1"
repository_name = "repository_name"

# デフォルトブランチからコミットを取得
client = CodeCommitListCommits(USERNAME, PASSWORD, region)
commits_default = client.list_commits(repository_name)
print(commits_default)

# 特定のブランチ（例: "branch1"）からコミットを取得
commits_branch1 = client.list_commits(repository_name, "branch1")
print(commits_branch1)
```

## CodeCommitのHTTPS Git認証情報の生成

1. AWS Management Consoleにログイン
1. 「セキュリティ認証情報」から「AWS CodeCommit認証情報」を選択
1. 「AWS CodeCommitのHTTPS Git 認証情報」の中の「認証情報を生成」をクリックし、ユーザー名とパスワードを作成
1. 生成されたユーザー名とパスワードを保存。これらはリポジトリをクローンするときに使用される。

## Requirements

- `dulwich` ライブラリ
- AWS CodeCommit 認証情報