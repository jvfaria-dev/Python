limite = int(input("Digite um número inteiro limite: "))
numeros_intervalo = ""
for i in range(limite + 1):
    if i < limite:
        numeros_intervalo += str(i) + ", "
    else:
        numeros_intervalo += str(i)
print(numeros_intervalo)