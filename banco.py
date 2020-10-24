import pymysql
conexao = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
        )
cursor = conexao.cursor()
class Banco:
    def __init__(self): ## construtor
        self._bd = "fazenda_bd"

    def consultarBanco(self):
        cursor.execute("use fazenda_bd;")
        cursor.execute("SELECT * FROM `Produto`;")
        dados = cursor.fetchall()
        for d in dados:
            print(d[0], d[1])