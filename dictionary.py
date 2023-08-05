def read_library():
    with open('greenteapress.com_thinkpython_code_words.txt') as file:
        library = file.readlines()

        new_lib = []

    for i in library:
        i = i.strip().strip('\n').lower()
        new_lib.append(i)

    return new_lib
