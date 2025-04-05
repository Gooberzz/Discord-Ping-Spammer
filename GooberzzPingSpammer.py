import os
import time
import requests
from pystyle import Colors, Colorate

green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
purple = "\033[1;35m"

os.system("title Gooberzz Ping Spam")

msg = "@everyone"

print("Gooberzz Ping Spammer")
print("")
WEBURL =  input("Enter webhook URL").strip()

def pinger(WEBURL):
    timeout = float(input("Enter the timeout delay in seconds: "))

    print(f"{yellow}Pings are starting.")

    try:
        print(f"{green}Spam pinger has attempted to start.")
        print("--------------------------------------------")
        while True:
            response = requests.post(WEBURL, json={"content": msg})
            if response.status_code == 429:
                retry_after = response.json().get("retry_after", timeout)
                print(f"{red}You have been rate limited. Trying again in {retry_after} seconds.")
                time.sleep(retry_after)
            else:
                response.raise_for_status()
                print(f"{green}Sent ping.")
                time.sleep(timeout)
    except Exception as err:
        print(f"{red}Error: {err}")
        input("")

os.system('cls' if os.name == 'nt' else 'clear')
pinger(WEBURL)