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
    
Or inform through CLI argument --lang
Or user will input
    
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
import sys

arguments = {
    "lang": None, "count": 1,
}

for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid option `{key}`")
        sys.exit()
    arguments[key] = value
    
# current_language = os.getenv("LANG", "en_US")[:5]
current_language = arguments["lang"]
if current_language is None:
    # todo: use repetition
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input(
            "Choose a language:"
        )

current_language = current_language[:5]

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
print(msg[current_language] * int(arguments["count"]))









