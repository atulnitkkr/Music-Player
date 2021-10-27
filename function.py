import os
from distutils.dir_util import copy_tree
from git import Repo


def clone_repo(repo_url, parent_working_directory):
    try:
        repo_name = repo_url.split(".git")[0].split("/")[-1]
        repo = Repo.clone_from(
            repo_url,
            os.path.join(parent_working_directory, repo_name),
            branch="master",
        )
        return repo , True
    except Exception as e:
        

def create_branch(repo,new_branch):
    repo.git.checkout("-b", new_branch)
    pass

def copy_dir_to_repo(current_working_directory,parent_working_directory,repo_url):
    repo_name = repo_url.split(".git")[0].split("/")[-1]
    src_dir = f"{current_working_directory}"
    dest_dir = os.path.join(parent_working_directory, repo_name)
    copy_tree(src_dir, dest_dir)
    pass

def push_repo(repo,new_branch):
    repo.git.add("--all")
    repo.git.commit("-m", "Initial Commit")
    repo.git.push("origin", new_branch)
    pass
