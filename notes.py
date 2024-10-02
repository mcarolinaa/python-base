#!/usr/bin/env python3

"""
Bloco de notas

$ notes.py new "Minha nova nota"
tag: tech
text:
Anotacao geral sobre tecnologia

$ notes.py read tech
...
...

"""

__version__ = "0.1.0"

import os
import sys
from datetime import datetime

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")
# timestamp = datetime.now().isoformat()
# user = os.getenv('USER', 'anonymous')

arguments = sys.argv[1:]
if not arguments:
    print( "Invalid usage")
    print(f"You must specify {cmds}")
    sys.exit(1)
 

if arguments[0] not in cmds:
    print( "Invalid command {arguments[0]}")
    
if arguments[0] == "read":
    try:
        arg_tag = arguments[1].lower()
    except IndexError:
        arg_tag = input("Please enter the tag: ").strip().lower()
    
    # leitura das notas
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arg_tag:
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()
            
       
if arguments[0] == "new":
    try:
        title = arguments[1]
    except IndexError:
       title = input("Please enter the title: ").strip().title()
        
    text = [
        f"{title}",
        input("tag: ").strip(),
        input("text: ").strip(),
        ]
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")

cont = input(f"Quer continuar {arguments[0]} notas? [N/y]").strip().lower()
if cont != "y":
    break



    