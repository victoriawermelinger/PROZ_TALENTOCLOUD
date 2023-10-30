#Desenvolva um algoritmo que utilize as seguintes características de um veículo:
#- Quantidade de rodas;
#- Peso bruto em quilogramas;
#- Quantidade de pessoas no veículo.

#Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir #das condições:
#A: Veículos com duas ou três rodas;
#B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
#C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
#D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; E: Veículos com quatro rodas ou mais e com #mais de 6000 kg.

# ALGORITIMO
Variaveis 
roda = inteiro
assento = inteiro
peso = floa
escreva(“O seu veículo possui quantas rodas?”)
 leia(roda)
escreva(“Quantos assentos o seu veículo possui?”)
 leia(assento)
escreva(“Qual o peso do seu veículo?”)
leia(peso)
se (roda<=3) entao
escreva(“Carteira de Habilitação Tipo A”)
senao se (roda==4) e (peso<=3500) e (assento<=8) entao
escreva(“Carteira de Habilitação Tipo B”)
senao se (roda>=4) e (peso>=3500) e (peso<=6000) entao
escreva(“Carteira de Habilitação Tipo C”)
senao se (roda>=4) e (assento>8) entao
escreva(“Carteira de Habilitação Tipo D”)
senao se (roda>=4) e (peso>6000) entao
escreva(“Carteira de Habilitação Tipo E”)
senao
escreva(“Dados informados incorretos, por favor reinicie o questionário.”)

#PYTHON

roda = int(input("Quantas rodas o veículo possui?"))
assentos = int(input("Quantos assentos o veiculo possui?"))
peso = int(input("Quantos quilos o veiculo pesa?"))
if(roda <= 3):
  print("Careira de Habilitação Tipo A")
elif(roda == 4) and (peso == 3500) and (assentos <=8):
  print("Carteira de Habilitação Tipo B")
elif(roda>=4) and (peso>=3500) and (peso<=6000):
    print("Carteira de Habilitação Tipo C")
elif (roda>=4) and (assentos>8):
    print("Carteira de Habilitação Tipo D")
elif(roda>=4) and (peso>6000):
    print("Carteira de Habilitação Tipo E")
else:
    print("Dados informados incorretos por favor repita a operação")
