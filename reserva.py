"""
Fazer programa de terminal que exibe ao usuário uma lista dos quartos
disponíveis p/ alugar e o preço de cada quarto - esta informação está
disponível em um arquivo de texto separado por vírgulas.

`quartos.txt`
# codigo, nome, preço
1, Suite Master, 500
2, Quarto Familia, 200
3, Quarto Single, 100
4, Quarto Simples, 50

O programa pergunta ao usuário o nome, qual o número do quarto a ser 
reservado e a quantidade de dias. E no final exibe o valor estimado
a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas.

`reservas.txt`
# cliente, quarto, dias
Maria, 3, 12

Se outro usuário tentar reservar o mesmo quarto, o programa deve 
exibir uma mensagem informando que já está reservado.

"""
import sys
import os
import logging

log = logging.Logger("Alerta")
path = os.curdir
filepath = os.path.join(path, "quartos.txt")

# ler as reservas p/ ver oq ta ocupado
ocupados = {}
try:
    for line in open("reservas.txt"):
        nome, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome,
            "dias": dias
            }
except FileNotFoundError:
    logging.error("Arquivo reservas.txt não existe")
    sys.exit(1)


# informa o que tem: le quartos e apresenta
quartos = {}
try:
    for line in open(filepath):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco), #TODO: Decimal
            "disponivel": False if int(codigo) in ocupados else True
        }
except FileNotFoundError:
    logging.error("{filepath} não existe")
    sys.exit(1)


# reserva
print("Reserva do Hotel Pyhtonico")
print("-"* 40)

# se nao estiver lotado
if len(ocupados) == len(quartos):
    print("Hotel lotado")
    sys.exit(1)

# efetiva reserva
nome = input(f"Informe o/a nome principal da reserva: ").strip().lower()
print("Lista de quartos disponíveis:")
for codigo, dados in quartos.items():
    nome_quarto = dados["nome"]
    preco = dados["preco"]
    disponivel = "⛔️" if not dados["disponivel"] else "👍🏼"
    print(f"{codigo} - {nome_quarto} - R$ {preco:.2f} - {disponivel}")


# pega info do usuario
print("-"* 40)

try:
    num_quarto = int(input("Número do quarto: ").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado")
        sys.exit(1)
except ValueError:
    logging.error("Número inválido, insira apenas dígitos")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe")
    sys.exit(1)

try:
    dias = int(input("Quantas diárias? ").strip())
except ValueError:
     logging.error("Número inválido, insira apenas dígitos")
     sys.exit(1)
     
# print(nome, num_quarto, dias)
nome_quarto = quartos[num_quarto]["nome"]
preco_quarto = quartos[num_quarto]["preco"]
disponivel = quartos[num_quarto]["disponivel"]
total =  preco_quarto * dias

with open("reservas.txt", "a") as f:
    f.write(f"{nome}, {num_quarto}, {dias}\n")

print(f"{nome}, você escolheu o quarto {nome_quarto} e vai custar: R${total}:.2f")