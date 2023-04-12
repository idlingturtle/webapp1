FILEPATH = 'todolist.txt'                         # constant variable aina isolla


def get_todos(filepath=FILEPATH):                       # tehdään custom funktio get_todos
    """ Luetaan todolistaus tiedostosta                 #
    joka on määritelty filepath default argumentilla    #  doc-string dokumentointiin
    """                                                 #
    with open(filepath, 'r') as file_local:             # avataan tiedosto lukua varten
        todolist_local = file_local.readlines()         # sulkee tiedoston automaattisesti
    return todolist_local                               # palauttaa tiedoston sisällön listan muodossa


def write_todos(todolist_param, filepath=FILEPATH):  # tehdään custom funktio get_todos
    """ Avataa tiedosto joka on määritelty filepath     #
    argumentilla kirjoitusta varten                     #  doc-string dokumentointiin
    """                                                 #
    with open(filepath, 'w') as file:                   # avataan tiedosto kirjoitusta varten
        file.writelines(todolist_param)                 # sulkee tiedoston automaattisesti


if __name__ == "__main__":           # voidaan käyttää koodin testaamiseen
    print("credits")                 # __name__ saa nimen main jos se suoritetaan suoraan