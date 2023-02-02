
## Import os module to interact with the operating system
import os
current_dir = os.getcwd()
print(current_dir)
os.chdir("/content/drive/MyDrive/Colab Notebooks/Streamlit_Demo/streamlit_app_git")


## Set the global Git user email, name, and password
!git config --global user.email "youremail@gmail.com"
!git config --global user.name "yourusername"
!git config --global user.password "yourpassword!"

## Set the global Git user email, name, and password
token ='yourusetoken'
username = 'yourusername'
repo ='streamlit_app_git'

## Clone / Pull from the remote repository
#! git clone https://{token}@github.com/{username}/{repo}
! git pull https://{token}@github.com/{username}/{repo}

!git status


# Update the index with all changes in the current repository
!git add --all 

! git commit -a -m " Added files" # m - message -a all

!git remote -v # show url of alll remote repos


#! git config --global --unset-all credential.helper

# Push changes to the remote repository
#!git push origin main # push to remote repository and make changes in git hub
! git push https://{token}@github.com/{username}/{repo}