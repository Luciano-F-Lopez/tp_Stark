from os import system
def pausar():
    system("pause")

def pantalla_limpia():
    system("cls")

def menu_00()->str:
    pantalla_limpia()
    print(" Menu de Opciones")
    print("1- Obtener nombre de cada Super Heroe")
    print("2- Obtener Nombre y Altura de cada Super Heroe")
    print("3- Obtener al SuperHeroe Mas Alto")
    print("4- Obtener al SuperHeroe Mas bajo")
    print("5- Obtener la Altura Promedio de todos los SuperHeroes")
    print("6- Obtener el nombre Del SuperHeroes Mas Alto y Mas bajo")
    print("7- Obtener Al SuperHeroe Mas y Menos Pesado")
    print("8- Salir")
    opcion = input("Ingrese opcion: ")
    return opcion

def menu_01()->str:
    pantalla_limpia()
    print(" Menu de Opciones")
    print("1- Obtener nombre de cada Super Heroe Masculino")
    print("2- Obtener nombre de cada Super Heroe Femenino")
    print("3- Obtener al SuperHeroe Mas Alto Masculino")
    print("4- Obtener a la SuperHeroina mas alta ")
    print("5- Obtener al SuperHeroe Mas bajo Masculino")
    print("6- Obtener al SuperHeroeina Mas baja")
    print("7- Obtener la Altura Promedio de todos los SuperHeroes")
    print("8- Obtener la Altura Promedio de todas las SuperHeroinas")
    print("9- Cuantos tipos de ojos tiene cada super")
    print("10- Cuantos tipos de pelo tiene cada super")
    print("11- Cuantos tipos de inteligencia tiene cada super")
    print("12- Supers agrupados por color de ojos")
    print("13- Supers agrupados por color de pelo")
    print("14- Supers agrupados por inteligencia")
    print("15- salir")

    opcion = input("Ingrese opcion: ")
    return opcion

def saludar():
    print("Buenos dias")

def brindar():
    print("Chin,chin....")

def despedir():
    print("Hasta Luego")

#---------------------------------------------------

