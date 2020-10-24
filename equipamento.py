import pymysql
conexao = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
        )
cursor = conexao.cursor()
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
    def consultar(self):
        cursor.execute("use fazenda_bd;")
        cursor.execute("SELECT `ID`, `nome` FROM `Equipamento`;")
        dados = cursor.fetchall()
        for d in dados:
            print(d[0], d[1])

    def inserir(self):
        nome = self.getNome()
        tipo = self.getTipo()
        sql = "INSERT INTO `Equipamento`(`nome`, `tipo`) VALUES ('" + nome + "','" + tipo + "');"
        cursor.execute("use fazenda_bd;")
        cursor.execute(sql)
        conexao.commit()

    def alterar(self,cod):
        nome = self.getNome()
        tipo = self.getTipo()
        sql = "UPDATE `Equipamento` SET `nome`='" + nome + "',`tipo`='" + tipo + "' WHERE `ID`=" + cod +";"
        cursor.execute("use fazenda_bd;")
        cursor.execute(sql)
        conexao.commit()

    def excluir(self,cod):
        sql = "DELETE FROM `Equipamento` WHERE `ID`=" + cod +";"
        cursor.execute("use fazenda_bd;")
        cursor.execute(sql)
        conexao.commit()