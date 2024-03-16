mi_array = ["pedro","manuel","jose","pedro"]
mi_arrayAUX = [{
'nombre':'Jose',
"apellidos":"Ramirez"
},{
'nombre':'Antonio',
"apellidos":"verdasco"
},{
'nombre':'Jose',
"apellidos":"Gutierrez"
}]

#para saber la longitud de un array
print(len(mi_array))

#para sacar cuantos valores hay repetidos en un array
print(mi_array.count("pedro"))

#con esto podemos instaciar variables con valores del array, pero tenemos que cojer todos los elementos o si no con [:numero], podremos cojer los valores que esten desde 0 hasta esa posicion.
nombre1,nombre2,nombre3,nombre4 = mi_array

print(nombre1,nombre2,nombre3,nombre4)

#para recorrer un array de objetos
for elemento in mi_arrayAUX:
    print(elemento['apellidos'])

#Esto añadimos al final de la lista el objeto/valor que le pasemos por parámetro
mi_arrayAUX.append({
    'nombre':'Juanlu',
    'apellidos':'Hernandez'
})
print(mi_arrayAUX)

#Para agregar varios objeto/valor al array, tendremos que utilizar el extend
mi_arrayAUX.extend([{
    'nombre':'Manuel',
    'apellidos':'Garrion'
},
{
    'nombre':'Manolo',
    'apellidos':'Cortes'
}])
print(mi_arrayAUX)

#Para eliminar un elemento del array pondremos el remove y el valor que tendra que buscar para eliminarlo
mi_arrayAUX.remove({
        'nombre':'Manuel',
    'apellidos':'Garrion'
})
print(mi_arrayAUX)

#Para ordenar un array, utilizaremos el sort, pero si queremos darle la vuelta ordenado tendremos que utilizar lo siguiente
mi_arrayAUX.sort(reverse =True)
print(mi_arrayAUX)

