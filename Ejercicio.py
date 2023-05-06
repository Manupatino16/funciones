#1. Crear una funcion que reciba un numero como parametro y devuelva True si es primo y False si no lo es.

def primo(numero):
    if numero <= 1: 
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
print(primo(12))  
print(primo(23))

#2. Utilizaando la funcion del punto 1, realizar otra funcion que reciba de parametro una lista de numeros y devuelva en una lista solo aquellos que son primos

def listaprimos(numeros):
    primos = []
    for numero in numeros:
        if primo(numero):
            primos.append(numero)
    return primos
print(listaprimos([26, 33, 4, 15, 63, 17, 8, 98, 10]))

#3. Crear una funcion que,al reciir una lista de numeros, devuleva el que mas se repite y cuantas veces lo hace. Si hay mas de un "mas repetido", que devuelva cualquiera




