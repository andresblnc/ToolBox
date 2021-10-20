#Aqui va todo el programa para conjuntos

def conjuntos():

    #Iniciamos los conjuntos
    U,A,B,C= [],[],[],[]    #CONJUNTOS FINALES
    a,b,c = "", "", ""      #ENTRADA DE USUARIO
    aa,bb,cc = [],[],[]     #CONJUNTOS CON REPETIDOS

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