#!/usr/bin/python3
"""Script to add n save"""


from sys import argv
list = []

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

while("add_item.json"):
    a = True
    break
if a == True:
    list = load_from_json_file("add_item.json")
for i in argv[1:]:
    list.append(i)

save_to_json_file(list, "add_item.json")
