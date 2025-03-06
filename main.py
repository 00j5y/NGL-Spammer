import requests
import keyboard
import time
import random
import string
from colorama import Fore, init

init() #Initialise les couleurs de colorama 

def deviceId():
    char = string.ascii_lowercase + string.digits

    part1 = ''.join(random.choices(char, k=8))
    part2 = ''.join(random.choices(char, k=4))
    part3 = ''.join(random.choices(char, k=4))
    part4 = ''.join(random.choices(char, k=4))
    part5 = ''.join(random.choices(char, k=12))

    return f"{part1}-{part2}-{part3}-{part4}-{part5}"

def userAgent():
    with open("user-agents.txt", "r") as file:
        lines = file.readlines()
    return random.choice(lines).strip()

def main():
    print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] NGL Link Spammer / Credit : @00j5y")
    print("")
    print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Press 'space' to start")
    keyboard.wait('space')  
    time.sleep(0.1)
    print("")

    ngluser = input(f"{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] NGL Username ? :").strip() 
    while True:
        try:
            number = int(input(f"{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] How many messages? :"))  # Convertir en int
            break
        except ValueError: # Si il y a une erreur
            print("")
            print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Please enter a valid number.")

    message = input(f"{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] Message ? :")  
    print("")

    sucess = 0
    fail = 0
    while sucess < number:
        headers = {
            'Host': 'ngl.link',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': f'{userAgent()}',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://ngl.link',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://ngl.link/{ngluser}',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
            'username': f'{ngluser}',
            'question': f'{message}',
            'deviceId': f'{deviceId()}',
            'gameSlug': '',
            'referrer': '',
        }


        response = requests.post('https://ngl.link/api/submit', headers=headers, data=data)
        if response.status_code == 200:
            print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] Message sent, {number-sucess} messages left")
            sucess+=1
            time.sleep(0.2)
        else:
            print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Failed, {number-sucess} messages left")
            fail+=1
        if fail == 4:
            print("")
            print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] New information will be generate, please wait 10 seconds")
            userAgent()
            deviceId()
            time.sleep(10)
            fail = 0

    print("")
    print(f"{Fore.WHITE}[{Fore.GREEN}?{Fore.WHITE}] {number} has be sent to {ngluser}")
    print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] Press 'space' to close the script")
    keyboard.wait('space')  

#Main program
main()