
def inserir_novo_item(lista_frutas):
    nova_fruta = input("Insira uma fruta: ")

    if nova_fruta not in lista_frutas:
        #lista_frutas.append(nova_fruta)
        lista_frutas.insert(1,nova_fruta)
    else:
        print("A fruta já existe na lista")
    
    print(lista_frutas)
    # método sort() usado para ordenar a lista lista_frutas
    lista_frutas.sort()

    return lista_frutas


def main():
    lista_frutas = ["maçã", "uva", "pera"]
    lista_ordenada = inserir_novo_item(lista_frutas)
    print(lista_ordenada)

if __name__ == "__main__":
    main()