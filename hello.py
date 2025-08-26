#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configura no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:
    python hello.py
    ou
    ./hello.py
"""
# Dunder é uma palavra que começa com dois _ e termina com dois _
__version__ = "0.0.1"
__author__ = "Dalton Augusto Soares"
__license__ = "Unlicense"

#current_language = "en_US" # padrao snake_case que tudo é minúsculo.  
current_language = input("Escolha a linguagem:\nen_US \npt_BR \nit_IT\n\n")

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

# Este programa imprime Hello World
print(msg)
