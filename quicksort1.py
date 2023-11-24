def soma(lista):
    if not lista:
        return 0
    return lista[0] + soma(lista[1:])


