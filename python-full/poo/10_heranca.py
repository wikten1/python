class Animal:
    def andar(self):
        print('estou andando como um animal')
        
    def correr(self):
        print("estou correndo")
        
    def pular(self):
        print('estou pulando')
        
class Felino(Animal):
    def felino(self):
        print('eu sou um felino')

class Gato(Felino, Animal):
    def miar(self):
        print('estou miando como um gato')
    def andar(self):
        print('estou andando como um felino')
        
class Cachorro(Animal):
  def latir(self):
       print('estou latindo')
        
y = Gato()      
y.miar()