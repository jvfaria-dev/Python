sequencia = input("Digite uma sequência de números separados por vírgula: ")
numeros = [int(numero.strip()) for numero in sequencia.split(',')]
soma = sum(numeros)
print("A soma dos números é:", soma)
