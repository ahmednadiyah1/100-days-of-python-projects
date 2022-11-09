import json
import random
adjectives=json.load(open("adjectives.txt"))
animals=json.load(open("animals.txt"))

randAdj=adjectives[random.randint(0,len(adjectives)-1)]
randAnl=animals[random.randint(0,len(animals)-1)]
print(randAdj+" "+randAnl)
