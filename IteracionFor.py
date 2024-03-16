array1 = ['Sevilla','Betis','Madrid','Barcelona','Huelva']
array2 = ['Andalucia','Andalucia','Madrid','Cataluña','Andalucia']

#Para iterar sobre 2 arrays, utilizaremos zip(Array1,Array2)
for ciudad,comunidad in zip(array1,array2):
    print(f'La Ciudad es {ciudad} y su comunidad es {comunidad}')

#Para recorrer en un rango de numeros
for numeros in range(3):
    print(numeros)
else:
    print("Se acabó el bucle")

#estilo .filter() en js, queremos que me muestre todas las ciudades menos Sevilla
for x in array1:
    if x == 'Sevilla':
        continue
    print(f'Las ciudad son las siguientes {x}')

#Para filtrar un array .filter() en JS, para hacer un for en una línea se haría de esta forma.
arrayFilter = [ciudad for ciudad in array1 if ciudad != 'Sevilla']
print(arrayFilter)

#Iteracion de Objetos
ObjecAux = {
'nombre':'Jose',
"apellidos":"Ramirez"
}

for informacion in ObjecAux.items():
    print(informacion) #Devuelve un diccionario clave valor
    print(f'Su nombre es {informacion[0]} y su apellidos es {informacion[1]}')