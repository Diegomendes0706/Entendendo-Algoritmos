estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

estacoes = {"kum": set(["id", "nv", "ut"]), "kdois": set(["wa", "id", "mt"]), "ktres": set(["or", "nv", "ca"]),
            "kquatro": set(["nv", "ut"]), "kcinco": set(["ca", "az"])}

estacoes_finais = set()

while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()
    for estacao, estados_por_estacao in estacoes.items():
        cobertos = estados_abranger & estados_por_estacao
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos
    estados_abranger -= estados_cobertos
    estacoes_finais.add(melhor_estacao)


print(estacoes_finais)