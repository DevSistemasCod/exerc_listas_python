
def adicionar_palavra(qtd_palavras):
    lista_palavras = []

    for i in range(qtd_palavras):
        palavra = input("Entre com a palavra: ")
        lista_palavras.append(palavra)
    
    # método reverse() usando para invernter
    lista_palavras.reverse()
    #possibilidade 2 use lista_palavras[::-1] para invernter a lista
    return lista_palavras

def main():
    lista_invertida = []

    qtd_palavras = int(input("Informe a quantidade de palavras: "))
    lista_invertida = adicionar_palavra(qtd_palavras)
    print(lista_invertida)

if __name__ == "__main__":
    main()