import git

def commit_changes(repo_path, commit_message):
    try:
        repo = git.Repo(repo_path)
        repo.git.add(A=True)
        repo.index.commit(commit_message)
        print(f"Committed changes with message: {commit_message}")
    except Exception as e:
        print(f"Error committing changes: {e}")

if __name__ == "__main__":
    repo_path = "/home/ec2-user/repo"
    commit_message = "Update README with latest changes"
    commit_changes(repo_path, commit_message)
