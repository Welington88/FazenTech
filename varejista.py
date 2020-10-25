import pymysql
conexao = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
        )
cursor = conexao.cursor()
class Varejista:
    ##construtor
    def __init__(self, nome, pf_pj, status):
        self._nome = nome
        self._pf_pj = pf_pj
        self._status = status
    ## get and set
    def setNome(self, nome):
        self._nome = nome

    def getNome(self): 
        return self._nome
    
    def setPf_pj(self, pf_pj):
        self._pf_pj = pf_pj

    def getPf_pj(self): 
        return self._pf_pj

    def setStatus(self, status):
        self._status = status

    def getStatus(self): 
        return self._status

    ## metodo crud banco de dados
    def consultar(self):
        cursor.execute("use fazenda_bd;")
        cursor.execute("SELECT `ID`, `Nome` FROM `VAREJISTA`;")
        dados = cursor.fetchall()
        for d in dados:
            print(d[0], d[1])

    def venda(self,cod_produto,cod_varejista,qtd):
        sql = "INSERT INTO `Compra`(`fk_Produto_ID`, `fk_VAREJISTA_ID`, `qtd`) VALUES ('" + cod_produto + "','"+ cod_varejista+"','"+ qtd +"');"
        cursor.execute("use fazenda_bd;")
        cursor.execute(sql)
        conexao.commit()

    def inserir(self):
        nome = self.getNome()
        pf_pj = self.getPf_pj()
        status = self.getStatus()
        sql = "INSERT INTO `VAREJISTA`(`Nome`, `pf_pj`, `status`) VALUES ('" + nome + "','" + pf_pj + "','" + status + "');"
        cursor.execute("use fazenda_bd;")
        cursor.execute(sql)
        conexao.commit()

    def alterar(self,cod):
        nome = self.getNome()
        pf_pj = self.getPf_pj()
        status = self.getStatus()
        sql = "UPDATE `VAREJISTA` SET `Nome`='" + nome + "',`pf_pj`='" + pf_pj + "',`status`='" + status + "' WHERE `ID`=" + cod + ";"
        cursor.execute("use fazenda_bd;")
        cursor.execute(sql)
        conexao.commit()

    def excluir(self,cod):
        sql = "DELETE FROM `VAREJISTA` WHERE `ID`=" + cod +";"
        cursor.execute("use fazenda_bd;")
        cursor.execute(sql)
        conexao.commit()