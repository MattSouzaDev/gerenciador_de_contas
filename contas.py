class Contas:
    def __init__(self, valor, descricao, vencimento, pagar=False, status=False):
        self.valor = valor 
        self.descricao = descricao
        self.vencimento = vencimento
        self.status = status
        self.pagar = pagar
    
    def __str__(self):
        return f"{self.valor}"
    
   
    #getters
    @property
    def valor(self):
        return self._valor
    
    @property
    def vencimento(self):
        return self._vencimento
  
    @valor.setter
    def valor(self, valor):
        if not valor:
            raise ValueError
        self._valor = valor

    @vencimento.setter
    def vencimento(self, vencimento):
        if not vencimento:
            raise ValueError
        self._vencimento = vencimento

