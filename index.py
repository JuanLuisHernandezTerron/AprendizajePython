from typing import List

#Consultar el tipo de dato
pedro = {
'nombre':'Hola',
"apellidos":"pepito"
}

array:List[bool] = [True,False,True,False,False,True]

print(isinstance("Hola",bool)) #Devuelve true o false si el tipo de datp es el que le pasamos por parametro
array.append("Hola") if (isinstance(True,bool)) else print("No se ha insertado por que no es boolean") #if ternario, primero ponemos la accion si es verdador, luego la condición y final la accion si es false
                                                                                                       #Con isinstance(), sabremos si el dato que le estamos pasando es del tipo que creemos o le ponemos en el segundo paramtro
print(type(25)) #Integer
print(type(True)) #Boolean
print(type([1,2,3,4,5])) #Lista/Array
print(type(pedro)) #Diccionario / Object
