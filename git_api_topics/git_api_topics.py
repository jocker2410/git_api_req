from colorama import Fore, Style
import requests, datetime, os, sys

uri = 'https://api.github.com/search/repositories'
now = datetime.datetime.now()

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
  print(Fore.YELLOW + "[+] Sort items\n")
  total_num = js_resp['total_count']
  items = js_resp['items']
  # Sorted by project name
  sorted_items = sorted(items, key=lambda x: x['html_url'].split('/')[4].lower())
  print(Fore.YELLOW + "[+] Sucessfully sorted\n\n")
  return sorted_items, total_num
def display_data(sorted_items, total_num, Y, M):
  for item in sorted_items:
    y = item['pushed_at'].split('-')[0]
    m = item['pushed_at'].split('-')[1]
    last_update = item['pushed_at']
    # Show only results that have been updated on this year or month
    if (y == Y or m == M ):
      url = item['html_url']
      user = item['html_url'].split('/')[3]
      repo = item['html_url'].split('/')[4]
      print(f"Creator:\t{user}\n"
            f"Repository:\t{repo}\n"
            f"Last Update:\t{last_update}\n"
            f"Url:\t{url}\n")
  print(Fore.GREEN + f"Total: {total_num}")
  print(Style.RESET_ALL)

def main():
  Y = now.strftime("%Y")
  M = now.strftime("%m")
  # If no argument, then use CVE- and current year as querry
  arg = sys.argv[1] if len(sys.argv) > 1 else f"cve-{Y}"
  params = {'q': arg}

  clear_screen()
  resp =  get_connectio(uri, params)
  sorted_items, total_num = get_data(resp=resp)
  display_data(sorted_items, total_num, Y, M)

if __name__ == "__main__":
  main()