def comb(n, k):
    def fatorial(num):
        if num == 0:
            return 1
        return num * fatorial(num - 1)    
    return fatorial(n) // (fatorial(k) * fatorial(n - k))

elementos = int(input("Informe o total de elementos (n): "))
coeficiente = int(input("Informe a quantidade de elementos a escolher (k): "))

if coeficiente > elementos:
    print("A quantidade de elementos a escolher não pode ser maior que o total de elementos.")
else:
    resultado = comb(elementos, coeficiente)
    print(f"O número de combinações possíveis é: {resultado}")
