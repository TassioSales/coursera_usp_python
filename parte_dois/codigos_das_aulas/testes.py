def tarefa(mat):
    dim = len(mat)
    for i in range(dim):
        print(mat[i][dim-1-i], end="  ")

def dimensoes(matrix):
    linhas = len(matrix)
    colunas = len(matrix[0])
    return print(f'{linhas} x {colunas}')

def soma_matrizes(m1, m2):
    if dimensoes(m1) != dimensoes(m2):
        return False
    else:
        matriz = []
        for i in range(len(m1)):
            linha = []
            for j in range(len(m1[0])):
                linha.append(m1[i][j] + m2[i][j])
            matriz.append(linha)
        return matriz

mat = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[1,2,3],[4,5,6],[7,8,9]]
tarefa(mat)

dimensoes(mat)
teste = soma_matrizes(mat, mat2)
print(teste)