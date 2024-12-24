from sysbanco_t3 import Conta
from sysbanco_t3 import ContaPoupanca
from sysbanco_t3 import ContaEspecial
from sysbanco_t3 import Banco

def terminal():
    opcao = 0
    sisbanco = Banco(0.01)
    while opcao != 8:
        print("SisBanco :: Bem-vindo!")
        print("..:::Opções:::..")
        print("0 - CriarConta")
        print("1 - Creditar")
        print("2 - Debitar")
        print("3 - Transferir")
        print("4 - Saldo")
        print("5 - Render Juros")
        print("6 - Render Bonus")
        print("7 - Alterar Taxa de Juros")
        print("8 - Sair")
        opcao = int(input("Digite: "))

        if opcao == 0:
            tipo = input("Digite o tipo de conta a ser criada: (S − Simples | P − Poupança | E − Especial): ")
            if tipo.lower() == "s":
                numero = input("Digite o número da conta SIMPLES: ")
                conta = Conta(numero)
                sisbanco.cadastrar(conta)

            elif tipo.lower() == "p":
                numero = input("Digite o número da conta POUPANÇA: ")
                conta = ContaPoupanca(numero)
                sisbanco.cadastrar(conta)

            elif tipo.lower() == "e":
                numero = input("Digite o número da conta ESPECIAL: ")
                conta = ContaEspecial(numero)
                sisbanco.cadastrar(conta)
            else: 
                print("..::: CONTA INVÁLIDA :::..")
            
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
                     
        elif opcao == 4: 
            numConta = input("Digite o número da conta que deseja consultar o saldo: ")
            sisbanco.saldoB(numConta)
                
        elif opcao == 5:
            numConta = input("Digite a conta que deseja Render juros: ")
            sisbanco.renderJuros(numConta)

        elif opcao == 6:
            numConta = input("Digite a conta que deseja Render bônus: ")
            sisbanco.renderBonus(numConta)

        elif opcao == 7:
            novaTaxa = float(input("Digite a nova taxa de correção da Poupança: "))
            sisbanco.set_taxa(novaTaxa)

        elif opcao == 8:
            print("SisBanco :: Bye!")
            break
        else:
            print("NÚMERO INVÁLIDO, DIGITE OUTRO NÚMERO!")

if __name__ == "__main__":
    terminal()