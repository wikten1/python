#Receba um número e mostra a tabuada completa dele usando o laço for.

num = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")