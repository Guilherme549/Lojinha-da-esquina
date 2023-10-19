from model import Categoria, Estoque, Fornecedor, Funcionario, Pessoa, Produto, Venda 


class ProdutoDal:
    @classmethod
    def Cadastrar(cls, produto: Produto):
        with open("CadastroProduto.txt", "w") as arq:
            arq.write(produto.nome + " " + str(produto.preco) + " " + produto.categoria)

    
    @classmethod
    def ler(cls):
        with open("CadastroProduto.txt", "r") as arq:
            print(arq.readlines())


p1 = Produto("sal", "10", "tempero")

produto = ProdutoDal.Cadastrar(p1)
ProdutoDal.ler()