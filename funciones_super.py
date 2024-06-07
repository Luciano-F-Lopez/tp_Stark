
from funciones_listas import *
from math import *
from random import randint, choice
from data_stark import *


def calcular_promedio_enteros(a:int,b:int)->float:
    """calcular_promedio_enteros

    Args:
        a (int): paso el primer entero a promediar 
        b (int): paso el segundo entero a promediar

    Returns:
        float: devuelve el promedio de los numeros anteriores
    """
    ai = int(a)
    bi = int(b)
    return (ai + bi) / 2

def promediar_listas(lista:list)->None:
    """promediar_listas

    Args:
        lista (list): paso la lista a promediar 
    """
    nota_1 = 3
    nota_2 = 4
    promedio = 5 
    tam = len(lista)
    for i in range(tam):
        promedios =  ((lista[i][nota_1] + lista[i][nota_2] / 2))
        lista[i][promedio] = promedios

def swap_lista(lista:list, i:int, j: int)->None:
    aux =lista[i]
    lista[i] = lista[j]
    lista[j] = aux

    
    
def mapear_nombre_sector(lista:list)->list:
    """mapear_nombre_sector

    Args:
        lista (list): paso la lista original

    Returns:
        list: retorna una lista con solo el nombre y sector
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_retorno = []
    for emp in lista:
        lista_retorno.append((emp["nombre"],emp["sector"]))
    return lista_retorno

def mapear_nombre_sueldo_sector(lista:list)->list:
    """mapear_nombre_sueldo_sector

    Args:
        lista (list): paso la lista original

    Returns:
        list: retorna una lista con solo el nombre,sueldo y sector
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_retorno = []
    for emp in lista:
        lista_retorno.append((emp["sueldo"],emp["sector"],emp["nombre"]))
    return lista_retorno


def mapear_altura_nombre(lista:list)->list:
    """mapear_altura_nombre

    Args:
        lista (list): paso la lista original

    Returns:
        list:retorna una lista con solo la altura y el nombre
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_retorno = []
    for emp in lista:
        lista_retorno.append((emp["altura"],emp["nombre"]))
    return lista_retorno

def mapear_peso_nombre(lista:list)->list:
    """_summary_

    Args:
        lista (list): paso la lista original

    Returns:
        list: retorna una lista con el peso y el nombre de cada super 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_retorno = []
    for emp in lista:
        lista_retorno.append((emp["peso"],emp["nombre"]))
    return lista_retorno

def mapear_edades(lista:list)->list:
    """mapear_edades

    Args:
        lista (list): paso una lista original 

    Returns:
        list: retorna una lista solo con las edades
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_retorno = []
    for emp in lista:
        lista_retorno.append((emp["edad"]))
    return lista_retorno
    
def mapear_campo_lista(lista:list,campo:str)->list:
    """mapear_campo_lista

    Args:
        lista (list): paso lista original
        campo (str): paso el campo de la lista que quiero extraer

    Returns:
        list: retorna una lista original solo con el campo que elejimos 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_retorno = []
    for emp in lista:
        lista_retorno.append(emp[campo])
        return lista_retorno 

#------------------------------------------------------------------------------------------------------------------------

lista = [3,213,21,3,43,24,325,43,5]

def mapear_list(funcion,lista:list[dict])->list:          #funcion que hace mas facil el mapeo de una lista y devuelve una modificacion de lo que habia 
    """_summary_

    Args:
        funcion (_type_): pasamos una funcion de lo que queremos que saque de la lista
        lista (list[dict]): pasamos la lista origina 

    Returns:
        list: retorna una lista con el mapeo que le pedimos 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_retorno = []
    for el in lista:
        lista_retorno.append(funcion(el))
    return lista_retorno


#empleados = []

#lista_destino = mapear_list(lambda emp: (emp["nombre"],emp["sector"], empleados)) #como utilizar la funcion del mapeo de lista simplificada
#lista_destino = mapear_list(lambda emp: (emp["edad"]))
#lista_destino = mapear_list(lambda emp: (emp["genero"]))
#lista_destino = mapear_list(lambda emp: (emp["nombre"],emp["apellido"], empleados))

#Con las siguientes funciones mantenemos la lista original remplazando solo el valor que queremos

def each_list_actualizar_sueldos(lista:list,porcentaje)->None:          #"actualizaria" la lista original que nosotros tenemos
    """each_list_actualizar_sueldos
    Args:
        lista (list): pasamos la lista original
        porcentaje (_type_): pasamos el porcentaje de sueldo a actualizar 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for i in range(len(lista)):
        lista[i]["sueldo"] = lista[i]["sueldos"] + lista[i]["sueldos"] * porcentaje 

def each_list_genero_mayusculas(lista:list)->None:          #"actualizaria" la lista original que nosotros tenemos 
    """each_list_genero_mayusculas

    Args:
        lista (list): pasamos la lista original
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for i in range(len(lista)):
        lista[i]["genero"] = lista[i]["genero"].upper() 

def each_list(funcion,lista:list)->None:          #"actualizaria" la lista original que nosotros tenemos 
    """each_list
    Args:
        funcion (_type_): pasamos la funcion que queremos que haga each_list
        lista (list): pasamos la lista original
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for i in range(len(lista)):
        lista[i] = (funcion(i))

#each_list(lambda emp: emp.update({["sueldo"] * 1.20}) , empleados)   #asi se utilizan estas funciones
#each_list(lambda emp: emp.update({["genero"].upper()}) , empleados)
#each_list(lambda emp: emp.update({"genero": emp["genero".upper],"sueldo": emp["sueldo"] * 1.20}) , empleados)
    
#------------------------------------------------------------------------------------------------------------------------
    

def filtrar_empleados_sector(lista:list,sector)->list:          #la diferencia con mapear es que de la lista vuelven algunos y otros no
    """filtrar_empleados_sector

    Args:
        lista (list): pasamos la lista original
        sector (_type_): pasamos el sector por el que queremos filtrar la lista 

    Returns:
        list: retorna la lista filtrada por el sector 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_retorno = []
    for emp in lista:
        if emp["sector"] == sector: 
            lista_retorno.append((emp))
    return lista_retorno

def filtrar_supers_genero(lista:list,genero)->list:          #la diferencia con mapear es que de la lista vuelven algunos y otros no
    """filtrar_supers_genero

    Args:
        lista (list): pasamos la lista original 
        genero (_type_): pasamos el genero por el que queremos filtrar la lista

    Returns:
        list: retorna la lista filtrada por el genero 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_retorno = []
    for emp in lista:
        if emp["genero"] == genero: 
            lista_retorno.append((emp))
    return lista_retorno

def filtrar_empleados(lista:list,campo,valor)->list:            #solo se pueden filtrar elementos con una variable y clave determinada
    """filtrar_empleados

    Args:
        lista (list): pasamos la lista original 
        campo (_type_): pasamos el campo que queremos 
        valor (_type_): pasamos el valor que queremos filtrar dentro del campo 

    Returns:
        list: _description_
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_retorno = []
    for el in lista:
        if el[campo] == valor: 
            lista_retorno.append((el))
    return lista_retorno

#lista_sistema = filtrar_empleados(empleados,"sector","sistemas")  #asi se usa la funcion anterior 
#lista_sistema = filtrar_empleados(empleados,"sector","sistemas")
#lista_sistema = filtrar_empleados(empleados,"sector","sistemas")


def filtrar_listas(funcion,lista:list)->list:                       #sirve para filtrar cualquier lista con cualquier valor
    """filtrar_listas

    Args:
        funcion (_type_): ponemos lo que queramos que filtre nuestra funcion
        lista (list): pasamos la lista original 

    Returns:
        list: retorna la lista filtreada 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    lista_retorno = []
    for el in lista:
        if funcion(el): 
            lista_retorno.append((el))
    return lista_retorno

#empleadas = filtrar_listas(lambda emp: emp["genero"] == "f",empleados)      #asi se usa la funcion anterior que es la mejor y mas completa con lambda 
#empleados = filtrar_listas(lambda emp: emp["genero"] == "m",empleados)
#empleados_lanus = filtrar_listas(lambda emp: emp["genero"] == "m" and emp["localidad"] == "lanus",empleados) #fijarse bien como esta escrito por que sino tira error

#--------------------------------------------------------------------------------------------------------------------------
def sumar_lista(lista:list)->int:
    """sumar_lista

    Args:
        lista (list): pasamos la lista original 

    Returns:
        int: retorna la suma de todos los elementos de la lista 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    sum = lista[0]
    for el in lista[1: ]:
        sum += el
    return sum


def mayor_lista(lista:list)->int:
    """mayor_lista

    Args:
        lista (list): pasamos la lista original 

    Returns:
        int: nos devuelve el mayor de la lista que pasamos 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    mayor = lista[0]
    for el in lista[1: ]:
        if mayor < el:
            mayor = el 
    return mayor
    

def menor_lista(lista:list)->int:
    """menor_lista

    Args:
        lista (list): pasamos la lista original 

    Returns:
        int: retorna el menor de la lista que pasamos 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    menor = lista[0]
    for el in lista[1: ]:
        if menor > el:
            menor = el 
    return menor


def reduce_list(funcion,lista:list)->any:    #manera generica o mas eficaz de todo lo anterior
    """reduce_list

    Args:
        funcion (_type_): pasamos lo que queremos que haga la funcion
        lista (list): pasamos la lista original 

    Returns:
        any: un entero 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    ant = lista[0]
    for el in lista[1: ]:
        ant = funcion(ant,el)
    return ant

numeros = [1,5,7,8,9,2,7]

#total = reduce_list(lambda ant,actual: ant + actual, numeros)   #asi se utiliza el reduce list(con la forma de la funcion suma)
#print(total)
#mayor = reduce_list(lambda ant,actual: ant if ant > actual else actual,numeros)  #asi se utiliza el reduce list(con la forma de la funcion mayor)
#print(mayor)

def stark_normalizar_datos(lista_heroes: list[dict])-> bool:
    """stark_normalizar_datos

    Args:
        lista_heroes (list[dict]): pasamos un diccionario 

    Returns:
        bool: nos devuelve los datos del diccionario listo para usar
    """
    if not isinstance(lista_heroes, list): raise TypeError ("primer parametro debe ser una lista")
    
    if lista_heroes != []:

        retorno = False
        for i in range(len(lista_heroes)):

            if type(lista_heroes[i]["altura"]) != float:
                altura_float = float(lista_heroes[i]["altura"])
                lista_heroes[i]["altura"] = altura_float
                retorno = True

            if type(lista_heroes[i]["peso"]) != float:
                lista_heroes[i]["peso"] = float(lista_heroes[i]["peso"])
                retorno = True

            if type(lista_heroes[i]["fuerza"]) != int:
                lista_heroes[i]["fuerza"] = int(lista_heroes[i]["fuerza"])
                retorno = True

        return retorno
    
    
def mostrar_dato_super_h(lista_super:list,campo)->any:
    """mostrar_dato_super_h

    Args:
        lista_super (list): pasamos la lista original 
        campo (_type_): pasamos el campo que queremos que nos muestre 

    Returns:
        any: devuelve el dato del campo que pedimos
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for el in lista_super:
        print(el[campo])

def mostrar_datos_super_h(lista_super:list,campo1:str,campo2:str)->any:
    """mostrar_datos_super_h

    Args:
        lista_super (list): pasamos la lista original 
        campo1 (_type_): pasamos el primer campo que queremos que nos muestr 
        campo2 (_type_): pasamos el segundo campo que queremos que nos muestr 

    Returns:
        any: _description_
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for el in lista_super:
        print(el[campo1],el[campo2])

def super_mas_alto_dato(lista_super:list)->str:
    """super_mas_alto_dato

    Args:
        lista_super (list): pasamos la lista original

    Returns:
        str: devuelve cual es el superheroe mas alto 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for _ in lista_super:
        nombre_altura_s = mapear_altura_nombre(lista_super)
        super_mas_alto = calcular_mayor(nombre_altura_s) 
    mensaje = f"el super heroes mas alto es {super_mas_alto}"
    return mensaje

def super_mas_bajo_dato(lista_super:list)->any:
    """super_mas_bajo_dato

    Args:
        lista_super (list): pasamos la lista original

    Returns:
        any: devuelve cual es el superheroe mas bajo 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for _ in lista_personajes:
        nombre_altura_s = mapear_altura_nombre(lista_super)
        super_mas_bajo = calcular_menor(nombre_altura_s) 
    mensaje = (f"el super heroes mas bajo es {super_mas_bajo}")
    return mensaje

def altura_promedio_super(lista_super:list)->any:
    """altura_promedio_super

    Args:
        lista_super (list): pasamos la lista original

    Returns:
        any: devuelve el promedio de altura de super heroes
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for _ in lista_super:
        nombre_altura_s = mapear_list(lambda alt:(alt["altura"]),lista_personajes)
        promedio = calcular_promedio_3_lista(nombre_altura_s) 
    mensaje = (f"el promedio de altura de los super heroes es: {promedio}")
    return mensaje

def super_mas_y_menos_alto(lista_super:list)->any:
    """super_mas_y_menos_alto

    Args:
        lista_super (list): pasamos la lista original 

    Returns:
        any: nos devuelve el superheore mas y menos alto 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    super_mas_alto = super_mas_alto_dato(lista_super)
    super_mas_bajo = super_mas_bajo_dato(lista_super)
    mensaje = f"{super_mas_alto} y {super_mas_bajo}"
    return mensaje

def mas_y_menos_pesado(lista_super:list)->any:
    """mas_y_menos_pesado

    Args:
        lista_super (list): pasamos la lista original
    Returns:
        any: devuelve el super heroe mas y menos pesado
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    for _ in lista_personajes:
        nombre_altura_s = mapear_peso_nombre(lista_super)
        super_mas_pesado = calcular_mayor(nombre_altura_s) 

    for _ in lista_personajes:
        nombre_altura_s = mapear_peso_nombre(lista_super)
        super_menos_pesado = calcular_menor(nombre_altura_s) 
    mensaje = (f"el super heroes mas pesado es {super_mas_pesado} y  el super heroe menos pesado es: {super_menos_pesado}")
    return mensaje





def super_masculino(lista:list)->any: #A
    """super_masculino

    Args:
        lista (list): pasamos la lista original

    Returns:
        any: nos devuelve el nombre de todos los masculinos 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    supers_masculinos = filtrar_listas(lambda emp: emp["genero"] == "M",lista)
    nombres_masculinos = mapear_list(lambda nombre:(nombre["nombre"]),supers_masculinos)    
    return nombres_masculinos






def super_Femenino(lista_super:list)->any: #b
    """super_Femenino

    Args:
        lista_super (list): pasamos la lista original

    Returns:
        any: nos devuelve el nombre de todos los femeninos 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    supers_femenino = filtrar_listas(lambda emp: emp["genero"] == "F",lista_super)
    nombres_femenino = mapear_list(lambda nombre:(nombre["nombre"]),supers_femenino)    
    return nombres_femenino






def mas_alto_masculino(lista_super:list)->any:#c
    """mas_alto_masculino

    Args:
        lista_super (list): pasamos la lista original

    Returns:
        any: devuelve el mas alto de los masculinos
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    supers_masculinos = filtrar_listas(lambda emp: emp["genero"] == "M",lista_super)
    datos_masculinos = mapear_list(lambda datos_mas:(datos_mas["altura"],datos_mas["nombre"]),supers_masculinos)
    mas_alto = calcular_mayor(datos_masculinos)
    return mas_alto





def mas_alto_femenino(lista:list)->any:#d
    """mas_alto_femenino

    Args:
        lista (list): pasamos la lista original 

    Returns:
        any: nos devuelve el femenino mas alto 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    supers_femeninos = filtrar_listas(lambda emp: emp["genero"] == "F",lista)
    datos_femeninos = mapear_list(lambda datos_mas:(datos_mas["altura"],datos_mas["nombre"]),supers_femeninos)
    mas_alto = calcular_mayor(datos_femeninos)
    return mas_alto





def mas_bajo_masculino(lista:list)->any:#e
    """mas_bajo_masculino

    Args:
        lista (list): pasamos la lista original 

    Returns:
        any: nos devuelve el mas bajo de los masculinos 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")

    supers_masculinos = filtrar_listas(lambda emp: emp["genero"] == "M",lista)
    datos_masculinos = mapear_list(lambda datos_mas:(datos_mas["altura"],datos_mas["nombre"]),supers_masculinos)
    mas_bajo = calcular_menor(datos_masculinos)
    return mas_bajo




def mas_bajo_femenino(lista:list)->any:#f
    """mas_bajo_femenino

    Args:
        lista (list): pasamos la lista original 

    Returns:
        any: devuelve el mas bajo de los femeninos 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    supers_femeninos = filtrar_listas(lambda emp: emp["genero"] == "F",lista)
    datos_femeninos = mapear_list(lambda datos_mas:(datos_mas["altura"],datos_mas["nombre"]),supers_femeninos)
    mas_bajo = calcular_menor(datos_femeninos)
    return mas_bajo




def promedio_alt_masculino(lista_super:list)->any:#g
    """promedio_alt_masculino

    Args:
        lista_super (list): pasamos la lista original 

    Returns:
        any: nos devuelve el promedio de altura masculino
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    supers_masculinos = filtrar_listas(lambda emp: emp["genero"] == "M",lista_super)
    datos_masculinos = mapear_list(lambda datos_mas:(datos_mas["altura"]),supers_masculinos)
    mas_alto = calcular_promedio_3_lista(datos_masculinos)
    return mas_alto




def promedio_alt_femenino(lista:list)->any:#h
    """promedio_alt_femenino

    Args:
        lista (list): pasamos la lista original 

    Returns:
        any: nos devuelve el promedio mas alto femenino 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    supers_femenino = filtrar_listas(lambda emp: emp["genero"] == "F",lista)
    datos_femenino = mapear_list(lambda datos_mas:(datos_mas["altura"]),supers_femenino)
    mas_alto = calcular_promedio_3_lista(datos_femenino)
    return mas_alto




def nombre_asociado(lista:list)-> any : # i
    nombre = mapear_list(lambda datos_mas:(datos_mas["altura"]),lista)
    return nombre





def tipo_color_ojos(lista:list,color_a_elegir:str)->any: # j
    """tipo_color_ojos

    Args:
        lista (list): pasamos la lista original 
        color_a_elegir (str): elegimos el color de ojos que queremos 

    Returns:
        any: devuelo cuantas personas tienen ese tipo de color de ojos
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    ojos = mapear_list(lambda ojos:(ojos["color_ojos"]),lista)
    color = contador_color_ojos(ojos,color_a_elegir)
    return color




def agrupar_color_ojos(lista:list,target:str)->any:  #m
    """agrupar_color_ojos

    Args:
        lista (list): pasamos la lista original 
        target (str): elegimos el color de ojos que queremos 

    Returns:
        any: devuelve el nombre de todos los que  tienen ese color de ojos
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    mismo_ojos_color = filtrar_listas(lambda ojos:(ojos["color_ojos"]== target),lista)
    super_nombre_ojos =  mapear_list(lambda nombre: (nombre["nombre"]),mismo_ojos_color)
    return super_nombre_ojos





def agrupar_color_pelo(lista:list,target:str)->any: #n
    """agrupar_color_pelo

    Args:
        lista (list): pasamos la lista original 
        target (str): pasamos el color de pelo que queremos 

    Returns:
        any: nos devuelve el nombre de todos los que tienen ese color de pelo 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    mismo_pelo_color = filtrar_listas(lambda ojos:(ojos["color_pelo"]== target),lista)
    super_nombre_pelo =  mapear_list(lambda nombre: (nombre["nombre"]),mismo_pelo_color)
    return super_nombre_pelo




def agrupar_inteligencia(lista:list,target:str)->any:  #0 
    """agrupar_inteligencia

    Args:
        lista (list): pasamos la lista original
        target (str): pasamos la inteligencia que queremos 

    Returns:
        any: nos devuelve el nombre de todos los que tienen esa inteligencia 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    misma_inteligencia = filtrar_listas(lambda ojos:(ojos["inteligencia"]== target),lista)
    super_nombre_inteligencia =  mapear_list(lambda nombre: (nombre["nombre"]),misma_inteligencia)
    return super_nombre_inteligencia




def tipo_color_pelo(lista:list,color_a_elegir:str)->any: #i
    """tipo_color_pelo

    Args:
        lista (list): lista
        color_a_elegir (str): elegimos el color de pelo que queremos 

    Returns:
        any: nos devuelve la cantidad de heroes que tienen el color de ojos que elgimos 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    ojos = mapear_list(lambda ojos:(ojos["color_pelo"]),lista)
    color = contador_color_ojos(ojos,color_a_elegir)
    return color




def tipo_inteligencia(lista:list,inteligencia:str)->any: #i
    """tipo_inteligencia

    Args:
        lista (list): pasamos la lista original 
        inteligencia (str): elegimos la inteligencia que queremos 

    Returns:
        any: nos devuelve la cantidad de heroes que tienen esa inteligencia 
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    ojos = mapear_list(lambda ojos:(ojos["inteligencia"]),lista)
    rojo = contador_color_ojos(ojos,inteligencia)
    return rojo




def contador_color_ojos(lista:list, target:str)->int:
    """contador_color_ojos

    Args:
        lista (list): pasamos la lista orignial 
        target (str): pasamos el target que queremos contar 

    Returns:
        int: devuelve la cantidad de veces que esta el target en la lista
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    contador_elemento = 0
    for color in lista:
        if color == target:
            contador_elemento+= 1
    return contador_elemento
            
                





    


    
            



