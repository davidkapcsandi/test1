import git

def clone_repository(repo_url, destination):
    try:
        git.Repo.clone_from(repo_url, destination)
        print(f"Repository cloned to {destination}")
    except Exception as e:
        print(f"Error cloning repository: {e}")

if __name__ == "__main__":
    repo_url = "https://github.com/davidkapcsandi/test1.git"
    destination = "/home/ec2-user/repo"
    clone_repository(repo_url, destination)
