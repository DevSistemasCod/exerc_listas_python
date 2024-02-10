
# método utilizado para inserir uma cor
def inserir_cores(tamanho_lista):
    lista_cor = []

    for i in range(tamanho_lista):
        cor = input(f"Entre com um nome de cor {i}: ")
        if cor not in lista_cor:
            lista_cor.append(cor)
    
    return lista_cor

def main():
    TAM_MAX = 5

    tamanho_lista = TAM_MAX
    lista_cores = inserir_cores(tamanho_lista)
    print(lista_cores)
    print("A partir do terceiro elemento",lista_cores[2:])

    #divisão da lista_cores em lista1 e lista2 
    lista1 = lista_cores[:2]
    lista2 = lista_cores[2:]

    print("Lista 1: ",lista1)
    print("Lista 2: ",lista2)

if __name__ == "__main__":
    main()