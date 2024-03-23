import sys  
sys.path.append("clases")
from clases.piloto import Piloto
from clases.escuderia import Escuderia

astonMartin = Escuderia("Aston Martin","Silverstone","1999-08-15")
pilotoAM1 = Piloto("Juan Luis",astonMartin,"2001-08-20",0)
pilotoAM2 = Piloto("Fernando Alonso",astonMartin,"2001-08-20",2)

#Para añadir/settear un piloto a un array de objeto
astonMartin.set_pilotos = pilotoAM1
astonMartin.set_pilotos = pilotoAM2
print(pilotoAM1.escuderia)

print(astonMartin)
for pilotos in astonMartin.pilotos:
    print(pilotos)


