def tamanho(lista):
    count = 0
    for i in lista:
        count += 1
    return count

entrada = input("Digite uma sequência de números separados por vírgula: ")

numeros = entrada.split(',')
numeros = [int(numero.strip()) for numero in numeros if numero.strip().isdigit()]

tamanho_lista = tamanho(numeros)

print("Lista válida:", numeros)
print("Tamanho da lista:", tamanho_lista)
