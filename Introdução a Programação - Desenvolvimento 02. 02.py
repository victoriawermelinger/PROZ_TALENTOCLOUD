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