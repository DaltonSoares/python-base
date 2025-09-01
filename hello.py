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

# importando modulo os que permite interagir com o sistema operacional.
import os

#current_language = "en_US" # padrao snake_case que tudo é minúsculo.


current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hola, Mundo!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "en_US":
    msg = "Hello, World!"


# Este programa imprime Hello World
print("\033[31m",current_language,"\033[0m")
print(msg)