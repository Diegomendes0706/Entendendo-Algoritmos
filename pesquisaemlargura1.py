from collections import deque


def pessoa_e_vendedor(nome):
    return nome[0] == 'B' or nome[0] == 'F'


def busca_mango_vendedor(grafo, nome):
    fila = deque()
    fila += grafo[nome]
    verificadas = []
    while fila:
        pessoa = fila.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + " é vendedor de manga")
            else:
                fila += grafo[pessoa]
                verificadas.append(pessoa)


# grafo de exemplo
grafo = {
    "voce": ["Bob", "Charlie"],
    "Bob": ["David", "Eva"],
    "Charlie": ["Frank", "Grace"],
    "David": [],
    "Eva": ["Isaac"],
    "Frank": [],
    "Grace": [],
    "Isaac": []
}

# chama a função com um nó inicial
busca_mango_vendedor(grafo, "voce")
