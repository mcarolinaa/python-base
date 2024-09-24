#!/usr/bin/env python3

"""
"""
import os
import sys

if os.path.exists("names.txt"):
    # input("...") # race condition - not desirable
    names = open("names.txt").readlines()
else:
    print("[Error] File names.txt not found")
    sys.exit(1)
    
# LBYL - Look Before You Leap

if len(names) >= 3:
    print(names[1])
else:
    print("[Error] Missing names in the list")
    sys.exit(1)