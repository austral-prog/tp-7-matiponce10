def enumerate_list(list):
    new_list = []
    i = 0
    for color in list:
        if color != "":
            new_list.append(f"{i}. {color}")
            i +=1
    return new_list


def enumerate_backwards(list):
    new_list = []
    i = 0
    for color in list:
        if color != "":
            new_list.append(f"{i}. {color[::-1]}")
            i += 1
    return new_list
