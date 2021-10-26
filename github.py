import os
from distutils.dir_util import copy_tree
from git import Repo

# from function import clone_repo, create_branch, copy_dir_to_repo, push_repo

new_branch = "xyz"
repo_url = "https://github.com/atulnitkkr/Music-Player.git"
# # Get the current working directory
current_working_directory = os.getcwd()
parent_working_directory = os.path.abspath(
    os.path.join(current_working_directory, os.pardir)
)

repo_name = repo_url.split(".git")[0].split("/")[-1]
# Clone
repo = Repo.clone_from(
    repo_url,
    os.path.join(parent_working_directory, repo_name),
    branch="master",
)
# print(type(repo))
# print(repo)

# Create new branch
repo.git.checkout("-b", new_branch)

src_dir = f"{current_working_directory}"
dest_dir = os.path.join(parent_working_directory, repo_name)

# # getting all the files in the source directory
# files = os.listdir(src_dir)
# for file in files:
#     src = os.path.join(src_dir, file)
#     dest = os.path.join(dest_dir, file)
#     if file != repo_name:
#         shutil.copy2(src, dest)
copy_tree(src_dir, dest_dir)
# shutil.copytree(src_dir, dest_dir, ignore=shutil.ignore_patterns(repo_name))
# # Push new branch to remote
# # subprocess.call(f"git push -u origin {nm_brnch}")

repo.git.add("--all")
repo.git.commit("-m", "Initial Commit")
# repo.git.push("origin", new_branch)
# init_repo = True
# repo = clone_repo(repo_url, parent_working_directory)
status, out, err = repo.git.push("origin", new_branch, with_extended_output=True)
if status == 0:
    print(err)
else:
    print("Git push completed")
# init_repo =
