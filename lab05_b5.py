def div(dividendo, divisor):
    if divisor == 0:
        return None, None
    else:
        quociente = dividendo / divisor
        resto = dividendo % divisor
        return quociente, resto

dividendo = int(input("Digite o número para o dividendo: "))
divisor = int(input("Digite o número para o divisor: "))

quociente, resto = div(dividendo, divisor)
if divisor == 0:
    print("Não consigo dividir um dividendo por 0")
else: 
    print("O resultado da divisão de {} por {} é igual à {} e o resto é igual à {}".format(dividendo, divisor, quociente, resto))
