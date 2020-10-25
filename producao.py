import pymysql
conexao = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
        )
cursor = conexao.cursor()
class ProducaoLeite:
    ##contrutor
    def __init__(self,especie, data_ultima_ordenha, temperatura_do_leite, produtividade_de_cada_quarto, inseminacao, estimativa_do_parto, secagem_esperada, minutos_de_ruminacao_por_dia):
        self._especie = especie
        self._data_ultima_ordenha = data_ultima_ordenha
        self._temperatura_do_leite = temperatura_do_leite
        self._produtividade_de_cada_quarto = produtividade_de_cada_quarto
        self._inseminacao = inseminacao
        self._estimativa_do_parto = estimativa_do_parto
        self._secagem_esperada = secagem_esperada
        self._minutos_de_ruminacao_por_dia = minutos_de_ruminacao_por_dia
    ## get and sets
    def setEspecie(self, especie):
        self._especie = especie

    def getEspecie(self): 
        return self._especie

    def setData_ultima_ordenha(self, data_ultima_ordenha): 
        self._data_ultima_ordenha = data_ultima_ordenha

    def getData_ultima_ordenha(self):
        return self._data_ultima_ordenha
    
    def setTemperatura_do_leite(self, temperatura_do_leite): 
        self._temperatura_do_leite = temperatura_do_leite

    def getTemperatura_do_leite(self):
        return self._temperatura_do_leite
    
    def setProdutividade_de_cada_quarto(self, produtividade_de_cada_quarto): 
        self._produtividade_de_cada_quarto = produtividade_de_cada_quarto

    def getProdutividade_de_cada_quarto(self):
        return self._produtividade_de_cada_quarto
    
    def setInseminacao(self, inseminacao): 
        self._inseminacao = inseminacao

    def getInseminacao(self):
        return self._inseminacao
    
    def setEstimativa_do_parto(self, estimativa_do_parto): 
        self._estimativa_do_parto = estimativa_do_parto

    def getEstimativa_do_parto(self):
        return self._estimativa_do_parto
    
    def setSecagem_esperada(self, secagem_esperada): 
        self._secagem_esperada = secagem_esperada

    def getSecagem_esperada(self):
        return self._secagem_esperada
    
    def setMinutos_de_ruminacao_por_dia(self, minutos_de_ruminacao_por_dia): 
        self._minutos_de_ruminacao_por_dia = minutos_de_ruminacao_por_dia

    def getMinutos_de_ruminacao_por_dia(self):
        return self._minutos_de_ruminacao_por_dia
    ## metodo crud banco de dados
    def consultar(self):
        cursor.execute("use fazenda_bd;")
        cursor.execute("SELECT * FROM `Producao_Leite`;")
        dados = cursor.fetchall()
        for d in dados:
            print(d[0], d[1],d[2],d[3],d[4],d[6],d[7])

    def inserir(self):
        especie = self.getEspecie()
        data_ultima_ordenha = self.getData_ultima_ordenha()
        temperatura_do_leite = float(self.getTemperatura_do_leite())
        produtividade_de_cada_quarto = float(self.getProdutividade_de_cada_quarto())
        inseminacao = self.getInseminacao()
        estimativa_do_parto = self.getEstimativa_do_parto()
        secagem_esperada = float(self.getSecagem_esperada())
        minutos_de_ruminacao_por_dia = float(self.getMinutos_de_ruminacao_por_dia())
        sql = "INSERT INTO `Producao_Leite`(`especie`, `data_ultima_ordenha`, `temperatura_do_leite`, `produtividade_de_cada_quarto`, `inseminacao`, `estimativa_do_parto`, `secagem_esperada`, `minutos_de_ruminacao_por_dia`) VALUES ('" + especie + "','" + data_ultima_ordenha + "'," + temperatura_do_leite  +  "," + produtividade_de_cada_quarto +",'" + inseminacao +"','" + estimativa_do_parto +"'," + secagem_esperada + ","+ minutos_de_ruminacao_por_dia+");"
        cursor.execute("use fazenda_bd;")
        cursor.execute(sql)
        conexao.commit()

    def alterar(self,cod):
        especie = self.getEspecie()
        data_ultima_ordenha = self.getData_ultima_ordenha()
        temperatura_do_leite = float(self.getTemperatura_do_leite())
        produtividade_de_cada_quarto = float(self.getProdutividade_de_cada_quarto())
        inseminacao = self.getInseminacao()
        estimativa_do_parto = self.getEstimativa_do_parto()
        secagem_esperada = float(self.getSecagem_esperada())
        minutos_de_ruminacao_por_dia = float(self.getMinutos_de_ruminacao_por_dia())
        sql = "UPDATE `Producao_Leite` SET `especie`='" + especie + "',`data_ultima_ordenha`='" + data_ultima_ordenha + "',`temperatura_do_leite`=" + temperatura_do_leite  +  ",`produtividade_de_cada_quarto`=" + produtividade_de_cada_quarto +",`inseminacao`='" + inseminacao +"',`estimativa_do_parto`='" + estimativa_do_parto +"',`secagem_esperada`=" + secagem_esperada + ",`minutos_de_ruminacao_por_dia`="+ minutos_de_ruminacao_por_dia+" WHERE `ID`=" + cod + ";"
        cursor.execute("use fazenda_bd;")
        cursor.execute(sql)
        conexao.commit()

    def excluir(self,cod):
        sql = "DELETE FROM `Producao_Leite` WHERE `ID`=" + cod +";"
        cursor.execute("use fazenda_bd;")
        cursor.execute(sql)
        conexao.commit()