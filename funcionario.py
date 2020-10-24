class Funcionario:
    ## construtor
    def __init__(self,nome, CPF, salario, cargo, admissao, nascimento):
        self._nome = nome
        self._CPF = CPF
        self._salario = salario
        self._cargo = cargo
        self._admissao = admissao
        self._nascimento = nascimento
    
    ## get and sets
    def setNome(self, nome):
        self._nome = nome

    def getNome(self): 
        return self._nome
    
    def setCPF(self, CPF):
        self._CPF = CPF

    def getCPF(self): 
        return self._CPF
    
    def setSalario(self, salario):
        self._salario = salario

    def getSalario(self): 
        return self._salario
    
    def setCargo(self, cargo):
        self._cargo = cargo

    def getCargo(self): 
        return self._cargo
    
    def setAdmissao(self, admissao):
        self._admissao = admissao

    def getAdmissao(self): 
        return self._admissao
    
    def setNascimaneto(self, nascimento):
        self._nascimento = nascimento

    def getNascimento(self): 
        return self._nascimento
    
    ## metodo crud banco de dados