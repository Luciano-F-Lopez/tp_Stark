def duplicar (numero:int)->int:
    numero = numero * 2
    return numero
    
#-------------------------------------------------------------------------------------

def duplicar_valores(listas:list)->None:
    for i in range(len(listas)):
        listas [i] = listas [ i] * 2

#-------------------------------------------------------------------------------------


def mostrar_lista(lista:list)->None:
    for el in lista:
        print(el,end=" ")
    print()

#-------------------------------------------------------------------------------------


def cargar_lista_enteros_random(lista:list, cant:int, desde:int, hasta:int)->None:
    from random import randint
    for _ in range(cant):
        lista.append(randint(desde, hasta))

#-------------------------------------------------------------------------------------


def crear_lista_enteros_random(cant:int, desde:int, hasta:int)->list:
    from random import randint
    lista = [ ]
    for _ in range(cant):
        lista.append(randint(desde, hasta))  
    return lista

#-------------------------------------------------------------------------------------


def totalizar_listas(lista:list)->int:
    total = 0
    for numero in lista:
        total += numero
    return total

#-------------------------------------------------------------------------------------

def calcular_promedio_lista(lista:list)->float:
    total = 0
    vuelta = 0
    for numero in lista:
        total += numero
        vuelta += 1

    promedio = total / vuelta
    return promedio

def calcular_promedio_2_lista(lista:list)->float:
    
    return totalizar_listas(lista) / len(lista)

def calcular_promedio_3_lista(lista:list)->float:
    cant = len(lista)
    if cant == 0:
        raise ValueError("No esta definido el promedio de una lista vacia")
    return totalizar_listas(lista) / cant

#-------------------------------------------------------------------------------------
def calcular_mayor(lista:list)->int:

    if len(lista) == 0:
        raise ValueError("No esta definido el mayor de una lista vacia")
    
    flag = False
    for numero in lista:
        if flag == False or numero > num_mayor :
            num_mayor = numero
            flag = True
    return num_mayor

#------------------------------------------------------------------------------------
def calcular_menor(lista:list)->int:
    if len(lista) == 0:
        raise ValueError("No esta definido el mayor de una lista vacia")
    
    flag = False
    for numero in lista:
        if flag == False or numero < num_menor :
            num_menor = numero
            flag = True
    return num_menor



#------------------------------------------------------------------------------------
def entero_in_lista(lista:list, target:int)->bool:
    for numero in lista:
        if numero == target:
            target = True
            return True
    return False

#-----------------------------------------------------------------------------------
def buscar_in_lista(lista:list, target:int)->int:
    indice = -1

    for i in range(len(lista)):
        if lista[i] == target:
            indice = i
            break
    return indice
            

#busca el elemento y te dice en que posicion esta, sino esta posicion es -1 (ver como lo hacen en clase)
#-----------------------------------------------------------------------------------
def contar_in_lista(lista:list, target:int)->int:
    contador_elemento = 0
    for numero in lista:
        if numero == target:
            contador_elemento+= 1
    return contador_elemento
#busca el elemento y te dice cuantas veces esta

#-----------------------------------------------------------------------------------
def sorteador(lista:list)->None:
    from random import randint
    import time
    i = randint(0,len(lista) - 1)
    time.sleep(2)
    print(lista[i])

#-----------------------------------------------------------------------------------
def ordenar_listas_ascendente(lista:list)->None:
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

#-----------------------------------------------------------------------------------
def ordenar_listas_descendente(lista:list)->None:
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

#----------------------------------------------------------------------------------
def menu_listas()->str:
    print(" Menu de Opciones")
    print("1- Ascendente")
    print("2- descendente")
    opcion = input("Ingrese opcion: ")
    return opcion
#-----------------------------------------------------------------------------------

def ordenar_lista_A_D(lista:list)->None:
    match menu_listas():
        case "1":
            ordenar_listas_ascendente(lista)        
        case "2":
            ordenar_listas_descendente(lista)
    return lista

def ordenar_lista_A_D2(lista:list, asc:bool = True)->None:
        tam = len(lista)
        if asc:
            for i in range(tam - 1):
                for j in range(i + 1, tam):
                    if lista[i] > lista[j]:
                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux       
        else:
            for i in range(tam - 1):
                for j in range(i + 1, tam):
                    if lista[i] < lista[j]:
                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux

        return lista

            



#Nosotros elegimos como lo queremos ordenar de manera ascendente / descendente 

            
    





