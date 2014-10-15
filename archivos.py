def lee(*args):
    for i in args:
        if isinstance(i,str):
            f = open(i)
            for linea in f:
                print linea
            f.close()

lee("archivo.txt")
