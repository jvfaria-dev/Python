def maiusculas(frase):
    resultado = ""
    for i in frase:
        if 'a' <= i <= 'z':
            resultado += chr(ord(i) - 32)
        else:
            resultado += i
    return resultado

def minusculas(frase):
    resultado = ""
    for i in frase:
        if 'A' <= i <= 'Z':
            resultado += chr(ord(i) + 32)
        else:
            resultado += i
    return resultado

frase = input("Digite uma palavra ou frase: ")

print("Versão em maiúsculas:", maiusculas(frase))
print("Versão em minúsculas:", minusculas(frase))
