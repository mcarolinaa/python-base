#!/usr/bin/env python3

# def repete_vogal(word):
#     """retorna palavra com vogais repetidas"""
#     final_word = ""
#     # start debugging w/ printing
#     for index, letter in enumerate(word):
#         print(f"{index=} {letter=}")
#         if letter.lower() in "aeiouãõâôêéáíó":
#             final_word = letter * 2
#         else:
#             final_word = letter
#         print(f"{final_word=}")
#     return final_word

def repete_vogal(word):
    """retorna palavra com vogais repetidas"""
    final_word = ""
    for letter in word:
        # __import__("pdb").set_trace() # nao é bonito, mas funciona
        # breakpoint()
        if letter.lower() in "aeiouãõâôêéáíó":
            final_word = letter * 2
        else:
            final_word = letter
    return final_word





print(repete_vogal("banana"))





# using pdb in terminal
# pyhton -m pdb tembug.py
# pyhton -m pdb -c continue tembug.py # entender melhor a exception
# check documentation

# variations of pdb protocol:
# ipdb, interactive
# for ipdb as default debugger:
# export PYTHONBREAKPOINT=ipdb.set_trace
 
# pudb has graphic interface, but light
# python -m pudb tembug.py
# and vscode debugger