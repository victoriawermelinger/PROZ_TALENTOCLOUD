#Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
#1. Soma
#2. Subtração
#3. Multiplicação
#4. Divisão
#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.


def calculadora(num1, num2, operador):
    if operador == 1:
       resultado = num1 + num2
    if operador == 2:
        resultado = num1 - num2
    if operador == 3:
        resultado = num1 * num2
    if operador == 4:
        resultado = num1 // num2
    return resultado

num1 = int(input("\nDigite o primeiro numero:"))
num2 = int(input("Digite o segundo numero: "))

operador = int(input("\nDigite 1: Soma\nDigite 2: Subtração\nDigite 3: Multiplicação\nDigite 4: Divisão\n"))
print()
resultado = calculadora(num1, num2, operador)
print('Resultado =', resultado)