# arquivo = open('pessoa.txt', 'a')
# i = 0
# while True:  
#     if i > 1:
#         break  
#     arquivo.write(input('Digite o nome da pessoa: ') + " " + input('Digite a idade: ') + "\n")
#     i += 1

# arquivo = open('pessoa.txt','r')
# resultados = arquivo.read()
# print(resultados)


arquivo = open('pessoa.txt','r')
resultados = arquivo.readlines()
for i in resultados:
    print(i)
    
    
arquivo = open('pessoa.txt','r')
resultados = arquivo.readlines()
x = []
for i in resultados:
    x.append(i.split())
print(x[1][1])
arquivo.close()