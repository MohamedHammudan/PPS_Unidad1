"""
2. Realiza, utilizando Python 3, un programa llamado binario.py que pida al usuario que
introduzca un número binario e imprima por pantalla el número en formato decimal.
Para desarrollar el programa, es necesario que desarrolles una función con la
siguiente cabecera:

def esBinario(strbinario)
# Devuelve True o False si la cadena de caracteres (strbinario) que se ha pasado
como parámetro contiene una cadena binaria.

# Ejemplo de esBinario:
print(esBinario(“1001”))
True

print(esBinario(“Hola”))
False

"""


#primera forma
numero = input("Introduzca el numero:   ")

def esBinario(numero):
    
    flag=0
    for bit in numero :
        if ((bit != "0") and (bit != "1")):
            print(flag)
            flag=1
    if flag != 0 :
        return False
    else :
        return True

def convierte_a_decimal(numero):
    if esBinario(numero) :
        posicion= len(numero) - 1 
        decimal=0 
        for bit in numero :
            decimal+=int(bit)*pow(2,posicion)
            posicion-=1     
        print(decimal)
    else:
        print("el numero no es binario")



convierte_a_decimal(numero)

#segunda forma 
def convierte_a_decimal_2(numero):
    if esBinario(numero) :
        binario=int(numero, 2)
        print(binario)
    else:
        print("el numero no es binario")
convierte_a_decimal_2(numero)