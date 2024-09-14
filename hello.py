#!/usr/bin/env python3
"""
Hello world multi languagues

Depending on the configured language
inside the environment, the program will
exhibit the corresponding message

Usage:
Have the LANG environment variable properly
set.
ex:
    export LANG=pt_br
    
Execution:
python3 hello.py
or
./hello.py

"""

# special metadata
__version__ = "0.1.2"
__author__ = "MCarolina"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG")[:5]

msg = {
    "en_US": "Hello world multi",
    "pt_BR": "Olá mundo multi",
    "es_ES": "Hola mundo multi",
    "fr_FR": "Salut monde multi",
    "ru_RU": "Privet, mul'ti mir",
    }

# sets (hash table) O(1) - constante
# dicts (hash table)

# Ordem Complexidade: O(n) (antigo)

# O(1) - constante
print(msg[current_language])









