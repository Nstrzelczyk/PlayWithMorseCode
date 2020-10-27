import random
from alfabeth import alfa


# random generator letter

def syg_first(dict=None):
    if dict is None:
        dict = {}
    letters = []
    for v in dict.values():
        letters.append(v)

    letter = random.choice(letters)
    return letter


print(syg_first(alfa))
