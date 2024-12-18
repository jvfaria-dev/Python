entrada = input("Digite uma sequencia de números separados por vírgula: ")
numeros = sorted([int(numero) for numero in entrada.split(",")])
numeros_reverso = numeros[::-1]

print("Ordem crescente: {}".format(numeros_reverso))