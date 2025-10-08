def criar_pessoa(nome,idade,id):
    dicionario = {"nome":nome,"idade":idade,"id":id}
    return dicionario
p1 = criar_pessoa("Marcos", 28, 1)
p2 = criar_pessoa("Ana", 24, 2)
p3 = criar_pessoa("Carlos", 30, 3)
print(p1)