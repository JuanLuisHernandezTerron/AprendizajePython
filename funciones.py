numeros = [15,25,30,15,2,8,9]
array_Ciudad = []
print(f"El numero mayor es {max(numeros)}")
print(f"El numero menor es {min(numeros)}")

def anadirCiudad(ciudad:str):
   return array_Ciudad.append(ciudad) if ciudad != 'Sevilla' else 'Has introducido Sevilla, no se puede añadir' 

def devolverNumeroPosicion(numero:str,posicion:int):
    return numero[int(posicion)] 

while len(array_Ciudad) < 5:    
   anadirCiudad(input("Introduce la ciudad "))

print(array_Ciudad)
print(devolverNumeroPosicion(input('dime el numero '),input('dime que posicion quieres sacar ')))

#Utilizaremos el parametro * para decir que transformaremos los datos pasados por parametros en una tupla
def sumaNumeros(*lista):
    print(lista)
    return sum(lista)

print(sumaNumeros(5,8,7,9,2,3,1,5,4,6))

#Utilizaremos el parametro ** para decir que tranformaremos todos los datos pasados por parametro en un objeto/diccionario
def diccionario(**object):
    print(object)

diccionario(nombre="Jose",apellidos="Ramon",edad=30)