class Pessoas:
    def __init__(self, nome, idade, cpf):
        print(f'{nome} | {idade} | {cpf}')
    
    def logar_sistema(self):
        print(f'estou logado no sistema')
        
p1 = Pessoas('Wikten Alves', 25, '16544344889435')

p2 = Pessoas('Caio Sampaio', 25, "16876853561")
