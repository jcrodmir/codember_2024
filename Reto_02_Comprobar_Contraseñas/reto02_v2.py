from io import open
import time
inicio=time.time() 
log= open("log.txt")

logs=log.readlines()


logs = [palabra.replace("\n", "") for palabra in logs]
    

def comprobra_array(array):
    Correcto=0
    Falso=0
    for palabra in array:
        if(not comprobar_digitos_caracteres(palabra)):
            Falso= Falso + 1
        else:
            Correcto=Correcto +1
    print("Correcto: " , Correcto)
    print("Falso: " , Falso)
    
def comprobar_digitos_caracteres(palabra):
    digito=-1
    letra=96
    letra_antes_digito=""
    for caracter in palabra:
        if(not caracter.isdigit()):
            if(ord(caracter)< 97 or ord(caracter)>122):
                return False
        if(caracter.isdigit() and int(caracter)>=digito):
            digito=int(caracter)
        elif(caracter.isdigit() and int(caracter)<digito):
            return False
        if(ord(caracter)>=letra):
            letra=ord(caracter)
        elif(not caracter.isdigit()):
            return False
        if(not caracter.isdigit() and ord(caracter)>=97 and ord(caracter)<=122):
            letra_antes_digito=caracter
        elif(letra_antes_digito != "" and caracter.isdigit()):
            return False
    return True

comprobra_array(logs)
fin=time.time()
print("Versión 2:" ,fin-inicio)
    
    