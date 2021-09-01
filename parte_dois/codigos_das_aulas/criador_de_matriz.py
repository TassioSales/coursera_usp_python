def cria_matriz(numero_linhas, numero_colunas):
    """[summary]
    (int, int) -> matriz(lista de listas)
    Cria e retorna uma matriz com numero_linha e numero_colunas em que cada elemento e digitado pelo usuario 

    Args:
        numero_linhas ([int]): [numero de linha da matrix]
        numero_colunas ([int]): [numero de colunas da matrix]
    """

    matriz  = [] # lista vazia
    for i in range(numero_linhas):
        #cria a linha i
        linha = [] #lista vazia
        for j in range(numero_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]: "))
            linha.append(valor)

        #adicona linha à matrix
        matriz.append(linha)
    
    return matriz

def ler_matriz():
    linhas = int(input("Digite o numero de linha da matriz:  "))
    colunas = int(input("Digite o numero de colunas da matriz: "))
    return cria_matriz(linhas, colunas)

teste = ler_matriz()

for linha in teste:
    print(linha)
