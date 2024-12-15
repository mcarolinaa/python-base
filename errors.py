#!/usr/bin/env python3

"""
"""
import os
import sys
import logging

log = logging.Logger("errors")


# EAFP - Easy to Ask Forgiveness than Permission 

def try_to_open_a_file(filepath, retry=0) -> list:
    """tries to open a file,
    if error, retries n times"""
    if retry > 999:
        raise ValueError("retry cannot be above 999")
    try:
        return open(filepath).readlines()
    except FileNotFoundError as e: # for errors that you know may happen
        log.error("ERRO: %s", e)
        time.sleep(2)
        if retry > 1:
            return try_to_open_a_file(filepath, retry=retry-1)
        # todo: use retry
    else: print("Sucess")
    finally: print("Finished")
    return []

for line in try_to_open_a_file("names.txt"):
    print(line)

try:
    print(names[1])
except:
    print("[Error] Missing names in the list")
    sys.exit(1)