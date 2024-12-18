def classificar_triangulo(lado1, lado2, lado3):

    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:

        if lado1 == lado2 == lado3:
            return "Triângulo Equilátero"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"
    else:
        return "Os lados fornecidos não formam um triângulo."

def main():

    lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
    lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
    lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

    resultado = classificar_triangulo(lado1, lado2, lado3)
    print(resultado)

if __name__ == "__main__":
    main()
