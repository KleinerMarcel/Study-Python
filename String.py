def areyouplay(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";


print(areyouplay("Ron"))
