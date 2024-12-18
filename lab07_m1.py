def separa(frase, caractere_separador=" "):
    return frase.split(caractere_separador)

def junta(lista_palavras, caractere_aglutinador=", "):
    return caractere_aglutinador.join(lista_palavras)

sequencia = input("Digite uma sequência de palavras separadas por um caractere específico: ")
caractere_separador = input("Digite o caractere separador: ")

lista_palavras = separa(sequencia, caractere_separador)
print("Lista de palavras separadas:", lista_palavras)

caractere_aglutinador = input("Digite o caractere aglutinador para unir as palavras (padrão: ', '): ")

if caractere_aglutinador == "":
    caractere_aglutinador = ", "

frase_junta = junta(lista_palavras, caractere_aglutinador)
print("Frase juntada novamente:", frase_junta)