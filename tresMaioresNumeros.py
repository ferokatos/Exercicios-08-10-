def ordenarNumeros(lista):
    lista.sort()
    return lista

def TresMaiores(lista):
    topTree = []
    for i in range(3):
        for p,i in enumerate(lista):
            if p == 0:
                maior = i
            elif maior < i:
                maior = i
        topTree.append(maior)
        lista.remove(maior)
    topTree.sort(reverse=True)
    return topTree


lista = [42, 12, 9, 73, 51, 22]
lista = ordenarNumeros(lista)
print(lista)
topTree = TresMaiores(lista)
print(topTree)