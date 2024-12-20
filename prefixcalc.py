#!/usr/bin/env python

""" 
Calculadora prefix

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py 
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em `prefixcalc.log`
"""

__version__ = "0.1.0"
__author__ = "MCarolina"
__license__ = "Unlicense"

import os
import sys
from datetime import datetime
import logging
from logging import handlers

# BOILERPLATE - logging
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("bruno", log_level)
fh = handlers.RotatingFileHandler(
   "meulog.log", 
   maxBytes=300, # 10**6
   backupCount=10,
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
fh.setFormatter(fmt)
log.addHandler(fh)
#

while True:
    arguments = sys.argv[1:] # pega os args q usuario digitar, exceto nome do progr

    if not arguments:
        operation = input("Qual operação deseja usar? ")
        n1 = input("Valor n1: ")
        n2 = input("Valor n2: ")
        arguments = [operation, n1, n2]
        
    elif len(arguments) != 3:
        print("Número de argumentos inválido")
        print("ex: `sum 5 5 `")
        sys.exit(1)
        
    operation, *nums = arguments

    valid_operations = ("sum", "sub", "mul", "div")
    if operation not in valid_operations:
        print("Operação inválida")
        print(valid_operations)
        sys.exit(1)
        
    validated_nums = []    
    for num in nums:
        # todo: use while + exception
        if not num.replace(".", "").isdigit():
            print(f"Número inválido {num}")
            sys.exit(1)
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        validated_nums.append(num)

    try:
        n1, n2 = validated_nums
    except ValueError as e:
        # print(str(e))
        log.error("[ERROR] Error %s", str(e))

    # todo: use dict of functions
    if operation == "sum": result = n1 + n2
    elif operation == "sub": result = n1 - n2
    elif operation == "mul": result = n1 * n2
    elif operation == "div": result = n1 / n2
            
            
    path = os.curdir
    filepath = os.path.join(path, "prefixcalc.log") 
    timestamp = datetime.now().isoformat()
    user = os.getenv('USER', 'anonymous')

    print(f"O resultado é = {result}")

    try:
        with open(filepath, "a") as file_:
            file_.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n")
    except PermissionError as e:
        # todo: logging
        # print(str(e))
        log.error("[ERROR] Error %s", str(e))
        sys.exit(1)

    if input("Pressione enter para continuar ou qualquer tecla para sair"):
        break
    



