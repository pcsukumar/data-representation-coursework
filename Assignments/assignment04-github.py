# This program will read a file from a repository and replace all the instances of the text "Andrew" with your 'Sukumar'.
# The program then commit those changes and push the file back to the repository.

from github import Github
from config import config as cfg

apikey = cfg["githubkey"]

g = Github(apikey)

# for repo in g.get_user().get_repos():
#     print(repo.name)

repo =g.get_repo('pcsukumar/aprivateone')

print (repo.clone_url)




