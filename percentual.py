def calcperc(faturaestado):
    totfatura = sum(faturaestado.values())
    percentualrep = {}
    for estado, faturamento in faturaestado.items():
        percentual = (faturamento / totfatura) * 100
        percentualrep[estado] = percentual
    return percentualrep

def main():
    faturaestado = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }
    
    percentualrep = calcperc(faturaestado)
    print("Percentual de representação de cada estado no faturamento total:")
    for estado, percentual in percentualrep.items():
        print(f"{estado}: {percentual:.2f}%")
nome = 'teste'
if nome == "teste":
    main()
