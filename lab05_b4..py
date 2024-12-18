def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


entrada = int(input("Digite o número do elemento que você deseja saber: "))
numero = entrada + 1

resultado = fibonacci(numero)
print("O {} elemento é o {}".format(entrada, resultado))

