try:
    numero = int(input("Digite um número inteiro: "))
    soma_digitos = 0

    while numero > 0:
        digito = numero % 10
        soma_digitos += digito
        numero //= 10

    print("A soma dos dígitos do número é:", soma_digitos)

except ValueError:
    print("Por favor, digite um número inteiro válido.")
