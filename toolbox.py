import time



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
    for i in range(10):
        print()
    
    print("Iniciando sistema",end="")
    for i in range(5):
        time.sleep(1)
        print(".",end="")

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
    print(f"{bcolors.FAIL}\__/     \__\________\________\______/ \______/\__|     \__\________|")


