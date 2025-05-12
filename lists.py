# Replace the "ANSWER HERE" with your answer

def remove_elements(listr):
    lista1 = listr[1:4] 
    return lista1


def add_elements(lista):
    lista.append("Yellow")
    lista.insert(0, "Pink")
    return lista


def is_empty(liste):
    empty = []
    comparar = empty == liste
    return comparar


def check_lists(listch,listch1):
    indice = 2
    if 0 <= indice < len(listch):
       tercero1 = listch[indice]
    else:
        tercero1 = []
        indice = 2
    if 0 <= indice < len(listch1):
       tercero2 = listch1[indice]
    else:
        tercero2 = []
    comp = tercero1 == tercero2
    return comp


def list_of_lists(listl):
    primero = listl[0][0:2]
    segundo = listl[1][1:4]
    tercero = listl[2][-2: ]
    listlfinal = [
        primero,
        segundo,
        tercero
    ]
    return listlfinal
