sequencia = input("Digite uma sequência de números separados por vírgula: ")
numeros = sequencia.split(',')

for numero_str in numeros:
    try:
        numero = int(numero_str)
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
    except ValueError:
        print(f"\"{numero_str}\" não é um número válido.")
