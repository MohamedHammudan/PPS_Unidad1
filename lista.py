"""
Realiza, utilizando Python 3, el ejercicio 3 de la página 35 del libro “Introducción a
Python” de Jon Vadillo e inclúyelo en un fichero llamado lista.py. Las funciones que
debes usar en el ejercicio 3 deben utilizar OBLIGATORIAMENTE las siguientes
cabeceras:

Ejercicio 3
Crea un programa que reciba un número del 1 al 20 introducido por el usuario y compruebe si está
dentro de la siguiente lista: [6,14,11,3,2,1,15,19]. Implementa una función que se asegure que el
número introducido por el usuario está en el rango indicado y otra que compruebe si está dentro
de la lista. Trata de crear las funciones de forma que puedan ser reutilizadas lo máximo posible en
otros programas.


"""

minimo=1
maximo=20
lista = [6,14,11,3,2,1,15,19]
valor = int(input("introduzca un numero entre el 1 y el 20 :  ")) 



def estaEnLista(valor,lista) :
        if valor in lista : 
            print(f" El numero {valor}  esta dentro de la lista")
            return True
        else :
            print("El valor introducido no esta dentro de la lista")
            return False



def estaEnRango(valor,minimo,maximo) :
    while valor > 20 or valor < 1 :
        print("porfavor introduce un numero entre el 1 y el 20 ")
        valor = int(input("introduzca un numero entre el 1 y el 20 :  ")) 
    else :
        estaEnLista(valor,lista) 

estaEnRango(valor,1,20)

