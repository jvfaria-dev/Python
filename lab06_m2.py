def soma_acumulada(lista):
    soma_acumulada = []
    count = 0
    for i in lista:
        count += i
        soma_acumulada.append(count)
    return soma_acumulada

entrada = input("Digite uma sequência de números separados por vírgula: ")

numeros = [int(numero.strip()) for numero in entrada.split(',') if numero.strip().isdigit()]

soma_acumulada_lista = soma_acumulada(numeros)

print("Lista original:", numeros)
print("Lista da soma acumulada:", soma_acumulada_lista)

