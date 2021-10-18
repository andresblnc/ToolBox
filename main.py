from gtt import *
from conjuntos import *

welcome()
print()
print("Qué quieres hacer?")
resp = int(input(">"))

while True:
    while resp < 1 or resp > 5:
        print("Respuesta no disponible, intenta de nuevo")
        resp = int(input(">"))

    if resp == 1:
        tablas()
        print()
        input("Escribe enter para continuar.")

    if resp == 2:
        print("Oh, aún no hemos trabajado sobre esa opción. Vuelve pronto.")

    if resp == 3:
        print("Oh, aún no hemos trabajado sobre esa opción. Vuelve pronto.")

    if resp == 4:
        print("Oh, aún no hemos trabajado sobre esa opción. Vuelve pronto.")

    if resp == 5:
        print("Gracias por utilizar nuestro programa. :)")
        input("Presiona enter para salir")
        break


    menu()
    print("Qué quieres hacer ahora?")
    resp = int(input(">")) 
