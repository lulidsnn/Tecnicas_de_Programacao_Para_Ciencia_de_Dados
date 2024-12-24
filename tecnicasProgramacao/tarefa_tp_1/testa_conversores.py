import conversores as conv

def testeCparaF(tempC):
    cTof = f"A temperatura {tempC}°C equivale a {conv.celsius_para_fahrenheit(tempC)}°F"
    return cTof

def testeFparaC(tempF):
    fToc = f"A temperatura {tempF}°F equivale a {conv.fahrenheit_para_celsius(tempF)}°C"
    return fToc

def testeMparaP(medidaMetro):
    mTop = f"O comprimento {medidaMetro}m equivale a {conv.metro_para_pes(medidaMetro)} pés."
    return mTop

def testePparaM(medidaPes):
    pTom = f"O comprimento {medidaPes} pés equivale a {conv.pes_para_metro(medidaPes)}m"
    return pTom

def testeKMparaMIL(dKm):
    kTom = f"A distância {dKm}km equivale a {conv.quilometro_para_milhas(dKm)} milhas"
    return kTom

def testeMILparaKM(dMil):
    mTok = f"A distância {dMil} milhas equivale a {conv.milhas_para_quilometros(dMil)} quilômetros"
    return mTok
    
def testeDiasparaHoras(dias):
    dToh = f"{dias} dia(s) em horas é: {conv.dia_para_horas(dias)}h"
    return dToh

print(testeCparaF(29))
print(testeFparaC(84.2))
print(testeMparaP(80))
print(testePparaM(80))
print(testeKMparaMIL(15))
print(testeMILparaKM(15))
print(testeDiasparaHoras(3))