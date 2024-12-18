def atribuir_conceito(nota):

    if nota >= 90:
        return "A"
    elif nota >= 75:
        return "B"
    elif nota >= 60:
        return "C"
    elif nota >= 40:
        return "D"
    else:
        return "F"

def main():

    nota = float(input("Digite sua nota (em uma escala de 0 a 100): "))

    conceito = atribuir_conceito(nota)

    print(f"Seu conceito é: {conceito}")

if __name__ == "__main__":
    main()
