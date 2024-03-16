cadena:str = "Hola a todos me llamo Juan Luis"

#Para acortar un string, donde en JS sería el equivalente a slice
print(cadena[0:9])

#Empieza a acortar el string desde el final | OUTPUT ->  Luis
print(cadena[-4:len(cadena)])

#Y si queremos sacar una letra solo | OUTPUT ->  n
print(cadena[-6])

#Para darle la vuelta a una cadena utilizaremos slicing con []
print(cadena[::-1])

#Empieza desde 0 hasta el final, y coje la letra cada 6 saltos | OUTPUT-> H  aas
print(cadena[0:len(cadena):6])

#Devuelve cuantas letras hay en la cadena con el parametro que le pasemos
print(cadena.count("H"))

#Pone la cadena entera en mayusculas, para minuscula entera sería lower()
print(cadena.upper())

#Devulve true o false si la cadena empieza por el string que le pasamos por parámetro
print(cadena.startswith("Hola"))

