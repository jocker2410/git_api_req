from colorama import Fore, Style
import requests, datetime, os, sys


now = datetime.datetime.now()
Y = now.strftime("%Y")
M = now.strftime("%M")
# If no argument, then CVE and current year should be used as querry
arg = sys.argv[1] if len(sys.argv) > 1 else f"cve-{Y}"

uri = 'https://api.github.com/search/repositories'
params = {'q': arg}
os.system("clear")
os.system("cls")
print(Fore.GREEN + "[+] Start Connection")
resp = requests.get(uri, params=params)
js_resp = resp.json()

print(Fore.YELLOW + "[+] Sort items")
total_num = js_resp['total_count']
items = js_resp['items']
sorted_items = sorted(items, key=lambda x: x['html_url'].split('/')[4].lower())
print(Style.RESET_ALL)
for item in sorted_items: 
  y = item['pushed_at'].split('-')[0]
  m = item['pushed_at'].split('-')[1]
  last_update = item['pushed_at']
  
  if (y == Y ):
    url = item['html_url']
    print(f"Last Update: {last_update}\nUrl:\n{url}\n")
print(Fore.GREEN + f"Total: {total_num}")
