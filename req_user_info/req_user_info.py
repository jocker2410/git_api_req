from colorama import Fore, Style
import requests
import json
import sys

def acces_data(url):
    try:
        resp = requests.get(url)
        data = resp.json()
        return data
    except Exception as e:
        print(Fore.RED + f"[-] Site {url} can't be reached.\nError:{resp.status_code}")
        exit()
def get_user_data(site, user):
    url = f"{site}/users/{user}"
    data = acces_data(url)
    print(Fore.GREEN + f"User:\t\t\t{data['login']}\n",
          Fore.YELLOW + f"Repos:\t\t\t{data['public_repos']}\n",
          Fore.BLUE + f"Follow:\t\t{data['followers']}\n",
          Fore.LIGHTBLUE_EX + f"Followed:\t\t{data['following']}")
def get_contacts(site):
    url = f"{site}/followers"
    follower_data = acces_data(url)
    print(Fore.CYAN +"\nFollowers:")
    for follow in follower_data:
        print(Fore.GREEN + follow['login'])
    url = f"{site}/following"
    folowing_data = acces_data(url)
    print(Fore.CYAN + "\nFollowing:")
    for folowing in folowing_data:
        print(Fore.GREEN + folowing['login'])
def get_repo_data(site):
    url = f"{site}/repos"
    repo_data = acces_data(url)
    print(Fore.CYAN + f"\nRepo Urls:")
    for repo in repo_data:
        print(Fore.GREEN + repo['clone_url'])
    comm_num = 0
    for repo in repo_data:
        repo_name = repo['name']
        url = f"{site}/repos/{repo['name']}/commits"
        commit_data = acces_data(url)
        print(Fore.YELLOW + f"\nCommits for {repo['name']}\n")
        n=0
        for commit in commit_data:
            n += 1
            print(Fore.GREEN + f"Committer:\t" + Fore.LIGHTYELLOW_EX + f"{commit['commit']['committer']['name']}\n",
                  Fore.GREEN + f"E-Mail:\t" + Fore.LIGHTYELLOW_EX + f"{commit['commit']['committer']['email']}\n",
                  Fore.GREEN + f"Update date:\t" + Fore.LIGHTYELLOW_EX + f"{commit['commit']['committer']['date']}\n",
                  Fore.GREEN + f"Message:\t" + Fore.LIGHTYELLOW_EX + f"{commit['commit']['message']}\n")
        print(Style.BRIGHT + Fore.MAGENTA + f"{n} commints found for {repo['name']}")
        comm_num += n
    print(Fore.GREEN + "Found " + Fore.LIGHTYELLOW_EX + f"{comm_num}" + Fore.GREEN + " comments for " + Fore.LIGHTYELLOW_EX + f"{commit_data['login']}")
def clear_screen():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

def main():
    clear_screen()
    user = sys.argv[1] if len(sys.argv) > 1 else f"jocker2410"
    site = "https://api.github.com"
    #get_user_data(site, user)
    get_contacts(f"{site}/users/{user}")
    get_repo_data(f"{site}/users/{user}")



    Style.RESET_ALL

if __name__ == '__main__':
    main()