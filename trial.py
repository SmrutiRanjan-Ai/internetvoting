
import re
import json

string = '26952518-d86d-440f-9a6a-f8c8d46e7de5@1@{"0e2e8069-d56f-4294-8e3b-f73fd45e277f": true, "2edbde45-03b3-4255-b453-88bc9935f581": null, "d0fa11d4-55cc-4b53-89f9-6eb4e98c7d91": null}'
pattern = '@'

result = re.split(pattern, string)
print(result)
res = json.loads(result[2])
print(res,type(res))
ages = {
    'Matt': 30,
    'Katie': 29,
    'Nik': 31,
    'Jack': 43,
    'Alison': 32,
    'Kevin': 38
}

max_value = max(ages, key=ages.get)
print(max_value)

import random
d = {'a':1, 'b':2, 'c':3, 'd':4}
print(d)
items = list(d.values())
keys = list(d.keys())
random.shuffle(keys)
for i in range(len(keys)):
    d[keys[i]]=items[i]
print(items)
print(keys)
print(d)
