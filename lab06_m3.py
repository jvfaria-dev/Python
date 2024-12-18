def filtro(predicado, lista):
    lista_filtrada = []
    for i in lista:
        if predicado(i):
            lista_filtrada.append(i)
    return lista_filtrada

def eh_par(numero):
    return numero % 2 == 0

def eh_impar(numero):
    return numero % 2 != 0

entrada = input("Digite uma sequência de números separados por vírgula: ")

numeros = [int(numero.strip()) for numero in entrada.split(',') if numero.strip().isdigit()]

numeros_pares = filtro(eh_par, numeros)
numeros_impares = filtro(eh_impar, numeros)

print("Os números pares são:", numeros_pares)
print("Os números ímpares são:", numeros_impares)