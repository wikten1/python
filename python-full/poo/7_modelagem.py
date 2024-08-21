class Pessoa:
    possui_olho = True
    possui_boca = True
    raca = "Ser humano"
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def retorna_nome(self):
        return self.nome
    
    def logar_sistema(self):
        print(f'{self.retorna_nome()} está logado no sistema')
        
    @classmethod
    def andar(cls):
        cls.possui_boca = False
        return None
    
    @staticmethod
    def e_adulto(idade):
        if idade > 18:
            return True
        return False
        
# p1 = Pessoa('Caio Sampaio', 21)
# p2 = Pessoa('Marcos sampaio', 45)

print(Pessoa.e_adulto(21))