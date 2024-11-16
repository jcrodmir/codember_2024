from io import open
import re
import time
inicio=time.time()
log= open("log.txt")

logs=log.readlines()


logs = [palabra.replace("\n", "") for palabra in logs]
    

def comprobra_array(array):
    Correcto=0
    Falso=0
    for palabra in array:
        if(not comprobar_digito_ascendente(palabra)):
            Falso= Falso + 1
        elif(not comprobar_digito_ascendente(palabra)):
            Falso= Falso + 1
        elif(not comprobar_letra_ascendente(palabra)):
            Falso= Falso + 1
        elif(not comprobar_digito_tras_letra(palabra)):
             Falso= Falso + 1
        else:
            Correcto=Correcto +1
    print("Correcto: " , Correcto)
    print("Falso: " , Falso)
    
def comprobar_digitos_caracteres(palabra):
    
    for letra in palabra:
        if(not letra.isdigit()):
            if(ord(letra)< 97 or ord(letra)>122):
                return False
    return True

print(comprobar_digitos_caracteres("afg23123dsfg"))
def comprobar_digito_ascendente(palabra):
    digito=-1
    for letra in palabra:
        if(letra.isdigit() and int(letra)>=digito):
            digito=int(letra)
        elif(letra.isdigit() and int(letra)<digito):
            return False
    return True
        
def comprobar_letra_ascendente(palabra):
    letra=96
    for caracter in palabra:
        if(ord(caracter)>=letra):
            letra=ord(caracter)
        elif(not caracter.isdigit()):
            return False
    return True

def comprobar_digito_tras_letra(palabra):
    letra=""
    for caracter in palabra:
        if(not caracter.isdigit() and ord(caracter)>=97 and ord(caracter)<=122):
            letra=caracter
        elif(letra != "" and caracter.isdigit()):
            return False
    return True

comprobra_array(logs)

fin=time.time()
print(fin-inicio)
    
    