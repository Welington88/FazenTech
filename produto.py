import pymysql
conexao = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
        )
cursor = conexao.cursor()
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
    def consultar(self):
        cursor.execute("use fazenda_bd;")
        cursor.execute("SELECT `ID`, `nome`, `qtd_em_estoque`, `preco` FROM `Produto`;")
        dados = cursor.fetchall()
        for d in dados:
            print(d[0], d[1])

    def inserir(self):
        nome = self.getNome()
        tipo = self.getTipo()
        qtd_em_estoque = int(self.getQtd_em_estoque())
        preco = float(self.getPreco())
        sql = "INSERT INTO `Produto`(`nome`, `tipo`, `qtd_em_estoque`, `preco`) VALUES ('"+nome+"','" + tipo +"',"+ qtd_em_estoque+","+ preco +");"
        cursor.execute("use fazenda_bd;")
        cursor.execute(sql)
        conexao.commit()

    def alterar(self,cod):
        nome = self.getNome()
        tipo = self.getTipo()
        qtd_em_estoque = int(self.getQtd_em_estoque())
        preco = float(self.getPreco())
        sql = "UPDATE `Produto` SET `nome`='" + nome +"',`tipo`='"+ tipo +"',`qtd_em_estoque`="+ qtd_em_estoque+",`preco`="+ preco +" WHERE" + cod +";"
        cursor.execute("use fazenda_bd;")
        cursor.execute(sql)
        conexao.commit()

    def excluir(self,cod):
        sql = "DELETE FROM `Produto` WHERE `ID`=" + cod +";"
        cursor.execute("use fazenda_bd;")
        cursor.execute(sql)
        conexao.commit()