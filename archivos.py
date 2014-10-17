# -*- encoding=utf-8 -*-
import click
import os
import sys
import glob
#import pdb
#pdb.set_trace()
def lee(*args):
    for i in args:
        #print "dentro de funcion lee()", type(i)
        if isinstance(i,unicode) or isinstance(i,str):
            #if os.access(i, os.R_OK): 
            if existe_archivo(i):
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
                        g.write("Este archivo fue copiado de ")
                        g.write(os.path.realpath(i))
                        for linea in f:
                            print linea
                            g.write(linea)
                        f.close()
                        g.close()
                        lee_archivo_varias_lineas(i)
            else:
                print "El archivo no existe."

def existe_archivo(archivo):
    if os.path.exists(archivo):
        return True
    else:
        resp = raw_input("El archivo NO existe, ¿Desea crearlo? [s/n]");
        if resp == "s" or resp == "S":
            if sys.platform == "linux2":
                os.system('touch ' + archivo )
            return True
        else:
            return False

def lee_archivo_varias_lineas(archivo):
    f=open(archivo)
    print "--------------------------------"
    print "Lee varias lineas sin ciclo for:"
    print (f.readlines())
    f.close

#def lista_txt():
#    nombres = os.listdir(os.getcwd))
#    for i in nombres:
#        cad = i
#        if string.find(cad,"*.txt"):
#            print cad

@click.command()
@click.option('--archivo_original', default='original.txt', prompt='Introduzca el nombre del archivo ORIGINAL a copiar', help='Permite indicar el nombre del archivo original.')
def principal(archivo_original):
    if sys.platform == "linux2":
        os.system('clear')
        #lista_txt()
        print glob.glob('*.txt')
        #archivo = raw_input("Introduzca el(los) nombre(s) de el(os) archivo(s) original(es):");
        #print archivo_original
        #print type(archivo_original)
        #copia=""
        #print type(copia)
        #copia=archivo_original
        #lee(copia)
        lee(archivo_original)

if __name__ == '__main__':
    principal()
