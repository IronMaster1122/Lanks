import getpass
from colorama import Fore, init
import time
import requests
import sys

init()

user = getpass.getuser()

print(Fore.RED + "                                              _                     _         ")
time.sleep(0.3)
print(Fore.RED + "                                             | |                   | |        ")
time.sleep(0.3)
print(Fore.RED + "                                             | |       __ _  _ __  | | __ ___ ")
time.sleep(0.3)
print(Fore.RED + "                                             | |      / _` || '_ \ | |/ // __|")
time.sleep(0.3)
print(Fore.RED + "                                             | |____ | (_| || | | ||   < \__ |")
time.sleep(0.3)
print(Fore.RED + "                                             |______| \__,_||_| |_||_|\_\|___/\n\n")
time.sleep(0.3)

print(Fore.RED + f"                                                    Welcome to Lanks, {user}\n")
time.sleep(0.3)
print(Fore.RED + f"                                                         I want to start!")
site = input(Fore.RED + "Input site: ")
packets = int(input(Fore.RED + "Input packets: "))  
delay = float(input(Fore.RED + "Input delay (seconds): "))  

for _ in range(packets):
    response = requests.get(site)
    if response.status_code == 200:
        print(f"Send to {site} packet! ms={response.elapsed.total_seconds()}")
    else:
        print("Error...")
    
    time.sleep(delay)
