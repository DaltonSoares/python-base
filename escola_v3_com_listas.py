#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
__version__ = "0.1.0"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

# Todos os alunos
todos_alunos = []
todos_alunos.extend(sala1)
todos_alunos.extend(sala2)

atividades = [
    ("Inglês", aula_ingles),
    ("Música", aula_musica),
    ("Dança", aula_danca),
]

# Alunos que façam mais de uma atividade
alunos_mais_de_uma_aula = set(aula_ingles) | set(aula_musica) | set(aula_danca)

# Mostrar o nome do aluno e qual atividade ele faz
for alunos in alunos_mais_de_uma_aula:
    print()
    for nome_atividade, atividade in atividades:
        if alunos in atividade:
            print(alunos, ":", nome_atividade)
    print("-" * 15)
    




"""
for aluno in alunos:
    for nome_atividade, atividade in atividades:
        if aluno in atividade:
            lista_aluno = []
            lista_aluno.append(atividade)
            print(lista_aluno, nome_atividade)
"""
    #print(aluno)

# Lista com as atividades para iterar nessa lista. 
# Cada item da lista é uma tupla, com uma label e uma lista.
"""atividades = [
    ("Inglês", aula_ingles),
    ("Música", aula_musica),
    ("Dança", aula_danca),
]
"""

# Percorrendo a lista atividades e fazendo o desacoplamento.
# Ao percorrer o primeiro item terá nome_atividade = ingles
# atividade = aula_ingles
"""for nome_atividade, atividade in atividades:
    print("-" * 40)
    print(f"Alunos da atividade {nome_atividade}\n")
    

    atividade_sala1 = []
    atividade_sala2 = []


    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)    
    print("Sala1", atividade_sala1)
    print("Sala2", atividade_sala2)

    print()
"""