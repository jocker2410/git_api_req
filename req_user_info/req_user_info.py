from colorama import Fore, Style
import requests
import json

user = "jocker2410"
# get user data
url = f"https://api.github.com/users/{user}"
resp = requests.get(url)
data = resp.json()

print(Fore.GREEN + f"User:\t\t\t{data['login']}\n",
      Fore.YELLOW + f"Repos:\t\t\t{data['public_repos']}\n",
      Fore.BLUE + f"Follow:\t\t{data['followers']}\n",
      Fore.LIGHTBLUE_EX + f"Followed:\t\t{data['following']}")

# get contacts
follower_link = f"{url}/followers"
follower_resp = requests.get(follower_link)
follower_data = follower_resp.json()
print(Fore.CYAN +"\nFollowers:")
for follow in follower_data:
    print(Fore.GREEN + follow['login'])
folowing_link = f"{url}/following"
folowing_resp = requests.get(folowing_link)
folowing_data = folowing_resp.json()
print(Fore.CYAN + "\nFollowing:")
for folowing in folowing_data:
    print(Fore.GREEN + folowing['login'])

# get repo data
repo_link = f"{url}/repos"
repo_resp = requests.get(repo_link)
repo_data = repo_resp.json()

print(Fore.CYAN + f"\nRepo Urls:")
for repo in repo_data:
    print(Fore.GREEN + repo['clone_url'])
print("")
# get Commits
for repo in repo_data:
    repo_name = repo['name']
    commit_url = f"{url.replace('users', 'repos')}/{repo['name']}/commits"
    commit_data = requests.get(commit_url).json()
    print(Fore.YELLOW + f"\nCommits for {repo['name']}\n")
    n=0
    for commit in commit_data:
        n =+1
        print(Fore.GREEN + f"Committer:\t" + Fore.LIGHTYELLOW_EX + f"{commit['commit']['committer']['name']}",
              Fore.GREEN + f"E-Mail:\t" + Fore.LIGHTYELLOW_EX + f"{commit['commit']['committer']['email']}",
              Fore.GREEN + f"Update date:\t" + Fore.LIGHTYELLOW_EX + f"{commit['commit']['committer']['date']}",
              Fore.GREEN + f"Message:\t" + Fore.LIGHTYELLOW_EX + f"{commit['commit']['message']}\n")
    print(Style.DIM + Fore.MAGENTA + f"{n} commints found for {repo['name']}")
    Style.RESET_ALL
