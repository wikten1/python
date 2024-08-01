#Receba um número inteiro do usuário e mostre a tabuada desse número.

num = int(input("Digite um número inteiro: "))
i = 1
while i <= 10:
        print(f"{num} X {i} = {num*i}")
        i += 1