def main():
    
    numero = int(input("Digite um número inteiro: "))
    
    if numero % 2 == 0:
        print("O número é par e também um múltiplo de 2.")
    else:
        print("O número é ímpar.")
    
    if numero % 3 == 0:
        print("O número é um múltiplo de 3.")
    else:
        print("O número não é um múltiplo de 3.")
    
    if numero % 5 == 0:
        print("O número é um múltiplo de 5.")
    else:
        print("O número não é um múltiplo de 5.")
    
    if numero % 7 == 0:
        print("O número é um múltiplo de 7.")
    else:
        print("O número não é um múltiplo de 7.")

if __name__ == "__main__":
    main()
