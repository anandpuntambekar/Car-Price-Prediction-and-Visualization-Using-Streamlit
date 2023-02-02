'''
The purpose of this code is to interact with a remote Github repository. It starts by importing the os module to interact with the operating system, and then retrieves the current working directory. It then changes the current working directory to "/content/drive/MyDrive/Colab Notebooks/Streamlit_Demo/streamlit_app_git".

The user is then prompted to enter their Github email, username, password, and token. The code then pulls changes from the remote repository using the user's credentials. The git status command is used to check the status of the repository.

The code then stages all changes using the git add command, commits the changes with a message, and checks the URL of the remote repository using the git remote -v command. Finally, the code pushes the changes to the remote repository.
'''


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