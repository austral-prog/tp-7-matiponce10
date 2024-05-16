def index_of_by_index(word, list, index):
    for i, elemento in enumerate(list[index:], index):
        if elemento == word:
            return i
    return -1


def index_of_empty(list):
    for i, elemento in enumerate(list):
        if elemento == "":
            return i
    return -1


def index_of(word, list):
    for i, elemento in enumerate(list):
        if elemento == word:
            return i
    return -1


def put(word, list):
    for i, elemento in enumerate(list):
        if elemento == "":
            list[i] = word
            return i
    return -1


def remove(word, list):
    borrados = 0
    for i, elemento in enumerate(list):
        if elemento == word:
            list[i] = ""
            borrados += 1
    return borrados
