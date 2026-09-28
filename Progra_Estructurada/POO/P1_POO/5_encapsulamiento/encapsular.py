class Clase:
    atributo_publico = "Hola soy atributo publico"   # Atributo publico
    __atributo_privado = "Hola soy atributo privado" # Atributo privado

    # No accesible desde el exterior
    def __getMetodoPrivado(self):  #metodo privado
        print("Soy un metodo privado")

    # Accesible desde el exterior
    def getMetodoPublico(self):  #metodo publico
        return "Soy un metodo publico"

    def getMetodoPublico2(self):  #metodo publico que accede a un atributo privado
        return self.__atributo_privado

    def getMetodoPublico3(self):
        self.__getMetodoPrivado()    

    
objeto = Clase()

print(objeto.atributo_publico) #imprimir un atributo publico
print(objeto.getMetodoPublico())  #utilizar un metodo publico

# Como esto no es posible se puede acceder a traves de un metodo publico
#print(objeto.__atributo_privado) 
print(objeto.getMetodoPublico2())

#Como no se puede ejecutar un metodo privado solo es posible desde un metodo publico
#print(objeto.__getMetodoPrivado())
objeto.getMetodoPublico3()

