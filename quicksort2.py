def contar(lista):
    if not lista:
        return 0
    return 1 + contar(lista[1:])
