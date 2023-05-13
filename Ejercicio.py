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

#3. Crear una función que convierta entre grados Celsius, Farenheit y Kelvin Convertir a farenheit : (°C × 9/5) + 32 = °F Convertir a Kelvin: °C + 273.15 = °K Debe recibir 3 parámetros: el valor, la medida de origen y la medida de destino

def convertir_temperatura(valor, medida_origen, medida_destino):
    if medida_origen == 'Celsius':
        if medida_destino == 'Fahrenheit':
            return (valor * 9/5) + 32
        elif medida_destino == 'Kelvin':
            return valor + 273.15
        else:
            return valor  # Si la medida de origen y destino es la misma, no se realiza ninguna conversión
    elif medida_origen == 'Fahrenheit':
        if medida_destino == 'Celsius':
            return (valor - 32) * 5/9
        elif medida_destino == 'Kelvin':
            return (valor - 32) * 5/9 + 273.15
        else:
            return valor
    elif medida_origen == 'Kelvin':
        if medida_destino == 'Celsius':
            return valor - 273.15
        elif medida_destino == 'Fahrenheit':
            return (valor - 273.15) * 9/5 + 32
        else:
            return valor
    else:
        return valor  # Si la medida de origen y destino no es válida, no se realiza ninguna conversión


#4.Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

temperaturas = [25, 0, 100]  # Ejemplo de lista con tres valores de temperatura

unidades = ['Celsius', 'Fahrenheit', 'Kelvin']  # Lista de las tres unidades posibles

for temperatura in temperaturas:
    for origen in unidades:
        for destino in unidades:
            if origen != destino:  # Evitar imprimir conversiones de la misma unidad
                resultado = convertir_temperatura(temperatura, origen, destino)
                print(f"{temperatura} grados {origen} son equivalentes a {resultado} grados {destino}")









