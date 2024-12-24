#from matematica import aritmetica
#from matematica import geometria
import matematica as mat
from matematica.estatistica import media

def testeAritmetica(n1,n2):
    som = f"Soma de {n1} e {n2} = {mat.soma(n1,n2)}"
    sub = f"Subtração de {n1} e {n2} = {mat.subtracao(n1,n2)}"
    return som, sub

def testeGeo1(raio):
    circulo = f"A área do círculo de raio {raio} é igual a {mat.areaCirculo(raio)}"
    return circulo

def testeGeo2(alt,lar):
    retangulo = f"A área do retângulo de altura {alt} e largura {lar} é igual a {mat.areaRetangulo(alt,lar)}"
    return retangulo

def testeEstat(lista):
    return media.media_simples(lista)

print(testeAritmetica(9,4))
print(testeGeo1(7))
print(testeGeo2(10,4))
print(testeEstat([3,6,12]))