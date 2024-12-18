entrada = input("Digite uma sequencia de números separados por vírgula: ")
numeros = sorted([int(numero) for numero in entrada.split(",")])

print("Ordem crescente: {}".format(numeros))