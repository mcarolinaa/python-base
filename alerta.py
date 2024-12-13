#!/usr/bin/env python3

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

# TODO: mover p/ modulo de utilidades

import sys
import logging
from typing import Dict

log = logging.Logger("Alerta")


def is_completely_filled(dict_of_inputs: Dict):
    """returns a boolean telling if a dictionary is completely filled"""
    info_size = len(dict_of_inputs)
    filled_size = len(
        [value for value in dict_of_inputs.values() if value is not None]
        )
    return info_size == filled_size
   
   
def read_inputs_for_dict(dict_of_info):
    """read information for a dict from user input"""
    
    for key in dict_of_info.keys():
        if dict_of_info[key] is not None:
            continue
        try:
            dict_of_info[key] = int(input(f"{key}:").strip())
        except ValueError:
            log.error("%s inválida, digite números", key)
            break
    

# Programa principl
info = {
    "temperatura": None,
    "umidade": None
}
    
while not is_completely_filled(info):
    
    read_inputs_for_dict(info)
    
    

temp, umidade = info.values()

    
# cmd+ctrl+space = emojis
if temp > 45: result = "ALERTA: 🥵 Perigo de calor extremo"
elif temp >= 0 and temp <= 10: result = "ALERTA: 🥶 Risco de frio"
elif temp * 3 >= umidade: result = "ALERTA: 🥵💧 Perigo de calor úmido"
elif temp < 0: result = "ALERTA: 🥶🥶 Perigo de frio extremo"
else: result = "🙂 Condições normais"

print(result)