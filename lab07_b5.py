def substitui_letra(frase, substitui, substituida):
    frase_substituida = ""
    for i in frase:
        if i == substitui:
            frase_substituida += substituida
        else:
            frase_substituida += i
    return frase_substituida

frase = input("Digite uma frase: ")
substitui = input("Digite uma letra a ser substituída: ")
substituida = input("Digite uma letra para substituir: ")

print(f"A frase substituída é: {substitui_letra(frase, substitui, substituida)}")
