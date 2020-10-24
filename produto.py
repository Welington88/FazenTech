class Produto:
    ##construtor
    def __init__(self,nome, tipo, qtd_em_estoque, preco):
        self._nome = nome
        self._tipo = tipo
        self._qtd_em_estoque = qtd_em_estoque
        self._preco = preco
    ## get and sets
    def setNome(self, nome):
        self._nome = nome

    def getNome(self): 
        return self._nome

    def setTipo(self, tipo): 
        self._tipo = tipo

    def getTipo(self):
        return self._tipo

    def setQtd_em_estoque(self, qtd_em_estoque):
        self._qtd_em_estoque = qtd_em_estoque

    def getQtd_em_estoque(self): 
        return self._qtd_em_estoque

    def setPreco(self, preco):
        self._preco = preco

    def getPreco(self): 
        return self._preco
    
    ## metodo crud banco de dados