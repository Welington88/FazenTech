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