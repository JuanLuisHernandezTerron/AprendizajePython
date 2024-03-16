objeto={
    'nombre':'Juanlu',
    'tecnologias':'JS, JAVA, TS, Python',
    'edad':22
}

#Para iterar las claves de un objeto y posteriormente sacar esos valores  
print(objeto.keys()) 
array = objeto.keys() #Devuelve un array con los valores de las claves del objeto 

for elemnto in array: #Recorremos el array y por cada iteracion sacamos su valor con .get()
    print(objeto.get(elemnto))

#Para obtener un dato de un objeto utilizaremos esto
print(objeto["edad"])  

#con .items, tendremos en un array par de claves valores, tendremos que llamar a la funcion list(), ya que es un array lo que devuelve pero no es indexable(NO SE PUEDE LLAMAR A "PELO")
asd = list(objeto.items())
print(asd[0])