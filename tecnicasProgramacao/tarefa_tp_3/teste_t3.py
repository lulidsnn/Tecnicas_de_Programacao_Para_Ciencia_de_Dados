from sysbanco_t3 import Conta
from sysbanco_t3 import ContaPoupanca
from sysbanco_t3 import ContaEspecial
from sysbanco_t3 import Banco

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

    conta2 = ContaPoupanca("88.456-7")
    conta2.creditar(600)
    conta2.debitar(20)
    #conta2.render_juros(0.02)
    conta2.get_saldo()
    print("Conta Numero: {} - Saldo: {}".format(conta2.get_numero(),
    conta2.get_saldo()))

    conta3 = ContaEspecial("55.715-9")
    conta3.creditar(700)
    conta3.creditar(300)
    print(conta3.get_bonus())
    print(conta3.get_saldo())

    banco = Banco()
    banco.cadastrar(conta)
    banco.cadastrar(conta1)
    banco.cadastrar(conta2)
    banco.cadastrar(conta3)
    banco.set_taxa(0.03)
    banco.renderJuros("88.456-7")
    banco.renderBonus("55.715-9")
    
    
    '''print(banco.procurar("21.342-7"))
    banco.transferir("21.342-7", "18.982-7", 50.0)
    print(banco.saldoB("18.982-7"))
    print(banco.saldoB("21.342-7"))
    banco.debitarB("21.342-7", 100)
    print(banco.saldoB("21.342-7"))'''

if __name__ == "__main__":
    criar_conta()
    #criar_conta2()