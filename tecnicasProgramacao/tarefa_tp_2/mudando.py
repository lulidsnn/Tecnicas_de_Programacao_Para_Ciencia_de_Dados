from sysbanco import Conta
from sysbanco import Banco

def terminal():
    opcao = 0
    sisbanco = Banco()
    while opcao != 5:
        print("SisBanco :: Bem-vindo!")
        print(".::Opções::.")
        print("0 - CriarConta")
        print("1 - Creditar")
        print("2 - Debitar")
        print("3 - Transferir")
        print("4 - Saldo")
        print("5 - Sair")
        opcao = int(input("Digite: "))

        if opcao == 0:
            numero = input("Digite o número da conta: ")
            conta = Conta(numero)
            sisbanco.cadastrar(conta)

        elif opcao == 1:
            numConta = input("Digite o número da conta que deseja creditar: ")
            valorC = float(input("Digite o valor a ser creditado: "))
            sisbanco.creditarB(numConta, valorC)
            
        elif opcao == 2:
            numConta = input("Digite o número da conta que deseja debitar: ")
            valorC = float(input("Digite o valor a ser debitado: "))
            sisbanco.debitarB(numConta, valorC)
            
        elif opcao == 3:
            contaOrigem = input("Digite o número da conta origem (que irá transferir): ")
            contaDestino = input("Digite o número da conta destino (que irá receber): ")
            valorT = float(input("Digite o valor a ser transferido: "))
            sisbanco.transferir(contaOrigem, contaDestino, valorT)
                     
        elif opcao == 4: #ALTERAR
            numConta = input("Digite o número da conta que deseja consultar o saldo: ")
            sisbanco.saldoB(numConta)

        elif opcao == 5:
            print("SisBanco :: Bye!")
            break
        
if __name__ == "__main__":
    terminal()