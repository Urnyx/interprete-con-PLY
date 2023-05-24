from principal import *   

def ejecutar(sintax):    
    res = ''
    
    for i in mostrar(sintax):
        if i != None:
           res += i +"\n"

    return res