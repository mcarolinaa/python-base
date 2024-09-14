#!/usr/bin/env python3

"""
Exibe relatório de crianças por atividade.
Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades.
"""

__version__ = "0.1.1"

from pprint import pprint

sala = {
    "1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
    ,"2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

aula = {
    "ingles": ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
    ,"musica": ["Erik", "Carlos", "Maria"]
    ,"danca":["Gustavo", "Sofia", "Joana", "Antonio"]  
    
}

atividades = {
    "aula": aula
    ,"sala": sala
}

# iterar em cada aula
for aula_nome, alunos in atividades["aula"].items():
    print(f"Aulos da aula de {aula_nome}:")
    # itera em cada sala
    for sala_nome, sala_alunos in atividades["sala"].items():
        # encontra alunos em cd sala que tbm estao na aula
        sala_aula_alunos = [aluno for aluno in sala_alunos if aluno in alunos]
        # print nome da sala e alunos daquela sala q estao na aula
        if sala_aula_alunos:
            print(f"  Sala {sala_nome}: {sala_aula_alunos}")












# for nome_atividade, atividade in atividades:
    
#     print()
#     print(f"Alunos da atividade {nome_atividade}\n")
#     print("-"* 40)
    
#     # sala1 q tem intersecao com a atividade
#     atividade_sala_1 = set(sala1) & set(atividade)
#     atividade_sala_2 = set(sala2).intersection(atividade)
    
        

    # for aluno in aula_ingles:
    #     if aluno in sala1:
    #         atividade_sala_1.append(aluno)
    #     elif aluno in sala2:
    #         atividade_sala_2.append(aluno)
        
    # print("Sala 1 ", atividade_sala_1)
    # print("Sala 2 ",atividade_sala_2)
    
    # print()
    # print("#"* 50) 