#! /usr/local/bin/ python3

# listas materializadas ocupam memoria
# numbers = [1,2,3,4,5,6]
original = [1,2,3]

# for loops
dobrada = []
for n in original:
    dobrada.append(n*2)
print(dobrada)

# funcional
# list comprehension
dobrada = [n*2 for n in original]
print(dobrada)

# dict comprehension
dados = {
    line.split(",")[0]: line.split(",")[1].strip()
    for line in open("emails.txt") 
    if "," in line
    }
print(dados)
