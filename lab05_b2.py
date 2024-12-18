def limites(*args):
    return min(args), max(args)

entrada = input("Digite números separados por vírgula: ")
numeros = [int(numero) for numero in entrada.split(',')]

minimo, maximo = limites(*numeros)

print("O valor mínimo é {}.".format(minimo))
print("O valor máximo é {}.".format(maximo))