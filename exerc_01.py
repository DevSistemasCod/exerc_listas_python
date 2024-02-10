
# Adicionar na última posição
def adicionar_na_ultima_posicao(lista):
    numero = int(input(f"Informe um número para a última posição: "))
    lista.append(numero)
    return lista

# Adicionar na primeira posição
def adicionar_na_primeira_posicao(lista):
    numero = int(input(f"Informe um número para a primeira posição: "))
    lista.insert(0,numero)
    return lista


# Adicionar itens na lista
def adicionar_itens(qtd_numeros):
    lista_numeros =[]

    for i in range(qtd_numeros):
        numero = int(input(f"Número de posição {i}: "))
        lista_numeros.append(numero)
    
    return lista_numeros

# Exibir itens da lista
def imprimir_lista(lista):
        print("Lista: ",lista)

# Remover item na segunda posição da lista
def remover_na_segunda_posicao(lista):
    lista.pop(1)
    return lista

def main():
    qtd_numeros = int(input("Informe a quantidade: "))
    lista = adicionar_itens(qtd_numeros)
    imprimir_lista(lista)
    
    lista = adicionar_na_ultima_posicao(lista)
    lista = adicionar_na_primeira_posicao(lista)
    imprimir_lista(lista)
    
    lista = remover_na_segunda_posicao(lista)
    print("Lista após remover a 2ª posição")
    imprimir_lista(lista)

if __name__ == "__main__":
    main()