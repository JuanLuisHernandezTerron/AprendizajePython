#Para crear arrow Functions
funcionLambda = lambda x: x  != 'Sevilla'
mi_array = ["Sevilla","Madrid","Barcelona","Burgos"]
print(list(filter(funcionLambda,mi_array)))
