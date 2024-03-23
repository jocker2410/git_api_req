from colorama import Fore, Style
import requests, datetime, os, sys

uri = 'https://api.github.com/search/repositories'
now = datetime.datetime.now()
Y = now.strftime("%Y")
M = now.strftime("%m")
# If no argument, then use CVE- and current year as querry
arg = sys.argv[1] if len(sys.argv) > 1 else f"cve-{Y}"
params = {'q': arg}
def clear_screen():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")
def get_connectio(uri, params):
  print(Fore.GREEN + "[+] Start Connection")
  try:
    resp = requests.get(uri, params=params)
  except Exception as ex:
    print("Connection Error to api.github.com")
    print(Fore.RED + f"[!] Status code: {resp.status_code}")
  return resp
def get_data(resp):
  js_resp = resp.json()
  print(Fore.YELLOW + "[+] Sort items")
  total_num = js_resp['total_count']
  items = js_resp['items']
  sorted_items = sorted(items, key=lambda x: x['html_url'].split('/')[4].lower())
  return sorted_items, total_num
def display_data(sorted_items, total_num, Y, M):
  for item in sorted_items:
    y = item['pushed_at'].split('-')[0]
    m = item['pushed_at'].split('-')[1]
    last_update = item['pushed_at']

    if (y == Y or m == M ):
      url = item['html_url']
      print(f"Last Update: {last_update}\nUrl:\n{url}\n")
  print(Fore.GREEN + f"Total: {total_num}")
  print(Style.RESET_ALL)

def main():
  clear_screen()
  resp =  get_connectio(uri, params)
  sorted_items, total_num = get_data(resp=resp)
  display_data(sorted_items, total_num, Y, M)

if __name__ == "__main__":
  main()