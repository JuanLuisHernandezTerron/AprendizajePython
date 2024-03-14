from typing import List
#Creacion de varias variables en una línea
numero,numeroAUX = 15 , "15"
 
array:List[bool] = [True,False,True,False,False,True]

#Vamos a parsearlo a string, en JS sería toString()
print(type(str(numero)))
#Vamos a parsearlo a integer.
print(type(int(numeroAUX)))

cadena1  = "Hola"
cadena2 = "a todos"
#Devuelve cuantos caracteres tiene una cadena,array,etc...
print(len(cadena1))
print(len(array))

#Para insertar datos desde la consola
edad:int = input("Cual es tu edad?")
print("Tu edad es:"+edad)

#En Python no sirve el && o el || o el ! para decir que no, tendremos que utilizar and , or , not
 
if (not numero == numeroAUX):
    print("Hola")
else:
    print("Hola pepito")