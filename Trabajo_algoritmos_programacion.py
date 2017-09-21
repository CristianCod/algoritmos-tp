

import funciones
import os
def menu():
    os.system('cls')
    print("Selecciona una opción")
    print("1 - Numérico")
    print("2 - Cadenas de carácteres")
    print("3 - Salir")
    opcion=int(input("Ingrese una Opcion: "))
    return opcion


def sub_menu_num():
    os.system("cls")
    print("Selecciona una opción")
    print("1 - Multiplicación")
    print("2 - División y resto")
    print("3 - Potencia")
    print("4 - Volver al Menú principal")
    opcion=int(input("Ingrese una Opcion: "))
    
    return opcion

def sub_menu_let():
    os.system("cls")
    print("Selecciona una opción")
    print("1 - Palabra mas Larga")
    print("2 - Palabra mas corta")
    print("3 - Contar Palabras")
    print("4 - Volver al Menú principal")
    opcion=int(input("Ingrese una Opcion: "))
    return opcion

salir=1
if salir==1:
    os.system('cls')

    opcion=menu()
    if opcion == 1:
        print("Estas en la Opcion Menú Numerico")
       
        opcion=sub_menu_num()
           
        if opcion == 1:
            continuar=1
            while continuar==1:   
                 valor1, valor2=funciones.solicitud()
                 parametro_1=funciones.multiplicacion(valor1, valor2)
                 funciones.imprimir(parametro_1)
                   
                 print("1 - Continuar")
                 print("2 - Ir al menú")
                 continuar=int(input("¿Quiere continuar operando? "))
           
        
        elif opcion == 2:
             continuar=1
             while continuar==1:  
                 valor1, valor2=funciones.solicitud()
                 parametro_1, parametro_2=funciones.division(valor1,valor2)
                 funciones.imprimir(parametro_1,parametro_2)
                 print("1 - Continuar")
                 print("2 - Ir al menú")
                 continuar=int(input("¿Quiere continuar operando? "))

        elif opcion == 3:
               continuar=1
               while continuar==1:
       
                   valor1, valor2=funciones.solicitud()
                   parametro_1=funciones.potencias(valor1, valor2)
                   funciones.imprimir(parametro_1)
                   print("1 - Continuar")
                   print("2 - Ir al menú")
                   continuar=int(input("¿Quiere continuar operando? "))
                   salir=int(("Ir al menú"))
                
        
        elif opcion == 4:
            salir=2
            #menu()
                   

    elif opcion == 2:
        
       
        
        print("Estas en la Opcion Menú de Cadenas de Texto")
        opcion=sub_menu_let()
        
        
        if opcion == 1:
            continuar=1
            while continuar==1:
                
                parametro_1=funciones.string_largo()
                funciones.imprimir(parametro_1)
                print("1 - Continuar")
                print("2 - Ir al menú")
                continuar=int(input("¿Quiere continuar operando? "))

             
        elif opcion == 2:
            continuar=1
            while continuar==1:
                
                parametro_1=funciones.string_corto()
                funciones.imprimir(parametro_1)
                print("1 - Continuar")
                print("2 - Ir al menú")
                continuar=int(input("¿Quiere continuar operando? "))
                   
           
        elif opcion == 3:
            continuar=1
            while continuar==1:
                
                parametro_1=funciones.contar_palabras()
                funciones.imprimir(parametro_1)
                print("1 - Continuar")
                print("2 - Ir al menú")
                continuar=int(input("¿Quiere continuar operando? "))
             
        elif opcion == 4:
             input("\nPresiona una tecla para continuar")
             menu()
        else:
             input("\nPresiona una tecla para continuar")
             sub_menu_let()

    elif opcion == 3:
        print("Estas en la Opcion Salir")
        salir=4
       
    else:    
        menu()
    

