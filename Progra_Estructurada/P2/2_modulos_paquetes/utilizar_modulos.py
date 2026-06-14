# 1er utilizar los modulos 
import modulos; 

modulos.borrarPantalla();
modulos.funcion1();

nom="Daniel";
ape="Flores";
nombre, apellidos=modulos.funcion4(nom,ape);
print(f"Nombre: {nombre} {apellidos}");

#2da formar de utilizar modulos

from modulos import borrarPantalla,funcion4
borrarPantalla();
nom="Daniel"; 
ape="Flores";
nombre, apellidos=funcion4(nom,ape);
print(f"Nombre: {nombre} {apellidos}");