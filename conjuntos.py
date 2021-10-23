#Aqui va todo el programa para conjuntos

#Iniciamos los conjuntos
U,A,B,C= [],[],[],[]    #CONJUNTOS FINALES
a,b,c = "", "", ""      #ENTRADA DE USUARIO
aa,bb,cc = [],[],[]     #CONJUNTOS CON REPETIDOS


def menu_conj():
    print("{: ^40s}".format("MENÚ OPERACIONES DE CONJUNTOS"))
    print("{: <20s}".format("1- Union de Conjuntos"))
    print("{: <20s}".format("2- Intersección de Conjuntos"))
    print("{: <20s}".format("3- Diferencia de Conjuntos"))
    print("{: <20s}".format("4- Diferencia Simétrica de Conjuntos"))
    print("{: <20s}".format("5- Volver al menú principal"))
    print()

def dif():
    print("Perfecto, que conjuntos quieres utilizar?")
    print("Te recuerdo tus conjuntos.")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"C = {C}")
    print(f"U = {U}")
    print()
    print("Escribe de esta manera A - B")
    response = input(">")
    response = response.strip().upper()
    if response[0] == "A":
        conj_1 = A
    if response[0] == "B":
        conj_1 = B
    if response[0] == "C":
        conj_1 = C
    if response[0] == "U":
        conj_1 = U

    if response[2] == "A":
        conj_2 = A
    if response[2] == "B":
        conj_2 = B
    if response[2] == "C":
        conj_2 = C
    if response[2] == "U":
        conj_2 = U
    
    helper = []
    for value in conj_1:
        if value in conj_2:
            pass
        else:
            helper.append(value)
    
    print()
    print(f"La respuesta es: {helper}")
    print("Quieres hacer otra diferencia usando esa respuesta?")
    again = input("y/n ->")

    if again.lower() == "y":
        print("Perfecto, que conjuntos quieres utilizar?")
        print("Te recuerdo tus conjuntos.")
        print(f"A = {A}")
        print(f"B = {B}")
        print(f"C = {C}")
        print(f"U = {U}")
        print(f"N = {helper}")
        print()
        print("Escribe de esta manera A - B")
        print("Donde quieras usar la respuesta anterior usa N")
        response = input(">")
        response = response.strip().upper()
        if response[0] == "A":
            conj_1 = A
        if response[0] == "B":
            conj_1 = B
        if response[0] == "C":
            conj_1 = C
        if response[0] == "U":
            conj_1 = U
        if response[0] == "N":
            conj_1 = helper

        if response[2] == "A":
            conj_2 = A
        if response[2] == "B":
            conj_2 = B
        if response[2] == "C":
            conj_2 = C
        if response[2] == "U":
            conj_2 = U
        if response[2] == "N":
            conj_2 = helper

        new = []
        for value in conj_1:
            if value in conj_2:
                pass
        else:
            new.append(value)
        
        print(f"{bcolors.ENDC}")
        print(f"La respuesta es: {new}")
    else:
        print("OK!")
        


def dif_sim():
    print("Entro")
    pass

def union():
    print("Entro")
    pass

def interseccion():
    print("Entro")
    pass


def crear_conjuntos():
    #Adquirimos conjuntos
    print()
    print("Muy bien porque no nos dices tus conjuntos.")
    print("Escribe los valores separados por comas. No escribas '}' ni ',' al final.")
    print("Empecemos por el A")
    a = input("A = {")
    print()
    print("Sigamos con el B")
    b = input("B = {")
    print()
    print("Terminemos con el C")
    c = input("C = {")
    print()

    #Limpiamos conjuntos
    a = a.strip(" ")
    b = b.strip(" ")
    c = c.strip(" ")

    aa = a.split(",")
    bb = b.split(",")
    cc = c.split(",")

    #Creamos los conjuntos ya limpios
    for element in aa:
        if element in A:
            pass
        else:
            A.append(element)
        
    for element in bb:
        if element in B:
            pass
        else:
            B.append(element)
        
    for element in cc:
        if element in C:
            pass
        else:
            C.append(element)
        
    #Creamos el conjunto Universal
    for element in A:
        if element in U:
            pass
        else:
            U.append(element)

    for element in B:
        if element in U:
            pass
        else:
            U.append(element)
        
    for element in C:
        if element in U:
            pass
        else:
            U.append(element)
        
def conjuntos():
    crear_conjuntos()
    while True:
        menu_conj()
        print("Qué quieres hacer?")
        op = int(input(">"))

        while op < 1 or op > 5:
            print("Opción no válida. Intenta de nuevo.")
            op = input(">")
            
        if op == 1:
            print()
            union()

        if op == 2:
            print()
            interseccion()

        if op == 3:
            print()
            dif()

        if op == 4:
            print()
            dif_sim()

        if op == 5:
            break
