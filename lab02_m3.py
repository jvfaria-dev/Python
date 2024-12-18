def main():
    
    numeros = []
    for i in range(3):
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        numeros.append(numero)

    pares = 0
    impares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")

    if pares > impares:
        print("A maioria dos números é par.")
    elif impares > pares:
        print("A maioria dos números é ímpar.")
    else:
        print("O mesmo número de números pares e ímpares foi inserido.")

if __name__ == "__main__":
    main()
