#!/usr/bin/env python3

"""
Imprime a mensagem de um e-mail
"""

import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("Informe o arquivo com a lista de emails, e o template de email")
    sys.exit(1)
    
filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename) #emails.txt
templatepath = os.path.join(path, templatename) #template.txt

clientes = []
for line in open(filepath):
    name, email = line.split(",")
    # todo: substitute for send email
    print(f"Enviando email para {email}")
    print()
    print(
        open(templatepath).read()
        % {
            "nome": name
            ,"produto": "caneta"
            ,"texto": "Escrever muito bem"
            ,"link": "http://canetaslegais.com"
            ,"quantidade": 1
            ,"preco": 50
        }
    )
    print("-" * 30)