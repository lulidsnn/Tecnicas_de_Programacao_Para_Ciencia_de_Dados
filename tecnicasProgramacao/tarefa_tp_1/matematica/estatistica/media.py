def media_simples(listaNum):
    soma = 0
    for i in range(len(listaNum)):
        soma += listaNum[i]
    media = f"A média dos valores da lista é {soma/len(listaNum)}"
    return media

'''lista = [3,6,9]
print(media_simples(lista))'''