import json

with open("dict_type.json", "r") as f:
    dict_type = json.load(f)

for key in dict_type:
    dict_type[key].append('ewef')

print(dict_type)