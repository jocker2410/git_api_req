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
      Fore.BLUE + f"Follow:\t\t\t{data['followers']}\n",
      Fore.LIGHTBLUE_EX + f"Followed:\t\t{data['following']}")
print(Fore.LIGHTMAGENTA_EX + 30 * "#")

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
repo_link = f"\n{url}/repos"
repo_resp = requests.get(repo_link)
repo_data = repo_resp.json()

print(Fore.CYAN + f"Repo Urls:")
for repo in repo_data:
    print(Fore.GREEN + repo['clone_url'])

