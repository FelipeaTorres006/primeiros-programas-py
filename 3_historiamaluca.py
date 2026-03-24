import time
import os

os.system('clear')

print(" Seja bem-vindo(a) à história de Maluca! ")

time.sleep(2)
os.system('clear')
time.sleep(2)

# Espaço para o usuário digitar as palavras

lugar = input("Digite um lugar: \n")
print()
pessoa_famosa = input("Me conte uma pessoa famosa: \n")
print()
objeto = input("Agora me fale um objeto: \n")
print()
cor = input("Qual cor você quer ? \n")
print()
verbo = input("Qual verbo deveriamos adicionar na história ? \n")
print()
numero = input("Qual sera o número ? \n")
print()
input("Digite ENTER se está pronto!\n")

os.system('clear')

print("Calma ai, estou fazendo a mágica acontecer")

time.sleep(3)
os.system('clear')


print(f"Certa vez, em {lugar}, o famoso {pessoa_famosa}\n" 
      f"acordou e decidiu pintar seu {objeto} de {cor}.\n"
      f"Então começou a {verbo} por {numero} horas\n"
      f"seguidas sem parar. O mundo nunca mais foi o mesmo.\n"
      
      )

