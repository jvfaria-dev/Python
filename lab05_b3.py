def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)
    
numero = int(input("Digite um número para que possa ser calculado o fatorial: "))
if numero < 0:
    print("Insira um número inteiro posítivo.")

resultado = fatorial(numero)
print("O fatorial de {} é igual à {}.".format(numero, resultado))
