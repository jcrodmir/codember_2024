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
        if(caracter.isdigit() and letra_antes_digito==""):
            if(int(caracter)<digito):
                return False
            else:
                digito= int(caracter)
        elif(ord(caracter)> 97 or ord(caracter)<122):
            if(ord(caracter)<letra):
                return False
            else:
                letra_antes_digito=caracter
                letra=ord(caracter)
        else:
            return False
        
    return True

comprobra_array(logs)
fin=time.time()
print("Versión 4:" ,fin-inicio)