numero = int(input('Digite um número inteiro posítivo: '))

for i in range(1, numero + 1):
    linha = ' '.join(str(i) for _ in range(i))
    print(linha)
