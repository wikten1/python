#Receba um número e exiba se ele é positivo ou negativo.

numero = int(input("Digite o número: "))

if numero > 0:
    print(f"O número {numero} é positivo")
elif numero < 0:
    print(f"O número {numero} é negativo")
else:
    print("O número é 0")