print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[23,45,23,33,25,100,-100];
print(numeros);

lista="[";
for i in numeros:
    lista+=f"{i}, ";
print(f"{lista}]");

lista1="[";
for i in range(0,len(numeros)):
    lista1+=f"{numeros[i]}, ";
print(f"{lista1}]");

lista2="[";
i=0;
while i<len(numeros):
    lista2+=f"{numeros[i]}, ";
    i+=1;
print(f"{lista2}]");


#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
palabras=["Hola","NBA","Ganador","Perdedor"];
palabra=input("Ingrese la palabra a buscar: ").strip();

#1re forma
if palabra in palabras:
    print(f"La palabra: {palabra} se encuentra en la lista");
else:
    print(f"La palabra: {palabra} no se encuentra en la lista");

#2DA FORMA
encontre=False;
for i in palabras:
    if i==palabra:
        encontre=True;

if encontre:
    print(f"La palabra: {palabra} se encuentra en la lista");
else:
    print(f"La palabra: {palabra} no se encuentra en la lista");


#3er FORMA
encontre=False;
i=0;
while i<len(palabras) and encontre==False:
    if palabras[i]==palabra:
        encontre=True;
    i+=1;

if encontre:
    print(f"La palabra: {palabra} se encuentra en la lista");
else:
    print(f"La palabra: {palabra} no se encuentra en la lista");

#4ta FORMA
encontre=False;
for i in range(0,len(palabras)):
    if palabras[i]==palabra:
        encontre=True;

if encontre:
    print(f"La palabra: {palabra} se encuentra en la lista");
else:
    print(f"La palabra: {palabra} no se encuentra en la lista");



#Ejemplo 3 Añadir elementos a la lista
lista=[];

true="S";
while true=="S":
    valor=input("Ingrese un valor a la lista: ").strip();
    lista.append(valor);
    true=input("Desea añadir otro elemento? S/N: ").strip().upper();
print(lista);

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
agenda=[
        ["Juan", "123456789"],
        ["Maria", "987654321"],
        ["Pedro", "456789123"]    
        ];
print(agenda);

for i in agenda:
    print(f"Nombre: {i[0]} - Telefono: {i[1]}");

lista="";
for r in range(0,3):
    for c in range(0,2):
        lista+=f"{agenda[r][c]}, ";
    lista+="\n";
print("["+lista+"]");