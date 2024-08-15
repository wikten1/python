# import pickle

# x = [1,2,3,4]

# string = pickle.dumps(x)
# print(pickle.loads(string))
#-----------------------------------
# import pickle
# x = [1,2,3,4]

# arq = open('arquivo.pkl', 'wb')
# pickle.dump(x, arq)

# arq = open('arquivo.pkl', 'rb')
# retornou = pickle.load(arq)

# print(retornou)

#------------------------------------

import pickle
class Pessoa:
    nome = 'caio'
    idade = 20

class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
p1 = Pessoas('marcos', 21)

arq = open('arquivo.pkl', 'wb')
pickle.dump(p1, arq)

arq = open('arquivo.pkl', 'rb')
retornou = pickle.load(arq)

print(retornou)