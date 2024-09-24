#!/usr/bin/env python3

"""
"""
import os
import sys

# EAFP - Easy to Ask Forgiveness than Permission 

try:
    names = open("names.txt").readlines()
except FileNotFoundError as e: # for errors that you know may happen
    print(f"{str(e)}")
    sys.exit(1)
    # todo: use retry
else: print("Sucess")
finally: print("Finished")

try:
    print(names[1])
except:
    print("[Error] Missing names in the list")
    sys.exit(1)