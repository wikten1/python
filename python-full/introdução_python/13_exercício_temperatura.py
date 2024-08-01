# Receba uma temperatura em farenheit e exiba em graus celsius.
# c = 5 * f - 32/9

temperatura = float(input("Digite uma temperatura em farenheit: "))
celsius = 5 * ((temperatura - 32)/9)

print(f"A temperatura convertida para celsicus é: {celsius}")