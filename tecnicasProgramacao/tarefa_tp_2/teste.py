from sysbanco import Conta
from sysbanco import Banco

def criar_conta():
    conta = Conta("21.342-7")
    conta.creditar(500.87)
    conta.debitar(45.00)
    print("Conta Numero: {} - Saldo: {}".format(conta.get_numero(),
    conta.get_saldo()))

    conta1 = Conta("18.982-7")
    conta1.creditar(100.87)
    conta1.debitar(60.00)
    print("Conta Numero: {} - Saldo: {}".format(conta1.get_numero(),
    conta1.get_saldo()))

    banco = Banco()
    banco.cadastrar(conta)
    banco.cadastrar(conta1)
    #print(banco.saldoB("18.982-7"))
    
    print(banco.procurar("21.342-7"))
    banco.transferir("21.342-7", "18.982-7", 50.0)
    print(banco.saldoB("18.982-7"))
    print(banco.saldoB("21.342-7"))
    banco.debitarB("21.342-7", 100)
    print(banco.saldoB("21.342-7"))

    banco.transferir("21.342-7", "18.982-7", 1000.0)

if __name__ == "__main__":
    criar_conta()
    #criar_conta2()