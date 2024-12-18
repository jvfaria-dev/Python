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

def verificarSimetria(matriz):
    for i in range(len(matriz)):
        for j in range(i, len(matriz[0])):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

if __name__ == "__main__":
    linhas = inputInt("Linhas da matriz: ")
    colunas = inputInt("Colunas da matriz: ")
    matriz = [inputListInt(f"Elementos da linha {i+1}: ") for i in range(linhas)]

    if linhas != colunas:
        print("A matriz não é quadrada, portanto, não pode ser simétrica.")
    elif verificarSimetria(matriz):
        print("A matriz é simétrica em relação à diagonal principal.")
    else:
        print("A matriz não é simétrica em relação à diagonal principal.")
