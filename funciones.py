
'''

def string_corto(valor1):
    cadena=valor1

    cadena=cadena.strip.replace(".","").replace(","," ").replace(";"," ")

    cadena=cadena.split()
    palabra_corta = cadena[0]

    for i in cadena:
        if len(palabra_corta) >= len(i):
            palabra_corta = i
        else:
            palabra_corta = palabra_corta
    long_palabra = len(palabra_corta)

    print("La palabra mas corta tiene: ", len(palabra_corta), "carácteres")
    print("La palabra mas corta es: ", palabra_corta)
    return palabra_corta, long_palabra
'''

def string_corto():
    
    cadena=input("Ingrese una cadena de texto: ")
    outside="  "
    inside=".,;"
    trans=cadena.maketrans(".,;","   ")
    cadena=cadena.translate(trans)
    lista_cadena=cadena.split()
    palabra_corta= lista_cadena[0]
    lista_auxiliar=[]
    #lista_auxiliar.append(palabra_corta)
    for i in lista_cadena:
       if len(palabra_corta)>len(i):
          del lista_auxiliar[::]
          palabra_corta=i
          lista_auxiliar.append(palabra_corta)
       elif len (palabra_corta)==len(i):
          #lista_auxiliar.append(palabra_corta)
          lista_auxiliar.append(i)
          palabra_corta=i
    
    print ("Las palabras cortas son: ",lista_auxiliar)
    palabras_cortas=lista_auxiliar
    return palabras_cortas

#string_corto()

def string_largo():
    
    cadena=input("Ingrese una cadena de texto: ")
    outside="  "
    inside=".,;"
    trans=cadena.maketrans(".,;","   ")
    cadena=cadena.translate(trans)
    lista_cadena=cadena.split()
    palabra_larga= lista_cadena[0]
    lista_auxiliar=[]
    #lista_auxiliar.append(palabra_corta)
    for i in lista_cadena:
       if len(palabra_larga)<len(i):
          del lista_auxiliar[::]
          palabra_larga=i
          lista_auxiliar.append(palabra_larga)
       elif len (palabra_larga)==len(i):
          #lista_auxiliar.append(palabra_corta)
          lista_auxiliar.append(i)
          palabra_larga=i
    
    print ("Las palabras largas son: ",lista_auxiliar)
    palabras_largas=lista_auxiliar
    return palabras_largas  
#string_largo()


##################################################3
def multiplicacion(valor1, valor2):
    a=int(valor1)
    b=int(valor2)
    c = 0
    suma=0
    if ((a < 0 and b < 0)):
        for i in range(b, 0):
            suma += - a
    elif (a > 0 and b < 0) or (a > 0 and b > 0):
        for i in range(0, a):
            suma += b
    else:
        if (b > 0 and a < 0):
            for i in range(0, b):
                suma += a
    print("La multiplicacion es", suma)

    return suma
####################
def potencias(valor1,valor2 ):
    c=int(valor1)
    d=int(valor2)
    multi = 1
    e = 0
    potencia = 0
    if (d >= 0):
        for i in range(0, d):
            multi = multi * c
        potencia = multi

    elif (d < 0):
        for i in range(d, 0):
            multi = multi * c
        potencia = 1 / multi
    print("La potencia es", potencia)
    return potencia
#######################
def division(valor1, valor2):
    dividendo=int(valor1)
    sor=int(valor2)
    div = 0
    if ((abs(dividendo) > abs(sor)) and (sor != 0)):
        if ((dividendo > 0 and sor > 0) or (dividendo < 0 and sor < 0)):
            resto = dividendo

            while (abs(resto) >= abs(sor)):
                resto += - sor
                div += + 1

        else:
            if ((dividendo > 0 and sor < 0) or (dividendo < 0 and sor > 0)):
                resto = abs(dividendo)
                sor = abs(sor)
                while (resto >= sor):
                    resto += - sor
                    div += + 1
                div = -div
                resto = -resto

    else:
        if dividendo == 0:
            div = 0
            resto = dividendo
        elif sor == 0:
            print("No se puede dividir por 0")
    print("La división es:", div)
    print("El resto es:", resto)
    return div, resto
######################

def contar_palabras():
    cadena=input("Ingrese una cadena de texto: ")

    contador_palabras=0

    cadena=cadena.strip()
    for caracter in cadena:
        if caracter == " " or caracter == "." or caracter == ";" or caracter == ",":
            contador_palabras += 1
        else:
            contador_palabras = contador_palabras
    print("Hay ",contador_palabras, "palabras en la cadena de texto.")

    return contador_palabras


    

def solicitud():

    valor_1=input("Ingrese un Parametro: ")
    valor_2=input("Ingrese un Parametro: ")
    
    return valor_1=="",valor_2==""

def imprimir(parametro_1="", parametro_2=""):

    print(parametro_1, parametro_2)
