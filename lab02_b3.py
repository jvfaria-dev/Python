import math

def calcular_raizes(a, b, c):

    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("Não existe raiz real.")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"Há uma raiz real: {raiz:.2e}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"As raízes reais são: {raiz1:.2e} e {raiz2:.2e}")

def main():

    a = float(input("Digite o coeficiente 'a': "))
    b = float(input("Digite o coeficiente 'b': "))
    c = float(input("Digite o coeficiente 'c': "))

    calcular_raizes(a, b, c)

if __name__ == "__main__":
    main()
