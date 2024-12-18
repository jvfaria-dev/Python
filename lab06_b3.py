def minl(lista):
    minimo = lista[0]
    for i in lista[1:]:
        if i < minimo:
            minimo = i
    return minimo

def maxl(lista):
    maximo = lista[0]
    for i in lista[1:]:
        if i > maximo:
            maximo = i
    return maximo

entrada = input("Digite uma sequência de números separados por vírgula: ")

numeros = [int(numero.strip()) for numero in entrada.split(',') if numero.strip().isdigit()]

numero_minimo = minl(numeros)
numero_maximo = maxl(numeros)

print("Elemento mínimo:", numero_minimo)
print("Elemento máximo:", numero_maximo)
