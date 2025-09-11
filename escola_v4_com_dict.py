#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
__version__ = "0.1.1"

# Dados

salas = {
    "sala1" : ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2" : ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}


atividades = {
    "aula_ingles" : ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "aula_musica" : ["Erik", "Carlos", "Maria"],
    "aula_danca" : ["Gustavo", "Sofia", "Joana", "Antonio"] 
}

# Listar alunos em cada atividade por sala

for nome_atividade, atividade_alunos in atividades.items():
    
    print("-" * 40)
    print(f"Alunos da atividade de {nome_atividade}\n")    

    # sala1 que tem interseção com a atividade
    atividade_sala1 = set(salas["sala1"]) & set(atividade_alunos)
    atividade_sala2 = set(salas["sala2"]).intersection(atividade_alunos)    

    print("Sala1", atividade_sala1)
    print("Sala2", atividade_sala2)

    print()