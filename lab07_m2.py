from unicodedata import unidata_version

def reverte(frase):
    return frase[::-1]

def soLetrasNumerosMaiusculas(frase):
    frase_processada = ""
    for char in frase:
        if char.isalnum():
            frase_processada += char.upper()
    return frase_processada

def ehPalindromo(frase):
    frase_processada = soLetrasNumerosMaiusculas(frase)
    return frase_processada == reverte(frase_processada)

frase = input("Digite uma frase: ")

if ehPalindromo(frase):
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
