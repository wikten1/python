from Models import Categoria, Estoque, Produtos, Fornecedor, Pessoa, Funcionario, Venda
from DAO import DaoCategoria, DaoVenda, DaoEstoque, DaoFornecedor, DaoPessoa, DaoFuncionario
from datetime import datetime

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso!')
        else:
            print('A categoria que deseja cadastrar já existe')
            
    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))
        
        if len(cat) <= 0:
            print('A categoria que deseja remover não existe!')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso!')
            
            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')
        
    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()
        
        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))
        
        if len(cat > 0):
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x) ,x))
                print("A alteração foi efetuada com sucesso!")
                #TODO: alterar a categoria também do estoque
            else:
                print('A categoria para qual deseja alterar já existe!')
            
        else:
            print('A categoria que deseja alterar não existe!')
            
        with open('catagoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')
                
    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))
        
        if len(cat) <= 0:
            print('A categiria que deseja remover não existe!')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso')
        #TODO: colocar sem categoria no estoque
        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x : x.categoria == categoria, y))
        est == list(filter(lambda x: x.produto.nome == nome, x))
        
        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso')
            else:
                print('Produto já existe em estoque')
        else:
            print('Categoria inexistente')
            
    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
            print('Produto foi removido com sucesso!')    
        else:
            print('O produto que deseja remover não existe!')
        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')
                
def alterarProduto(self, nomeAlterar, novoNome, novoPreco,novaCategoria, novaQuantidade):
    x = DaoEstoque.ler()
    y = DaoCategoria.ler()
    h = list(filter(lambda x: x.categoria == novaCategoria, y))
    if len(h) > 0:
        est = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.produto.nome == novoNome, x))
            if len(est) == 0:
                x = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade), novaQuantidade) if(x.produto.nome == nomeAlterar) else(x), x)
                print('Produto alterado com sucesso!')
            else:
                print('Produto já cadastrado!')
        else:
            print('O produto que deseja alterar não existe!')
            
        
        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" +  i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')
                
def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque vazio')
        else:
            print("==========Produtos==========")
            for i in estoque:
                print(f"Nome: {i.produto.nome}\n"
                      f"Preco: {i.produto.preco}\n"
                      f"Categoria: {i.produto.categoria}\n"
                      f"Quantidade: {i.quantidade}"

                )
                print("--------------------")

        