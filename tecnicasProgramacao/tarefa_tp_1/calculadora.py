acumulador = 0

def soma(operador_a, operador_b = None):
    global acumulador
    if operador_b == None:
        acumulador += operador_a
    else:
        acumulador = operador_a + operador_b
    return acumulador

def subtracao(operador_a, operador_b = None):
    global acumulador
    if operador_b == None: 
        acumulador -= operador_a
    else:   
        acumulador = operador_a - operador_b
    return acumulador
        
def multiplicacao(operador_a, operador_b = None):
    global acumulador
    if operador_b == None:
        acumulador = acumulador * operador_a
    else:
        acumulador = operador_a * operador_b
    return acumulador
    
def divisao(operador_a, operador_b = None):
    global acumulador
    if operador_b == None: 
        acumulador = acumulador / operador_a
    else:   
        acumulador = operador_a / operador_b
    return acumulador

def valor_acumulador(): #criado para atribuir o valor da variável acumulador 
    return acumulador