#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
#A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).
#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.


import datetime

nome = str(input("digite nome:"))
while len(nome) <= 3:
    nome = str(input("digite_nome:"))
nasc = int(input("digite_ano_de_nascimento:"))

while nasc < 1922 or nasc > 2021:
    print("Erro!")
    nasc = int(input("digite_ano_de_nascimento:"))
else:
    print("Validando_os_dados....", nome)

hoje = datetime.date.today().year

idade = hoje - nasc

print("Resultado:\n" + nome + " está_com", idade)