

import os
current_dir = os.getcwd()
print(current_dir)

os.chdir("Location where you want to save cloned repo")

!git config --global user.email "youremail@gmail.com"
!git config --global user.name "yourname"
!git config --global user.password " dweiunf;oiwe!"

token ='yourtoken'
username = 'yourusername'
repo ='streamlit_app_git'

! git clone https://{token}@github.com/{username}/{repo}

# Commented out IPython magic to ensure Python compatibility.
# %cd streamlit_app_git

!git status

!git add --all #update index with current content in current repo

! git commit -a -m " Added files" # m - message -a all

!git remote -v # show url of alll remote repos

!git push origin main # push to remote repository and make changes in git hub

!git add --all