#! /usr/local/bin/ python3

"""Cadastro de produto"""

__version__ = "0.1.0"

from pprint import pprint

produto = {
    "nome" : "Caneta"
    ,"cores": ["azul", "branco"]
    ,"preco": 3.23
    ,"dimensao": {
        "altura": 12.1
        ,"largura": 0.8
        }
    ,"em_estoque": True
    ,"codigo": 45678
    ,"codebar": None
    }

cliente = {
    "nome": "Maria"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}


# for chave, valor in produto.items():
#     print(chave, "-->", valor)

# pprint(compra)

total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"A cliente {compra['cliente']['nome']}"
    f" comprou {compra['quantidade']} unidades de {compra['produto']['nome']}"
    f" e pagou o total de {total_compra}"
    )