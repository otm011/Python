def multiprint(message, a):
    for i in range(0, a):
        print(message + "\n")

# multiprint("Hello world", 26)

def reverse(liste):
    new_list = []
    for i in range(len(liste) - 1, -1, -1):
        new_list.append(liste[i])
    return new_list

def reverse_rec(liste):
    print(liste)
    if len(liste) == 2:
        a = liste[0]
        liste[0] = liste[1]
        liste[1] = a
    elif len(liste) > 2:
        x = liste.pop()
        reverse_rec(liste)
        liste.insert(0, x)
    print(liste)
    return liste


