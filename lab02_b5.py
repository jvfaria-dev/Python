def main():

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = input("Escolha a operação desejada (+ para soma, - para subtração, * para multiplicação, / para divisão): ")

    if operacao == '+':
        resultado = numero1 + numero2
        print(f"O resultado da soma é: {resultado}")
    elif operacao == '-':
        resultado = numero1 - numero2
        print(f"O resultado da subtração é: {resultado}")
    elif operacao == '*':
        resultado = numero1 * numero2
        print(f"O resultado da multiplicação é: {resultado}")
    elif operacao == '/':
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Não é possível dividir por zero.")
    else:
        print("Operação não reconhecida.")

if __name__ == "__main__":
    main()
