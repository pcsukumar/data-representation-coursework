# This program will read a file from a repository and replace all the instances of the text "Andrew" with your 'Sukumar'.
# The program then commit those changes and push the file back to the repository.

import requests
import json
from config import config as cfg

filename = "repos-private.json"

url = 'https://api.github.com/repos/pcsukumar/aprivateone'

apikey = cfg["githubkey"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)