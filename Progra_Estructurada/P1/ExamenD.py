def limpiarpantalla():
    print("\033c");

def sueldoBase(h,s):
    sb=h*s;
    return sb;

res="si";
num_trabadores=0;
sueldos_netos=0;

while res =="si":
    limpiarpantalla();
    nombre=input("Introduce tu nombre: ");
    numero_horas=int(input("Introduce el numero de horas trabajadas: "));
    sueldo_xhoras=float(input("Introduce el sueldo por hora: "));

    sueldo=sueldoBase(numero_horas,sueldo_xhoras);  
    aumeneto=0;

    if numero_horas==10:
        aumeneto=0.20;
    elif numero_horas==15:
        aumeneto=0.30;
    elif numero_horas==20:
        aumeneto=0.15;
    elif numero_horas>25:
        aumeneto=0.08;

    aumentofinal=aumeneto*sueldo;
    sueldo_final=sueldo+aumentofinal;

    print(f"El sueldo final de {nombre} es: {sueldo_final}");
    print(f"El aumento aplicado es del {aumentofinal}");
    res=input("¿Deseas calcular el sueldo de otro trabajador? (si/no): ").lower().strip();
    num_trabadores+=1;
    sueldos_netos=sueldos_netos+sueldo_final;

limpiarpantalla();
print(f"El numero de trabajadores es: {num_trabadores}");
print(f"El total de sueldos netos es: {sueldos_netos}");
