
import re

string = 'Twelve:12Eightynine:89.'
pattern = ':'

result = re.split(pattern, string)
print(result)

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
