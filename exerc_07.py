
# função criada para exibir os extremos obtidos em cada período
def exibir_temperaturas_max_e_min(lista_final):
    
     # Verifica se lista_final tem pelo menos uma sublista
    if (lista_final and len(lista_final) >= 3):
        # Verifica e exibir temperaturas da manhã
        if((len(lista_final[0]) >= 2) and (lista_final[0][0] != "") and (lista_final[0][1] != "")):
            print("\nMenor temperatura manha: ",lista_final[0][1])
            print("Maior temperatura manha: ",lista_final[0][0])

        # Verifica e exibi temperaturas da tarde
        if ((len(lista_final) >= 2) and (len(lista_final[1]) >= 2) and (lista_final[1][0] != "") and (lista_final[1][1] != "")):
            print("\nMenor temperatura tarde: ",lista_final[1][1])
            print("Maior temperatura tarde: ",lista_final[1][0])

        # Verifica e exibi temperaturas da noite
        if ((len(lista_final) >= 3) and (len(lista_final[2]) >= 2) and (lista_final[2][0] != "") and (lista_final[2][1] != "")):
            print("\nMenor temperatura noite: ",lista_final[2][1])
            print("Maior temperatura noite: ",lista_final[2][0])
    

# função criada definir as temperaturas e períodos
def obter_temperaturas():
    lista_final = []
    opcao = 0
    temperaturas_manha = []
    temperaturas_tarde = []
    temperaturas_noite = []

    while (opcao != 4):

        print("\n =-- Escolhe algum dos períodos --= ")
        print(" 1 - Para Manhã")
        print(" 2 - Para Tarde")
        print(" 3 - Para Noite")
        print(" 4 - Sair")

        opcao = int(input())

        if opcao == 1:
            print("Informe quantas temperaturas serão cadastradas")
            qtd_temp = int(input())

            for i in range (qtd_temp):
                temp = float(input("Digite a temperatura da manhã: "))    
                temperaturas_manha.append(temp)

        elif opcao == 2:
            print("Informe quantas temperaturas serão cadastradas")
            qtd_temp = int(input())
            for i in range (qtd_temp):
                temp = float(input("Digite a temperatura da tarde: "))
                temperaturas_tarde.append(temp)
            
        elif opcao == 3:
            print("Informe quantas temperaturas serão cadastradas")
            qtd_temp = int(input())
            for i in range (qtd_temp):
                temp = float(input("Digite a temperatura da noite: "))
                temperaturas_noite.append(temp)
        elif opcao == 4:
            print("Processando...")
        else:
            print("Período inválido !!!")
        

    lista_final = encontrar_extremos(temperaturas_manha, temperaturas_tarde, temperaturas_noite)
    exibir_temperaturas_max_e_min(lista_final)


    
# Função criada para encontrar e devolver os extremos de cada período
def encontrar_extremos(temperaturas_manha, temperaturas_tarde, temperaturas_noite):
    lista_final = []
    sub_lista_manha = []
    sub_lista_tarde = []
    sub_lista_noite = []

    # condição para verificar se a lista está vazia
    if(temperaturas_manha):
        # encontrar extremos temperaturas manha
        temp_manha_max = max(temperaturas_manha)
        temp_manha_min = min(temperaturas_manha)
        #adiciona a maior e a menor temperatura na sub lista
        sub_lista_manha.append(temp_manha_max)
        sub_lista_manha.append(temp_manha_min)

    # condição para verificar se a lista está vazia
    if(temperaturas_tarde):
        # encontrar extremos temperaturas tarde
        temp_tarde_max = max(temperaturas_tarde)
        temp_tarde_min = min(temperaturas_tarde)
        #adiciona a maior e a menor temperatura na sub lista
        sub_lista_tarde.append(temp_tarde_max)
        sub_lista_tarde.append(temp_tarde_min)

    # condição para verificar se a lista está vazia
    if(temperaturas_noite):
        # encontrar extremos temperaturas noite
        temp_noite_max = max(temperaturas_noite)
        temp_noite_min = min(temperaturas_noite)
        #adiciona a maior e a menor temperatura na sub lista
        sub_lista_noite.append(temp_noite_max)
        sub_lista_noite.append(temp_noite_min)

    #adicionar a lista final as sublistas
    lista_final = [sub_lista_manha] + [sub_lista_tarde] + [sub_lista_noite]
    
    return lista_final


def main():
    obter_temperaturas()
   
if __name__ == "__main__":
    main()
