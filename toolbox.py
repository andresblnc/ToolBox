import time
from tqdm import tqdm
from tabulate import tabulate
#https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data



#PARA IMPIMIR DE COLORES SE HACE ASÍ, PARA CAMBIAR COLOR CAMBIAS EL DONDE DICE MORADO, EL ULTIMO ES PARA QUE SE REINCIE Y NO IMPRIMA MORADO DE AHÍ EN ADELANTE
#print(f"{bcolors.MORADO}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

class bcolors:  # ESTE BLOQUE DEFINE LOS COLORES
    MORADO = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


def welcome():  #FUNCIÓN DE BIENVENIDA
    for i in range(2):
        print()
    
    print("Iniciando sistema",end="")
    for i in range(4):
        time.sleep(1)
        print(".",end="")
    print(" ")


    print(f"{bcolors.GREEN}")
    for i in tqdm(range(100), desc=""):
        time.sleep(0.02)
    print()
    print()

    for i in range(3):
        print()
    
    print(f"{bcolors.FAIL}$$\      $$\$$$$$$$$\$$\      $$$$$$\  $$$$$$\ $$\      $$\$$$$$$$$\ ")
    time.sleep(0.2)
    print(f"{bcolors.MORADO}$$ | $\  $$ $$  _____$$ |    $$  __$$\$$  __$$\$$$\    $$$ $$  _____|")
    time.sleep(0.2)
    print(f"{bcolors.BLUE}$$ |$$$\ $$ $$ |     $$ |    $$ /  \__$$ /  $$ $$$$\  $$$$ $$ |      ")
    time.sleep(0.2)
    print(f"{bcolors.WARNING}$$ $$ $$\$$ $$$$$\   $$ |    $$ |     $$ |  $$ $$\$$\$$ $$ $$$$$\    ")
    time.sleep(0.2)
    print(f"{bcolors.WARNING}$$$$  _$$$$ $$  __|  $$ |    $$ |     $$ |  $$ $$ \$$$  $$ $$  __|   ")
    time.sleep(0.2)
    print(f"{bcolors.BLUE}$$$  / \$$$ $$ |     $$ |    $$ |  $$\$$ |  $$ $$ |\$  /$$ $$ |      ")
    time.sleep(0.2)
    print(f"{bcolors.MORADO}$$  /   \$$ $$$$$$$$\$$$$$$$$\$$$$$$  |$$$$$$  $$ | \_/ $$ $$$$$$$$\ ")
    time.sleep(0.2)
    print(f"{bcolors.FAIL}\__/     \__\________\________\______/ \______/\__|     \__\________|{bcolors.ENDC}")
    print(f"{bcolors.GREEN}")

    print(f"{bcolors.WARNING}")
    print("{: ^40s}".format("MENÚ PRINCIPAL"))
    print("{: <20s}".format("1- Generador de Tablas de Verdad",end=""))
    print("{: >20s}".format("2- Opción aún no disponible"))
    print("{: <20s}".format("3- Opción aún no disponible",end=""))
    print("{: >20s}".format("4- Opción aún no disponible"))


#Aquí va todo lo que tenemos que hacer para las tablas de verdad.
def tablas():
    print(f"{bcolors.CYAN}")
    print("Perfecto!, para empezar, porqué no nos dices cuantas variables vas a utilizar?")
    print("Puedes usar todas las letras menos la letra v")
    num_var = int(input(">"))
    variables = []
    #Pregunta por las variables y las guarda
    for i in range(1,num_var+1):
        print(f"Escribe la variable {i}:")
        var = input(">")
        variables.append(var)

    print()
    print("Los signos que utiliza el programa son:", end="")
    print()
    signos = [["PARENTESIS","()"],["AND","&"],["OR","|"],["NOT","!"],["XOR","+"],["IMPLICACIÓN",">"],["BICONDICIONAL","*"]]
    print(tabulate(signos))
    print()

    #Pregunta por el número de pasos del problema
    print("Perfecto!, cuántos pasos tiene tú problema?")
    print("Por ejemplo, el problema (p&q>r) tendría dos pasos.")
    print("El primer paso sería  p&q  y el segundo sería  (p&q)>r")
    pasos = int(input(">"))
    print()

    #Explica como dividir el problema en pasos
    print("Perfecto! Ahora dinos cada uno de tus pasos por separado.")
    print("El último paso debe de ser el problema completo.")
    print(tabulate(signos))
    partes = []
    #Recibe el problema por partes
    for i in range(1,pasos+1):
        print(f"Escribe el paso {i}:")
        pieza = input(">")
        partes.append(pieza)
    


#MENÚ
welcome()
print()
print("Qué quieres hacer?")
resp = int(input(">"))

while resp < 1 or resp > 4:
    print("Respuesta no disponible, intenta de nuevo")
    resp = int(input(">"))

if resp == 1:
    tablas()
else:
    print("Oh, aún no hemos trabajado sobre esa opción. Vuelve pronto.")