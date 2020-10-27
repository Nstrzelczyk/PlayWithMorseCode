from alfabeth import alfa


text_translate = input("Write your text:\n")  # input data


def output(string, alm):
    string = string.lower()
    for character in string:
        al = alfa[character]
        alm += al
    return alm


name = output(text_translate, "")
print(name)