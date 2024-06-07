from data_stark import * 
from funciones_super import *
from menu_tp00_stark import *

stark_normalizar_datos(lista_personajes)
#b


# for el in lista_personajes:
#     print(el["nombre"])
#c


# for el in lista_personajes:
#     print(el["nombre"], el["altura"])
#d


# for el in lista_personajes:
#     nombre_altura_s = mapear_altura_nombre(lista_personajes)
#     super_mas_alto = calcular_mayor(nombre_altura_s) 
# print(f"el super heroes mas alto es {super_mas_alto}")

#e


# for el in lista_personajes:
#     nombre_altura_s = mapear_altura_nombre(lista_personajes)
#     super_mas_bajo = calcular_menor(nombre_altura_s) 
# print(f"el super heroes mas bajo es {super_mas_bajo}")

#f



# for el in lista_personajes:
#     nombre_altura_s = mapear_list(lambda alt:(alt["altura"]),lista_personajes)
#     promedio = calcular_promedio_3_lista(nombre_altura_s) 
# print(f"el promedio de altura de los super heroes es: {promedio}")

#g


# print(f"el super heroe mas alto es : {super_mas_alto[1]} y el super heroe mas bajo es: {super_mas_bajo[1]}")

#h


# for el in lista_personajes:
#     nombre_altura_s = mapear_peso_nombre(lista_personajes)
#     super_mas_pesado = calcular_mayor(nombre_altura_s) 

# for el in lista_personajes:
#     nombre_altura_s = mapear_peso_nombre(lista_personajes)
#     super_menos_pesado = calcular_menor(nombre_altura_s) 
# print(f"el super heroes mas pesado es {super_mas_pesado} y  el super heroe menos pesado es: {super_menos_pesado}")

#i


#j
# while True:
#     match menu_00():
#         case "1":
#             mostrar_dato_super_h(lista_personajes,"nombre")
#         case "2":
#             mostrar_datos_super_h(lista_personajes,"nombre","altura")
#         case "3":
#             mas_alto = super_mas_alto_dato(lista_personajes)
#             print(mas_alto)
#         case "4":
#             mas_bajo = super_mas_bajo_dato(lista_personajes)
#             print(mas_bajo)
#         case "5":
#             promedio = altura_promedio_super(lista_personajes)
#             print(promedio)
#         case "6":
#             mas_y_menos_alto = super_mas_y_menos_alto(lista_personajes)
#             print(mas_y_menos_alto)
#         case "7":
#             mas_y_menos_pesado_s = mas_y_menos_pesado(lista_personajes)
#             print(mas_y_menos_pesado_s)          
#         case "8":
#             break

#     pausar()
# print("Fin del programa")


while True:
    match menu_01():
        case "1":
            super_masc = super_masculino(lista_personajes)
            print(super_masc)
            
        case "2":
            super_fem = super_Femenino(lista_personajes)
            print(super_fem)
        case "3":
            mas_alto_mas = mas_alto_masculino(lista_personajes)
            print(mas_alto_mas)
        case "4":
            mas_alta_fem = mas_alto_femenino(lista_personajes)
            print(mas_alta_fem)
        case "5":
            mas_bajo_mas = mas_bajo_masculino(lista_personajes)
            print(mas_bajo_mas)
        case "6":
            mas_bajo_fem = mas_bajo_femenino(lista_personajes)
            print(mas_bajo_fem)
            
        case "7":
            promedio_mas = promedio_alt_masculino(lista_personajes)       
            print(promedio_mas)
        case "8":
            promedio_fem = promedio_alt_femenino(lista_personajes)
            print(promedio_fem)
            
        case "9":
            marron = tipo_color_ojos(lista_personajes,"Brown")
            azul = tipo_color_ojos(lista_personajes,"Blue")
            verde = tipo_color_ojos(lista_personajes,"Green")
            hazel = tipo_color_ojos(lista_personajes,"Hazel")
            amarillo = tipo_color_ojos(lista_personajes,"Yellow")
            rojo = tipo_color_ojos(lista_personajes,"Red")
            silver = tipo_color_ojos(lista_personajes,"Silver")
            mensaje =f"el tipo de ojo marron lo tienen : {marron} superheroes \n el tipo de ojo azul lo tienen : {azul}\nel tipo de ojo verde lo tienen :{verde}  \nel tipo de ojo hazel lo tienen :{hazel}  \nel tipo de ojo amarillo lo tienen :{amarillo} \nel tipo de ojo rojo lo tienen :{rojo}  \nel tipo de ojo silver lo tienen :{silver}"
            print(mensaje)
        case "10":
            negro = tipo_color_pelo(lista_personajes,"Black")
            Blond = tipo_color_pelo(lista_personajes,"Blond")
            NoHair = tipo_color_pelo(lista_personajes,"No Hair")
            Brown_White = tipo_color_pelo(lista_personajes,"Brown / White")
            Red = tipo_color_pelo(lista_personajes,"Red")
            Green = tipo_color_pelo(lista_personajes,"Green")
            White = tipo_color_pelo(lista_personajes,"White")
            Red_Orange = tipo_color_pelo(lista_personajes,"Red / Orange")
            Auburn = tipo_color_pelo(lista_personajes,"Auburn")
            mensaje =f"color pelo :\n negro : {negro}  \n Blond : {Blond}\n Brown_White :{Brown_White}  \n Red:{Red}  \n Green:{Green} \nWhite:{White}  \n Red/Orange:{Red_Orange}\n Auburn : {Auburn}"
            print(mensaje)
        case "11":
            average = tipo_inteligencia(lista_personajes,"average")
            good = tipo_inteligencia(lista_personajes,"good")
            high = tipo_inteligencia(lista_personajes,"high")
            no_se = tipo_inteligencia(lista_personajes,"")
            mensaje = f"tipo de inteligencia \n average : {average}\n good: {good}   \nhigh: {high}   \n no se sabe:{no_se}  "
            print(mensaje)
        case "12":
            marron = agrupar_color_ojos(lista_personajes,"Brown")
            azul = agrupar_color_ojos(lista_personajes,"Blue")
            verde = agrupar_color_ojos(lista_personajes,"Green")
            hazel = agrupar_color_ojos(lista_personajes,"Hazel")
            amarillo = agrupar_color_ojos(lista_personajes,"Yellow")
            rojo = agrupar_color_ojos(lista_personajes,"Red")
            silver = agrupar_color_ojos(lista_personajes,"Silver")
            mensaje =f"el tipo de ojo marron lo tienen : {marron} superheroes \n el tipo de ojo azul lo tienen : {azul}\nel tipo de ojo verde lo tienen :{verde}  \nel tipo de ojo hazel lo tienen :{hazel}  \nel tipo de ojo amarillo lo tienen :{amarillo} \nel tipo de ojo rojo lo tienen :{rojo}  \nel tipo de ojo silver lo tienen :{silver}"
            print(mensaje)
        case "13":
            negro = agrupar_color_pelo(lista_personajes,"Black")
            Blond = agrupar_color_pelo(lista_personajes,"Blond")
            NoHair = agrupar_color_pelo(lista_personajes,"No Hair")
            Brown_White = agrupar_color_pelo(lista_personajes,"Brown / White")
            Red = agrupar_color_pelo(lista_personajes,"Red")
            Green = agrupar_color_pelo(lista_personajes,"Green")
            White = agrupar_color_pelo(lista_personajes,"White")
            Red_Orange = agrupar_color_pelo(lista_personajes,"Red / Orange")
            Auburn = agrupar_color_pelo(lista_personajes,"Auburn")
            mensaje =f"color pelo :\n {negro} superheroes \n Blond : {Blond}\nBrown_White :{Brown_White}  \n Red:{Red}  \n Green:{Green} \nWhite:{White}  \n Red/Orange:{Red_Orange}\n Auburn : {Auburn}"
            print(mensaje)
        case "14":
            average = agrupar_inteligencia(lista_personajes,"average")
            good = agrupar_inteligencia(lista_personajes,"good")
            high = agrupar_inteligencia(lista_personajes,"high")
            no_se = agrupar_inteligencia(lista_personajes,"")
            mensaje = f"tipo de inteligencia \n average : {average}\n good: {good}   \nhigh: {high}   \n no se sabe:{no_se}  "
            print(mensaje)
        case "15":
            break

    pausar()
print("Fin del programa")

# lista_a = []
# for i in range(len(nombre_altura_s)):
#     altura = float(nombre_altura_s[i][0])
#     lista_a.append(altura)



# mayor_a = calcular_mayor(lista_a)


# print(mayor_a)
    


#print(super_mas_alto)
#print(super_mas_alto)
#print(f"el super heroe mas alto es {super_mas_alto[1]}")