class Calculadora: #calculadora com 'memória'
    def __init__(self):
        self.__acumulador = 0.0

    def somar(self, operando_a, operando_b = None):
        if operando_b == None:
            self.__acumulador += operando_a 
        else:
            self.__acumulador = operando_a + operando_b
        return self.__acumulador
    
    def subtrair(self, operando_a, operando_b = None):
        if operando_b == None:
            self.__acumulador -= operando_a 
        else:
            self.__acumulador = operando_a - operando_b
        return self.__acumulador
    
    def multiplicar(self, operando_a, operando_b = None):
        if operando_b == None:
            self.__acumulador = self.__acumulador * operando_a 
        else:
            self.__acumulador = operando_a * operando_b
        return self.__acumulador
    
    def dividir(self, operando_a, operando_b=None):
        if operando_b == 0:
            return 'OPERAÇÃO INVÁLIDA'
        elif operando_b == None:
            self.__acumulador = self.__acumulador / operando_a
        else:
            self.__acumulador = operando_a / operando_b
        return self.__acumulador
        
        