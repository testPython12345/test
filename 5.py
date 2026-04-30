import json
data = {
    "Name":"Daniil",
    "Age":25,
    "Skills":['python']
}
with open('exp.json', mode='w', encoding='utf-8') as file:
    json.dump(obj=data, fp=file, indent=4)

with open('exp.json', 'r', encoding='utf-8') as f:
    print(json.load(f))