entrada = input("Digite uma sequência de números inteiros separados por vírgula: ")
numeros = [int(numero) for numero in entrada.replace(" ", "").split(",")]

print("Lista inicial:", numeros)

retirado = int(input("Escolha um número da lista para remover: "))

if retirado in numeros:
    numeros.remove(retirado)
    print("Número removido. Lista atualizada:", numeros)
else:
    print("O número escolhido não está presente na lista.")
