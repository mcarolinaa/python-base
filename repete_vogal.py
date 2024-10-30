"""
Repete vogais

Fazer programa que pede ao usuário que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.

ex:
python3 repete_vogal.py
'Digite uma palavra (ou enter para sair)': Python
'Digite uma palavra (ou enter para sair)': Maria
'Digite uma palavra (ou enter para sair)': <enter>
Pythoon
Maariiaa
"""
import sys
import logging

vogais = "aeiouy"
words = []

while True:
    
    word = input("Digite uma palavra (ou enter para sair):").strip()
    if not word: #condicao de parada
        break
    final_word = ""
    for letter in word:
        # TODO: remover acentuacao usando funcao
        # if letter.lower() in vogais:
        #     final_word += letter*2
        # else:
        #     final_word += letter
        final_word += letter * 2 if letter.lower() in vogais else letter
    words.append(final_word)

# for word in words:
#     print(word)
print(*words, sep="\n")
