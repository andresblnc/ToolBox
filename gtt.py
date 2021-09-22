import time, re
from tqdm import tqdm
from tabulate import tabulate
#https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data



#PARA IMPIMIR DE COLOpartes SE HACE ASÍ, PARA CAMBIAR COLOR CAMBIAS EL DONDE DICE MORADO, EL ULTIMO ES PARA QUE SE REINCIE Y NO IMPRIMA MORADO DE AHÍ EN ADELANTE
#print(f"{bcolors.MORADO}Warning: No active frommets remain. Continue?{bcolors.ENDC}")



def menu():
    print(f"{bcolors.ENDC}")
    print("{: ^40s}".format("MENÚ PRINCIPAL"))
    print("{: <20s}".format("1- Generador de Tablas de Verdad",end=""))
    print("{: >20s}".format("2- Opción aún no disponible"))
    print("{: <20s}".format("3- Opción aún no disponible",end=""))
    print("{: >20s}".format("4- Opción aún no disponible"))
    print()

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

#FUNCIÓN DE BIENVENIDA
def welcome():

    for i in range(2):
        print()
    
    print("Iniciando sistema",end="")
    for i in range(4):
        time.sleep(1)
        print(".",end="")
    print(" ")


    print(f"{bcolors.GREEN}")
    for i in tqdm(range(100), desc=""):
        time.sleep(0.01)
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

    menu()


#Aquí va todo lo que tenemos que hacer para las tablas de verdad.
def tablas():
    print(f"{bcolors.CYAN}")

    def condicional(exp):
        if "=>" in exp:
            init = exp[exp.index("=")-1]
            final = exp[exp.index(">")+1]
            return "(!"+init+"|"+final+")"
        else:
            return exp

    def space_print(exp, num):
        exp_sub = ""
        for i in range(num//2):
            exp_sub = exp_sub + " "
        exp_sub = exp_sub + exp
        for i in range(num//2):
            exp_sub = exp_sub + " "
        return exp_sub

    lista_variables 	= []
    table 			= []
    table_row 		= []
    par_count 		= 0
    space 			= 0

    variables = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    print("GENERADOR DE TABLAS DE VERDAD")
    signos = [["PARENTESIS","()"],["AND","&"],["OR","|"],["NOT","!"],["IMPLICACIÓN","=>"],["BICONDICIONAL","<=>"]]
    print(tabulate(signos))
    print("Nuestro programa soporta todas las letras: ", *variables)
    print()

    print("Escribe tu enunciado :")
    entrada = input(">")

    #Quitamos mayuscylas y espacios
    argumento_log = entrada.lower()
    argumento_log = argumento_log.replace(' ', '')

    print()
    print("TABLA DE VERDAD")
    for i in range(30):
        print("=", end="")
    print()
    print(f'Tú enunciado: {argumento_log}')
    for i in range(30):
        print("=", end="")
    print()

    #Compilamos todas las letras para trabajar más fácil
    name_regex = re.compile(r"[a-z]")
    for i in range (len(variables)):
        if variables[i] in argumento_log:
            lista_variables = lista_variables + list(variables[i])

    #Buscamos por exppartesiones dentro de parentesis por primera vez
    partes = re.findall(r'\(.*?\)', argumento_log)

    i = 0
    for exp in partes:
        #revisamos si la expresion contiene partes por primera vez
        for letter in str(exp):
            if letter=="(":
                par_count+=1
        #tiene partes dentro de ella
        if par_count > 1 : 
            partes_i = partes[i]
            partes[i] = partes_i[1:]
            #las detectamos y ponemos como una expresion nueva
            sub_partes = re.findall(r'\(.*?\)', partes[i]) 
            partes = partes + list(sub_partes)
        i+=1
        par_count = 0
    partes.append(str(argumento_log))
    imp_partes = partes[:]

    ##PROCESO DE BICONDICIONAL
    i = 0
    for exp in partes:
        if "<=>" in exp:
            #delimitamos de donde a donde tomar
            init = exp[exp.index("<=>")-1]
            final = exp[exp.index("<=>")+3]
            #Buscamos por más partes de nuevo usando parentesis
            if init==")" :
                exp_sub = exp[:exp.index("<")]
                exp_sub = exp_sub[exp_sub.index("("):exp_sub.index(")")+1]
                init = condicional(exp_sub)
            if final=="(" :
                exp_sub = exp[exp.index("<=>")+3:]
                exp_sub = exp_sub[exp_sub.index("("):exp_sub.index(")")+1]
                final = condicional(exp_sub)
            #ESCRIBIMOS SU EQUIVALENTE EN ALGO QUE PYTHON PUEDA USAR
            new_exp = "(!"+init+"|"+final+")&(!"+final+"|"+init+")"
            partes[i] = new_exp
        i+=1


    ##PROCESO DE CONDICIONAL
    i = 0
    for exp in partes:
        partes[i] = condicional(exp)
        i+=1

    ##CREAMOS LA TABLA PERO ÁUN NO PONEMOS NADA
    number_rows = 2 ** len(lista_variables) 
    for i in range(number_rows):
        ##LLENAMOS LA TABLA CON VALORES DE 0
        current_bin = bin(i)[2:].zfill(len(lista_variables))
        for letter in str(current_bin):
            table_row = table_row + list(letter)
        table.append(table_row)

        val_eval = table[i]
        j = 0

        ##EVALUAMOS CADA EXPRESION POR SEPARADO
        for sub_exp in partes:
            argumento_log = str(sub_exp)
            ##USAMOS SU VALOR ACTUAL EN LA FILA PARA EVUALUAR LA VARIABLE
            for var in lista_variables:
                argumento_log = argumento_log.replace(str(var), str(val_eval[j]))
                j += 1
            j=0

            ##VOLVEMOS A CAMBIAR LA EXPRESION PARA PYTHON
            argumento_log = argumento_log.replace("&", " and ")
            argumento_log = argumento_log.replace("|", " or " )  
            argumento_log = argumento_log.replace("!", " not ")
            
            #SE EVALÚA Y SE ESCRIBE
            resultado = str(eval(argumento_log))
            resultado = "1" if (resultado=="True" or resultado == "1") else "0"
            table[i] = table[i] + (list(resultado))
            argumento_log = sub_exp
            table_row = []

    #POR ÚLTIMO LA TABLA
    lista_variables = lista_variables + (imp_partes)
    print(f"{bcolors.ENDC}")
    print(*lista_variables, sep = "\t")
    print(f"{bcolors.BOLD}")

    for row in table:
        fila = ""
        i=0
        for item in row:
            space = len(str(lista_variables[i]))
            fila = fila + space_print(item, space)+"\t"
            i+=1
        print(fila)