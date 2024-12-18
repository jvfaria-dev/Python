def soma_digitos(n):
    if n < 10:
        return n
    return n % 10 + soma_digitos(n // 10)

numero = int(input("Digite um número inteiro positivo: "))
while numero <= 0:
    print("Por favor, digite um número inteiro positivo válido.")
    numero = int(input("Digite um número inteiro positivo: "))

resultado = soma_digitos(numero)
print(f"A soma dos dígitos de {numero} é: {resultado}")