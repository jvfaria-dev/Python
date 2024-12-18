def busca(elemento, lista):
    for i, num in enumerate(lista):
        if num == elemento:
            return i
    return -1

entrada = input("Digite uma sequência de números separados por vírgula: ")

numeros = [int(numero.strip()) for numero in entrada.split(',') if numero.strip().isdigit()]

elemento = int(input("Digite o número que deseja encontrar na lista: "))

indice = busca(elemento, numeros)

if indice != -1:
    print("O número {} é encontrado no índice {} da lista.".format(elemento,indice))
else:
    print("O número {} não foi encontrado na lista.".format(elemento))

