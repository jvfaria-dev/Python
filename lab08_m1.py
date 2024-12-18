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

def criarMatriz():
    linhas = inputInt("Informe o número de linhas da matriz: ")
    colunas = inputInt("Informe o número de colunas da matriz: ")
    print("Informe os elementos da matriz separados por vírgula:")
    elementos = inputListInt("")

    if len(elementos) != linhas * colunas:
        print("Número incorreto de elementos fornecidos.")
        return None

    matriz = []
    for i in range(linhas):
        linha = []
        for c in range(colunas):
            linha.append(elementos[i * colunas + c])
        matriz.append(linha)

    return matriz
matriz = criarMatriz()
if matriz:
    print("Matriz criada:")
    printMatriz(matriz)
