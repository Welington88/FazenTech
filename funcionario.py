import pymysql
conexao = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
        )
cursor = conexao.cursor()
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
    # metodo crud banco de dados
    def consultar(self):
        cursor.execute("use fazenda_bd;")
        cursor.execute("SELECT * FROM `Funcionario`;")
        dados = cursor.fetchall()
        for d in dados:
            print(d[0], d[1])

    def inserir(self):
        nome = self.getNome()
        cpf = self.getCPF()
        salario = self.getSalario()
        cargo = self.getSalario()
        admissao = self.getAdmissao()
        nascimento = self.getNascimento()
        sql = "INSERT INTO `Funcionario`(`nome`, `CPF`, `salario`, `cargo`, `admissao`, `nascimento`) VALUES ('" + nome + "','" + cpf +"'," + salario +", '" + cargo+"', '"+ admissao  +"','" + nascimento + "' );"
        cursor.execute("use fazenda_bd;")
        cursor.execute(sql)
        conexao.commit()

    def alterar(self,cod):
        nome = self.getNome()
        cpf = self.getCPF()
        salario = self.getSalario()
        cargo = self.getCargo()
        admissao = self.getAdmissao()
        nascimento = self.getNascimento()
        sql = "UPDATE `Funcionario` SET `nome`='" + nome + "',`CPF`='" + cpf + "',`salario`=" + salario +",`cargo`='" + cargo + "',`admissao`='" + admissao + "',`nascimento`='" + nascimento + "'WHERE `ID`="+ cod +";"
        cursor.execute("use fazenda_bd;")
        cursor.execute(sql)
        conexao.commit()

    def excluir(self,cod):
        sql = "DELETE FROM `Funcionario` WHERE `ID`=" + cod +";"
        cursor.execute("use fazenda_bd;")
        cursor.execute(sql)
        conexao.commit()