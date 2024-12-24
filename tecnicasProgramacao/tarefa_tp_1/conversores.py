def celsius_para_fahrenheit(tempCelsius):
    tempFah = (tempCelsius * 1.8) + 32
    return tempFah

def fahrenheit_para_celsius(tempFahrenheit):
    tempCel = (tempFahrenheit - 32)/1.8
    return tempCel

def metro_para_pes(medMetro):
    if medMetro < 0:
        print("Medida inválida!")
    else:
        medidaPes = medMetro * 3.28
        return medidaPes

def pes_para_metro(medPes):
    if medPes < 0:
        print("Medida inválida!")
    else:
        medidaMetro = medPes / 3.28
        return medidaMetro

def quilometro_para_milhas(km):
    if km < 0:
        print("Número inválido!")
    else:
        medidaMilha = km * 0.6214
    return medidaMilha

def milhas_para_quilometros(mil):
    if mil < 0:
        print("Número inválido!")
    else:
        medidaKm = mil * 1.6093
    return medidaKm

def dia_para_horas(qtdeDias):
    if qtdeDias < 0:
        print("Número inválido!")
    else:
        horas = qtdeDias * 24
    return horas