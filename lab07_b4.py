def reverte(frase):
    frase_revertida = ""
    for i in frase:
        frase_revertida = i + frase_revertida
    return frase_revertida

frase = input("Digite uma palavra ou frase: ")

print("Frase invertida:", reverte(frase))
