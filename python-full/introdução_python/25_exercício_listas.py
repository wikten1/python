#Receba 10 valores e exiba a soma de todos eles

lista = [int(input()) for i in range(0, 10)]
soma = 0

    
for i in lista:
   soma +=  i
   
print(soma)