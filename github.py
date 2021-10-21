import os
from distutils.dir_util import copy_tree
from git import Repo

new_branch = "new_branch"
# Get the current working directory
current_working_directory = os.getcwd()
parent_working_directory = os.path.abspath(
    os.path.join(current_working_directory, os.pardir)
)
# Clone
repo = Repo.clone_from(
    "https://github.com/atulnitkkr/Music-Player.git",
    f"{parent_working_directory}/initial_commit/",
    branch="master",
)

# Create new branch
repo.git.checkout("-b", new_branch)

src_dir = f"{current_working_directory}"
dest_dir = f"{parent_working_directory}/initial_commit/"

# getting all the files in the source directory
files = os.listdir(src_dir)
copy_tree(src_dir, dest_dir)
# Push new branch to remote
# subprocess.call(f"git push -u origin {nm_brnch}")

repo.git.add("--all")
repo.git.commit("-m", "Initial Commit")
repo.git.push("origin", new_branch)
