def separa(frase, caractere_separa=" "):
    return frase.split(caractere_separa)

def junta(palavras, caractere_junta=" "):
    return caractere_junta.join(palavras)

def soLetrasNumerosEspacos(frase):
    caracteres_permitidos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    return ''.join(char for char in frase if char in caracteres_permitidos)

def trocaOrdemCadaDuasPalavras(palavras):
    nova_palavras = []
    for i in range(0, len(palavras), 2):
        if i + 1 < len(palavras):
            nova_palavras.append(palavras[i + 1])
            nova_palavras.append(palavras[i])
        else:
            nova_palavras.append(palavras[i])
    return nova_palavras

frase = input("Digite uma frase: ")
frase = frase.upper()

frase_recebida = soLetrasNumerosEspacos(frase)
palavras = separa(frase_recebida)

palavras_trocadas = trocaOrdemCadaDuasPalavras(palavras)
frase_final = junta(palavras_trocadas)

print("Frase após a troca de ordem de cada duas palavras consecutivas:")
print(frase_final)
