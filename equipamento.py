class Equipamento: ##definicao da classe

    def __init__(self, nome, tipo): ## construtor
        self._nome = nome
        self._tipo = tipo

    ## get and sets
    def setNome(self, nome):
        self._nome = nome

    def getNome(self): 
        return self._nome

    def setTipo(self, tipo): 
        self._tipo = tipo

    def getTipo(self):
        return self._tipo
    ## metodo crud banco de dados