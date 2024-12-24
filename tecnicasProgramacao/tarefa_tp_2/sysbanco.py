class Conta:
  def __init__(self, numero:str): 
    self.__numero = numero #numero da CONTA
    self.__saldo = 0.0  

  def creditar(self, valor:float) -> None:
    self.__saldo += valor

  def debitar(self, valor:float) -> None:
    self.__saldo -= valor   

  def get_numero(self) -> str:
    return self.__numero

  def get_saldo(self) -> float:
    return self.__saldo

class Banco:
    def __init__(self):
      self.__contas = []

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
           