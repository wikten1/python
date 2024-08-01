#Receba F para feminimo e M para masculino e exbia o sexo da pessoa.

sexo = input("Digite o sexo da pessoa (F/M): ")

if sexo == 'M' or sexo == 'f':
    print("Masculino")
elif sexo == 'F' or sexo == 'm':
    print("Feminino")
else:
    print("Digite um sexo valido!")