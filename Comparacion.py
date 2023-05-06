#Funcion que verifique que los datos (dos numeros) sean enteros o decimales y muestre cual de ellos es el mayor
def comparar_numeros(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        print("Ambos números son enteros.")
    elif isinstance(num1, float) and isinstance(num2, float):
        print("Ambos números son decimales.")
    else:
        print("Los números son de tipo diferente.")
    if num1 > num2:
        print(f"{num1} es mayor que {num2}.")
    elif num2 > num1:
        print(f"{num2} es mayor que {num1}.")
    else:
        print("Los números son iguales.")

comparar_numeros(9, 3)
comparar_numeros(5.2, 6.4)
comparar_numeros(8, 3.0)