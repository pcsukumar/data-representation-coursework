# This program will read a file from a repository and replace all the instances of the text "Andrew" with your 'Sukumar'.
# The program then commit those changes and push the file back to the repository.

import requests
from github import Github
from config import config as cfg

apikey = cfg["githubkey"] # Set the GitHub API key, importing from config.py file which is added in .gitignore

g = Github(apikey) # Create a GitHub client

# for repo in g.get_user().get_repos(): # Get all repositories by the user
#     print(repo.name)

repo =g.get_repo('pcsukumar/aprivateone') #Get the repository named 'aprivateone'

# print (repo.clone_url)

fileInfo = repo.get_contents("test.txt") # Get the contents of the file 'test.txt'
urlOfFile = fileInfo.download_url

#print(urlOfFile)  # Print the URL of the file

response = requests.get(urlOfFile) # Download the file's content
contentOfFile = response.text

#print(contentOfFile) # Print the contents of the file

# Replace all instances of 'Andrew' with 'Sukumar' in the content of the file
modifiedContent = contentOfFile.replace("Andrew", "Sukumar")

#print(modifiedContent) # Print the modified contents of the file


# Commit and push the file with the modified content into the respository
gitHubResponse = repo.update_file(fileInfo.path, "Replace all the instances of the text 'Andrew' with 'Sukumar'", modifiedContent, fileInfo.sha)

print(gitHubResponse) # Print the GitHub API response