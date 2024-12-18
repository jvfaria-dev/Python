def reverter(lista):
    lista_revertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_revertida.append(lista[i])
    return lista_revertida

entrada = input("Digite uma sequência de números separados por vírgula: ")

numeros = [int(numero.strip()) for numero in entrada.split(',') if numero.strip().isdigit()]

lista_revertida = reverter(numeros)

print("Lista original:", numeros)
print("Lista após reversão:", lista_revertida)