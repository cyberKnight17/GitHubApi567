import requests


def get_repo_list(github_id):
    response = requests.get(f"https://api.github.com/users/{github_id}/repos")
    repo_list = []
    for repo_info in response.json():
        repo_list.append(repo_info['name'])
    return repo_list


def get_com_num(github_id, repo_name):
    response = requests.get(f"https://api.github.com/repos/{github_id}/{repo_name}/commits")
    return len(response.json())


def main(github_id):
    for repository in get_repo_list(github_id):
        print(f"{repository}: {get_com_num(github_id, repository)}")