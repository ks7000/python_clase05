# -*- encoding=utf-8 -*-
import os
def lee(*args):
    for i in args:
        if isinstance(i,str):
            if os.access(i, os.R_OK): 
                arch = raw_input("Introduzca el nombre del archivo a copiar:");
                if arch<> "":
                    copiar = False                    
                    if os.path.exists(arch):
                        resp = raw_input("El archivo existe, ¿Desea sobreescribirlo? [s/n]");
                        if resp == "s" or resp == "S":
                            copiar = True
                    else:
                        copiar = True
                    if copiar:                    
                        f = open(i)
                        g = open(arch, "w")
                        g.write("Este archivo fue copiado de " , os.path.
                        for linea in f:
                            print linea
                            g.write(linea)
                        f.close()
                        g.close()
            else:
                print "El archivo no existe."

archivo = raw_input("Introduzca el(los) nombre(s) de el(os) archivo(s) original(es):");
lee(archivo)
