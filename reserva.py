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
import logging

log = logging.Logger("Alerta")

RESERVAS_FILE = "reservas.txt"
QUARTOS_FILE = "quartos.txt"

# TODO: usar lib csv

# ler as reservas p/ ver oq ta ocupado
ocupados = {} # acumulador
try:
    for line in open(RESERVAS_FILE):
        nome_cliente, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome_cliente": nome_cliente,
            "dias": int(dias)
            }
except FileNotFoundError:
    logging.error("Arquivo %s não existe", RESERVAS_FILE)
    sys.exit(1)


# informa o que tem: le quartos e apresenta
# TODO: usar funçãp p/ ler arquivos
quartos = {}
try:
    for line in open(QUARTOS_FILE):
        num_quarto, nome_quarto, preco = line.strip().split(",")
        quartos[int(num_quarto)] = {
            "nome_quarto": nome_quarto,
            "preco": float(preco), #TODO: Decimal
            "disponivel": False if int(num_quarto) in ocupados else True
        }
except FileNotFoundError:
    logging.error("Arquivo %s não existe", QUARTOS_FILE)
    sys.exit(1)


# reserva
print("Reserva do Hotel Pyhtonico")
print("-"* 40)

# se estiver lotado, nao
if len(ocupados) == len(quartos):
    print("Hotel lotado")
    sys.exit(0)

# efetiva reserva
nome_cliente = input(f"Informe o/a nome principal da reserva: ").strip().lower()
print()
print("Lista de quartos disponíveis:")
for num_quarto, dados in quartos.items():
    nome_quarto = dados["nome_quarto"]
    preco = dados["preco"]
    disponivel = "⛔️" if not dados["disponivel"] else "👍🏼"
    print(f"{num_quarto} - {nome_quarto} - R$ {preco:.2f} - {disponivel}")


# pega info do usuario
print("-"* 40)

try:
    num_quarto = int(input("Número do quarto desejado: ").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado")
        sys.exit(0)
except KeyError:
    logging.error("O quarto {num_quarto} não existe")
    sys.exit(0)
except ValueError:
    print(f"Número inválido, insira apenas dígitos")
    sys.exit(0)

try:
    dias = int(input("Quantas diárias? ").strip())
except ValueError:
     logging.error("Número inválido, insira apenas dígitos")
     sys.exit(0)
     
# print(nome, num_quarto, dias)
nome_quarto = quartos[num_quarto]["nome_quarto"]
preco_quarto = quartos[num_quarto]["preco"]
disponivel = quartos[num_quarto]["disponivel"]
total =  preco_quarto * dias

with open(RESERVAS_FILE, "a") as f:
    f.write(f"{nome_cliente}, {num_quarto}, {dias}\n")

print(f"{nome_cliente}, você escolheu o quarto {nome_quarto} e vai custar: R${total:.2f}")