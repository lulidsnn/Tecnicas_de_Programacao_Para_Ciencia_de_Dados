class Conta:
  def __init__(self, numero:str): 
    self.__numero = numero #numero da CONTA
    self.__saldo = 0.0  

  def creditar(self, valor:float) -> None:
    self.__saldo += valor

  def debitar(self, valor:float) -> None:
    self.__saldo -= valor   

  def get_numero(self)-> str:
    return self.__numero

  def get_saldo(self)-> float:
    return self.__saldo

class ContaPoupanca(Conta):
   
   def __init__(self, numero:str):
      super().__init__(numero)

   def render_juros(self, taxa: float) -> None:
    self.creditar(self.get_saldo() * taxa)

class ContaEspecial(Conta):
  def __init__(self, numero: str):
    super().__init__(numero)
    self.__bonus = 0

  def get_bonus(self):
     return self.__bonus
  
  def render_bonus(self) -> None:
     super().creditar(self.__bonus)
     self.__bonus = 0

  def creditar(self, valor:float) -> None: #toda vez que utilizamos o método CREDITAR, incrementamos o atributo BONUS com 1% do valor creditado
     self.__bonus += valor * 0.01
     super().creditar(valor)

class Banco:
    def __init__(self, taxa):
      self.__contas = []
      self.__taxaCorrecao = taxa

    def cadastrar(self,conta:Conta) -> None:
        self.__contas.append(conta)

    def procurar(self, numero:str) -> Conta:
        for conta in self.__contas:
            if conta.get_numero() == numero:
                return conta
        return None

    def creditarB(self, numero:str, valor: float) -> None:
        conta = self.procurar(numero)
        if conta is not None:
          conta.creditar(valor)
          print(f"Valor R${valor} creditado com sucesso na conta {numero}!")
        else:
           print(" !..:::CONTA INEXISTENTE :::..!")

    def debitarB(self, numero:str, valor: float) -> None:
        conta = self.procurar(numero)
        if conta is not None:
            conta.debitar(valor)
            print(f"Valor R${valor} debitado com sucesso na conta {numero}!")
        else:
           print(" !..:::CONTA INEXISTENTE :::..!")

    def saldoB(self, numero:str) -> float:
        conta = self.procurar(numero)
        if conta is not None:
            print(f"Saldo da conta {numero} é de: R${conta.get_saldo()}")
        else:
            print(" !..:::CONTA INEXISTENTE :::..!")
            return None

    def transferir(self, origem:str, destino:str, valor: float) -> None:
        contaOrigem = self.procurar(origem)  #retorna uma CONTA
        contaDestino = self.procurar(destino) #retorna uma conta
        if contaOrigem is not None and contaDestino is not None:
            if valor > contaOrigem.get_saldo():
               print(f"Saldo na conta {origem} é insuficiente!")
            else: 
              contaOrigem.debitar(valor)
              contaDestino.creditar(valor)
              print(f"Transferência no valor de {valor}R$ da conta {origem} para a conta {destino} feita com sucesso!")
        else:
            print(" !..:::CONTA INEXISTENTE :::..!")
            return None
        
    def renderJuros(self, numero:str) -> None:
       conta = self.procurar(numero)
       if conta is not None and isinstance(conta, ContaPoupanca):
          conta.render_juros(self.__taxaCorrecao)
          print(f"Saldo com juros: {conta.get_saldo()}")
       else:
          print("A conta informada não é do tipo POUPANÇA, ou é INEXISTENTE")
          return None

    def get_taxa(self) -> float:
       return self.__taxaCorrecao
    
    def set_taxa(self,taxa) -> None:
       self.__taxaCorrecao = taxa

    def renderBonus(self, numero:str) -> None:
       conta = self.procurar(numero)
       if conta is not None and isinstance(conta, ContaEspecial):
          conta.render_bonus()
          print(f"Saldo com bônus: {conta.get_saldo()}")
       else:
          print("A conta informada não é do tipo ESPE, ou é INEXISTENTE")
          return None
       
           