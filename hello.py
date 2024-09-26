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
import logging

# boilerplate from log.py
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger(__name__, log_level) 
ch = logging.StreamHandler() 
ch.setLevel(log_level)
fmt = logging.Formatter(  
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)


arguments = {
    "lang": None, "count": 1,
}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
        "You need to use `=`, you passed %s, try --key=value: %s",
        arg,
        str(e)
    )
        sys.exit(1)
    key = key.lstrip("-").strip()
    value = value.strip()
    
    # validacao
    if key not in arguments:
        print(f"Invalid option `{key}`")
        sys.exit(1)
        
    arguments["lang"] = value
    
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

# eafp
try:
    # current_language in msg:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)
    
# message = msg[current_language]

# another way, not so good bc it does not inform the reason of the error
# try w/ default value:
# message = msg.get(current_language, msg["en_US"])

print(message * int(arguments["count"]))









