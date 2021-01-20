#!/usr/bin/python3
"""add item module
add argv into json file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    myList = load_from_json_file("add_item.json")
except:
    myList = []

args = len(sys.argv)
arg = sys.argv
i = 1

while i < args:
    myList.append(arg[i])
    i += 1
save_to_json_file(myList, "add_item.json")
