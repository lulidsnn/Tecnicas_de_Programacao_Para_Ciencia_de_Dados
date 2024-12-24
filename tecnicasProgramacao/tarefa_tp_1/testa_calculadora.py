import calculadora as calc

def testeSoma(operador_a, operador_b = None):
    if operador_b == None:
        operador_b = calc.valor_acumulador()
    print("Soma de {} e {} = ".format(operador_a, operador_b))
    return calc.soma(operador_a, operador_b)
    
def testeSub(operador_a, operador_b = None):
    if operador_b == None:
        operador_b = calc.valor_acumulador()
    print("Subtração de {} e {} = ".format(operador_a, operador_b))
    return calc.subtracao(operador_a, operador_b)

def testeMult(operador_a, operador_b = None):
    if operador_b == None:
        operador_b = calc.valor_acumulador()
    print("Multiplicação de {} e {} = ".format(operador_a, operador_b))
    return calc.multiplicacao(operador_a, operador_b)

def testeDiv(operador_a, operador_b = None):
    if operador_b == None:
        operador_b = calc.valor_acumulador()
    print("Divisão de {} e {} = ".format(operador_a, operador_b))
    return calc.divisao(operador_a, operador_b)

def testeTodas(operador_a, operador_b = None):
    if operador_b == None:
        operador_b = calc.valor_acumulador()
    print("Soma de {} e {} = ".format(operador_a, operador_b), calc.soma(operador_a, operador_b))
    print("Subtração de {} e {} = ".format(operador_a, operador_b), calc.subtracao(operador_a, operador_b))
    print("Multiplicação de {} e {} = ".format(operador_a, operador_b),calc.multiplicacao(operador_a, operador_b))
    print("Divisão de {} e {} = ".format(operador_a, operador_b), calc.divisao(operador_a, operador_b))

print(testeDiv(8,2))
print(testeSoma(5))