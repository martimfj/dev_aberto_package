import requests


def hello():
    response = requests.get('https://api.github.com/repos/insper/dev-aberto/commits')
    commit_info = response.json()[0]['commit']['author']
    return commit_info['date'], commit_info['name']
