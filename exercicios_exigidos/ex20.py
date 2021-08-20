def remove_repetidos(lista):
    dados = []
    for num in lista:
        if num not in dados:
            dados.append(num)
    dados.sort()
    return dados