import requests,time,os

from colorama import Fore

print(f'''{Fore.CYAN}

  __  __                                   _       _                _   _               
 |  \/  | ___  ___ ___  __ _  __ _  ___   / \   __| |_   _____ _ __| |_(_)___  ___ _ __ 
 | |\/| |/ _ \/ __/ __|/ _` |/ _` |/ _ \ / _ \ / _` \ \ / / _ \ '__| __| / __|/ _ \ '__|
 | |  | |  __/\__ \__ \ (_| | (_| |  __// ___ \ (_| |\ V /  __/ |  | |_| \__ \  __/ |   
 |_|  |_|\___||___/___/\__,_|\__, |\___/_/   \_\__,_| \_/ \___|_|   \__|_|___/\___|_|   
                             |___/                                                      

{Fore.RESET}\n{Fore.GREEN}Made by {Fore.LIGHTRED_EX}cashflow#1337\n''')


msg_one = open("data/message.txt", "r", encoding="utf-8").read()
message = msg_one.replace("\\n", "\n")
token = open("data/token.txt", "r").read()
ids = open("data/channelids.txt", "r").readlines()
os.system(f'title MessageAdvertiser')


print(f"{Fore.GREEN}Message: \n{Fore.CYAN}{message}{Fore.RESET}")
print(f"{Fore.GREEN}Loaded channel ids:\n{Fore.CYAN}{len(ids)}{Fore.RESET}")

delay = int(input("\nDelay between each message in seconds (recommend 3 or higher): " + Fore.CYAN))
sleeptime = int(input(Fore.RESET + "Delay before sending a new wave of messages in seconds (3600 for 1 hour): " + Fore.CYAN))
sleeptimer = str(sleeptime)


print("\n")

def sendMessage(token, id, message):
    url = 'https://discord.com/api/v10/channels/{}/messages'.format(id)
    data = {"content": message}
    header = {"authorization": token}

    r = requests.post(url, data, headers=header)
    if r.status_code == 200:
        print(Fore.GREEN + "[Success] Message sent to " + Fore.CYAN + format(id))
    else:
        print(Fore.RED + "[Failed] Could not send message to " + Fore.CYAN + format(id) + Fore.RED + "\n[Error] Error code " + str(r.status_code))

    

while True:
    for id in ids:
        newId = id.strip()
        if newId != '':
            sendMessage(token, newId, message)
            time.sleep(delay)
    print(f"{Fore.YELLOW}[Info] Sleeping {Fore.CYAN}{sleeptimer} {Fore.YELLOW}seconds")
    time.sleep(sleeptime)