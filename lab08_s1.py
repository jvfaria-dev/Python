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
    for linha in matriz:
        print("|", end=" ")
        for elemento in linha:
            print(f"{elemento:^6}", end=" ")
        print("|")

def multiplicaMatriz(matriz1, matriz2):
    result = [[0] * len(matriz2[0]) for _ in range(len(matriz1))]
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                result[i][j] += matriz1[i][k] * matriz2[k][j]
    return result

if __name__ == "__main__":
    linhas1 = inputInt("Linhas da primeira matriz: ")
    colunas1 = inputInt("Colunas da primeira matriz: ")
    matriz1 = [inputListInt("Elementos da linha {}: ".format(i+1)) for i in range(linhas1)]

    linhas2 = inputInt("Linhas da segunda matriz: ")
    colunas2 = inputInt("Colunas da segunda matriz: ")
    matriz2 = [inputListInt("Elementos da linha {}: ".format(i+1)) for i in range(linhas2)]

    if colunas1 != linhas2:
        print("As matrizes não podem ser multiplicadas.")
    else:
        resultado = multiplicaMatriz(matriz1, matriz2)
        print("\nResultado da multiplicação das matrizes:")
        printMatriz(resultado)