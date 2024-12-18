def inputInt(msg):
    while True:
        numero = input(msg)
        if numero.isnumeric():
            numero = int(numero)
            break
    return numero

def inputListInt(msg):
    if not "vírgula" in msg:
        msg += " [separação por vírgulas] "
    lista = list()
    while True:
        numeros = input(msg).split(',')
        for i in range(len(numeros)):
            if numeros[i].strip().isnumeric():
                lista.append(int(numeros[i].strip()))
        if len(lista) > 0:
            break
    return lista

def printMatriz(matriz):
    m, n = len(matriz), len(matriz[0])
    for i in range(m):
        print("|", end=" ")
        for j in range(n):
            print(f"{str(matriz[i][j]):^6s}", end=" ")
        print("|")

def criarMatriz(linhas, colunas):
    print(f"Informe os elementos da matriz {linhas}x{colunas} separados por vírgula:")
    elementos = inputListInt("")
    if len(elementos) != linhas * colunas:
        print("Número incorreto de elementos fornecidos.")
        return None
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(elementos[i * colunas + j])
        matriz.append(linha)
    return matriz

def transposta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def somaMatrizes(matriz1, matriz2):
    return [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]

if __name__ == "__main__":
    linhas1 = inputInt("Informe o número de linhas da primeira matriz: ")
    colunas1 = inputInt("Informe o número de colunas da primeira matriz: ")
    matriz1 = criarMatriz(linhas1, colunas1)

    linhas2 = inputInt("Informe o número de linhas da segunda matriz: ")
    colunas2 = inputInt("Informe o número de colunas da segunda matriz: ")
    matriz2 = criarMatriz(linhas2, colunas2)

    if matriz1 and matriz2 and linhas1 == colunas2 and colunas1 == linhas2:
        print("Matriz 1:")
        printMatriz(matriz1)

        print("\nMatriz 2:")
        printMatriz(matriz2)

        transposta_matriz2 = transposta(matriz2)
        print("\nTransposta da Matriz 2:")
        printMatriz(transposta_matriz2)

        soma_transposta = somaMatrizes(matriz1, transposta_matriz2)
        print("\nSoma da Matriz 1 com a Transposta da Matriz 2:")
        printMatriz(soma_transposta)
    else:
        print("As matrizes não possuem dimensões compatíveis.")
