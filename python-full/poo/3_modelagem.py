class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
    
    def retorna_nome(self):
        return self.nome
    
    def logar_sistema(self):
        print(f'{self.retorna_nome()} está logado no sistema')
        
p1 = Pessoas('Wikten Alves', 25, '16544344889435')

p2 = Pessoas('Caio Sampaio', 25, "16876853561")

p2.logar_sistema()