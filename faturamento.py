def calcular_faturamento(faturamento_diario):
    if not faturamento_diario:
        return None, None, 0

    menor_valor = min(faturamento_diario)
    maior_valor = max(faturamento_diario)
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)
    
    dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)
    
    return menor_valor, maior_valor, dias_acima_media

def prin():
    faturamento_diario = [22174.1664, 24537.6698, 26139.6134, 26742.6612, 42889.2258, 46251.174, 11191.4722, 
                          3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 35240.1826, 43829.1667, 
                          18235.6852, 4355.0662, 13327.1025, 25681.8318, 1718.1221, 13220.495, 8414.61]

    menor_valor, maior_valor, dias_acima_media = calcular_faturamento(faturamento_diario)
    
    print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")

nome = 'teste'
if nome == "teste":
    prin()
