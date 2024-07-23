import os
import sys
import subprocess

def clone_repo(repo_url, target_dir):
    try:
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        subprocess.run(['git', 'clone', repo_url, target_dir], check=True)
        print(f"Repository cloned successfully into {target_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")

if __name__ == "__main__":
    repo_url = 'https://github.com/davidkapcsandi/test1.git'
    target_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    clone_repo(repo_url, target_dir)

