print("Hola Mundo!")
print("Adios mundo!")

#Operadores aritmeticos
5+1
print(4+6)
print(3*4)
#precedencia de operadores
print(5+8*(3+2))

#Tiposdedatos
print(type(2))
print(type(8.62))
print(type("Texto"))
print(type('Texto'))
print(type("S"))

#Variables
mensaje = "Esto es un mensaje"
print(mensaje)
mensaje = "Mensaje notificado"
print(mensaje)
print(type(mensaje))
mensaje = 100
print(mensaje)
print(type(mensaje))

mis3animales = "Perico, gallo, chivo"
print(mis3animales)

tresAnimales = "Perico, gallo, chivo"
print(tresAnimales)

#Concatenacion
textoUno = "Mi texto"
textoDos = "Mi segundo texto"

print(textoUno + textoDos)

edad = 20
print("La edad del usuario es: " + str(edad))
print("El tipo de dato de edad es: " + str(type(edad)))

import math

grados = 45.0
radianes = grados * math.pi / 180.0
seno = math.sin(radianes)
print("Seno de 45: " + str(seno))

#La manera de definir funciones en Python
def saludar(nombre):
    print("Hola" + nombre)
    print("¿Cómo estas?")
    print("Te saludo de lejos por eso del virus")

def despedir():
    print("Ya me voy")
    print("Ya que pase todo esto nos abrazamos")

def concatenar(parte1, parte2):
    return parte1 + parte2

print("Esto no es parte de la funcion")
saludar("Martin")
despedir()

frase = concatenar("Hola ", "Adios")
print(frase)