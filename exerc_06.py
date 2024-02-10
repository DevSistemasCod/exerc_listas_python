# Crie uma lista m de alunos com uma quantidade n de notas. 
# Calcule a média dessas notas e gere duas listas 
# uma de alunos aprovados e outra de alunos  reprovados.


def calcular_media(qtd_alunos,qtd_notas):
    lista_aprovados = []
    lista_reprovados = []
    somatoria_notas = 0
    media = 0
    NOTA_APROVACAO = 5

    for i in range(1,qtd_alunos+1):
        # somatoria_notas deve ser zerada para o próximo cálculo
        somatoria_notas = 0
        for j in range(qtd_notas):
            nota = float(input(f"Informe a nota{j} do aluno{i}: "))
            somatoria_notas = somatoria_notas + nota    
        media = somatoria_notas / qtd_notas
        print("valor da media: ",media)
        if(media >= NOTA_APROVACAO):
            #adiciona na lista de aprovados as sub listas [i] e [media]
            lista_aprovados.append([i] + [media])
        else:
            #adiciona na lista de reprovados as sub listas [i] e [media]
            lista_reprovados.append([i] + [media])
            

    print("Aprovados: ",lista_aprovados)
    print("Reprovados: ",lista_reprovados)   

def main():
    qtd_alunos = int(input("Informe a quantidade de alunos: "))
    qtd_notas = int(input("Informe a quantidade de notas: "))

    calcular_media(qtd_alunos,qtd_notas)


if __name__ == "__main__":
    set_vazio = set()
    print(type(set_vazio))
    main()