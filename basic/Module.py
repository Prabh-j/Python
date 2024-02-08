print('imprting the module.....')

test = "test string"

def find_index(to_search, target):
    for i, value in enumerate(to_search): #emunerate for multiple values
        if value == target:
            return i
    return -1
