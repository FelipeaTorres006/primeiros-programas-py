# python3 1_adivinheonumero.py
# Como eu faço para printar um número aleatorio entre 1 e 10 


import os               # Modulo interação do terminal
import random           # Modulo da aleatoriedade número aleatório
import time             # Modulo que retorna tempo

os.system('clear')

x = random.randint(1, 10)   # Aqui diz que a variável x é uma random do tipo inteira

print('Seja Bem-vindo ao jogo da advinhação\n')
print('Pense em um número de 1 a 10\n')
input('Se já pensou aperte ENTER:\n')
os.system('clear')

print('Pensando...')

time.sleep(2)
os.system('clear')

while True: 
    print(f'O número que você pensou foi... {x}\n')
    resposta = input('Acertei ? (sim/não)\n').lower()

    if resposta == 'sim':
        print();
        print('Uhull!!! Eu sou o primo do Akinator mesmo.')
        break
    elif resposta.isdigit():     # Esse bloco verifica se o input da resposta é composto apenas por algarismos
        os.system('clear')       # Aqui limpa tudo o que estava acima
        print('Só consigo ler letras, meu amigo.')
        time.sleep(2)
        os.system('clear')
    else:
        os.system('clear')
        print('Mama mia, irei de novo\n')
        x = random.randint(1,10)  # Isso imprime um número aleatório de 1 a 10 
        time.sleep(2)             # Isso deixa o sistema  "dormir" por 2 segundos
        os.system('clear')



