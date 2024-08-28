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
__version__ = "0.0.1"
__author__ = "MCarolina"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG")[:5]

msg = "Hello world multi"

if current_language == "pt_BR":
    msg =  "Olá mundo multi"
elif current_language == "fr_FR":
    msg = "Salut monde multi"
elif current_language == "es_SP":
    msg = "Hola, mundo multi"
elif current_language == "ru_RU":
    msg = "privet, mul'ti mir"

print(msg)









