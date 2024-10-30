"""
Alarme de temperatura

Fazer script que pergunta ao usuário qual a temperatura atual e o indice
de umidade do ar, sendo que poderá ser emitida mensagem de alerta 
dependendo das condições:

temp > 45: Alerta, perigo de calor extremo
temp * 3 >= umidade: Alerta, perigo de calor úmido
10 <= temp <= 30: Normal
0 <= temp <= 10: Alerta de frio
temp < 0: Alerta de frio extremo
"""

import sys
import logging

log = logging.Logger("Alerta")

info = {
    "temperatura": None,
    "umidade": None
}


while True:
    
    info_size = len(info.values())
    filled_size = len([value for value in info.values() if value is not None])
    if info_size == filled_size:
        break   
    
    if all(info.values()):
        break # se dict preenchido, para
    
    for key in info.keys():
        if info[key] is not None:
            continue
        try:
            info[key] = int(input(f"{key}:").strip())
        except ValueError:
            log.error("%s inválida, digite números", key)
            break

temp, umidade = info.values()

    
# cmd+ctrl+space = emojis
if temp > 45: result = "ALERTA: 🥵 Perigo de calor extremo"
elif temp >= 0 and temp <= 10: result = "ALERTA: 🥶 Risco de frio"
elif temp * 3 >= umidade: result = "ALERTA: 🥵💧 Perigo de calor úmido"
elif temp < 0: result = "ALERTA: 🥶🥶 Perigo de frio extremo"
else: result = "🙂 Condições normais"

print(result)