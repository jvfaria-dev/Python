def soma(lista):
    count = 0
    for i in lista:
        count += i
    return count

entrada = input("Digite uma sequência de números separados por vírgula: ")

numeros = entrada.split(',')
numeros = [int(numero.strip()) for numero in numeros if numero.strip().isdigit()]

resultado = soma(numeros)

print("Lista válida:", numeros)
print("Soma dos elementos:", resultado)