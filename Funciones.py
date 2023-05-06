#FUNCIONES: Ahorrar lineas de codigo, reutilizar codigo, permite dividir el programa en pequeñas tareas
#DECLARAR UNA FUNCION EN PYTHON: 
"""def NombreFuncion(parametro1, parametro2...):
    Conjunto de Instrucciones
NombreFuncion(Argumento1, Argumento2...)
"""
#FUNCION SIN PARAMETROS
def DerechosHumanos():
    print("Derecho a la vida\nDerecho a la salud\nDerecho a la educacion\nDerecho a la libre expresión\nderecho a la libertad\nDerecho al libre desarrollo de la personalidad")
DerechosHumanos()
def MayoresEdad():
    print("Derecho a morir dignamente\nDerecho al trabajo\nDerecho a una vejez digna\nDerecho a votar")

#FUNCION CON PARAMETROS:
#Declarar una funcion que muestre los derechos humanos y derechos mayores de edad, si la edad es mayor o igual que 18 de lo contrario solo muestre los derecho humanos.

def Derechos(Nombre, Edad):
    print(f"{Nombre} tus derechos son: ")
    if Edad >= 18:
        DerechosHumanos()
        MayoresEdad()
    else:
        DerechosHumanos()
Edad = int(input("Ingrese la edad: "))
Derechos("Karina", Edad)

#FUNCION DIVISION: 
#Divisor es 0 debe arrojar un mensaje de error, de lo contrario muestre el resultado

Divisor = 3
def Division(Dividendo, Divisor):
    if Divisor == 0:
        print("No existe la division por cero")
    else:
        print(f"El cociente es {Dividendo // Divisor}")
Division(20, Divisor)
print(Divisor)


