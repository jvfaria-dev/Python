def calcular_imposto(valor_compra, estado_destino):

    if estado_destino == "MG":
        percentual_imposto = 0.07
    elif estado_destino == "SP":
        percentual_imposto = 0.12
    elif estado_destino == "RJ":
        percentual_imposto = 0.15
    elif estado_destino == "ES":
        percentual_imposto = 0.08
    else:
        return None 

    imposto = valor_compra * percentual_imposto
    return imposto

def main():

    valor_compra = float(input("Informe o valor da compra: "))
    estado_destino = input("Informe a sigla do estado de destino (MG, SP, RJ, ES): ").upper()

    if valor_compra <= 0:
        print("O valor da compra deve ser um número positivo.")
        return

    imposto = calcular_imposto(valor_compra, estado_destino)

    if imposto is not None:
        total_pago = valor_compra + imposto
        print(f"Total a ser pago (incluindo imposto): R$ {total_pago:.2f}")
    else:
        print("Estado de destino não reconhecido. Por favor, corrija a entrada.")

if __name__ == "__main__":
    main()
