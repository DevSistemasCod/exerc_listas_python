
def definir_lista(tamanho_lista):
    lista_pares = []
    lista_impares = []
    lista_final = []
    
    for i in range (tamanho_lista):
        numero = int(input(f"Entre com o número {i}: "))
        resto = numero % 2
        if(resto == 0):
            lista_pares.append(numero)
        else:
            lista_impares.append(numero)

    #cria a lista_final com as sublistas lista_pares e lista_impares
    lista_final = [lista_pares] + [lista_impares]
    return lista_final

def main():
    tamanho_lista = int(input(" Informe o tamanho da lista: "))
    lista = definir_lista(tamanho_lista)
    
    #considerando a lista "lista"
    # é possivel obter a primeira sublista com [0]
    print("Números Pares: ",lista[0])
    # é possivel obter a segunda sublista com [1]
    print("Números Ímpares: ",lista[1])

if __name__ == "__main__":
    main()