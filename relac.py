def relaciones():
    NODOS = []
    RELACION = []

    #RELACION
    arr = input("\nEscribe los valores del dominio separados por comas: ")
    if(len(arr) != 0):
        NODOS = list(map(str,arr.split(',')))


    Relacion_raw = "1"
    while Relacion_raw != "":
        print("Escribe tus relaciones de una en una, separando los nodos con comas. Cuando termines dejalo vacío y da enter.")
        Relacion_raw = input("\nRelaciones: ")
        if(len(Relacion_raw) != 0):
            Relacion_raw = list(map(str,Relacion_raw.split(',')))
            print(Relacion_raw)
            RELACION.append(tuple(Relacion_raw))
    RELACION.pop(len(RELACION)-1)#Quitamos el vacio


    print("\nMuy bien! Estos son tus datos:")
    print("NODOS: ",NODOS)
    print("RELACIONES: ",RELACION)
    print()

    num_nodos = len(NODOS)
    num_relaciones = len(RELACION)

    #REFELEXIVOS
    isReflexivo = 0
    for i in range(num_relaciones):
        par_nodos = (RELACION[i]) #par de nodos
        nodo1 = par_nodos[0] #nodo inicial
        nodo2 = par_nodos[1] #nodo secundario

        if (nodo1 == nodo2):
            isReflexivo=isReflexivo+1
            print("Los nodos: ",par_nodos, " son reflexivos")


    if (isReflexivo) >= num_nodos:
        print("El conjunto de pares son reflexivos")
    else :
        print("En el conjunto de pares 1 o más no son simetricos.")


    #SIMETRICOS
    isSimetrico = 1 #empezamos con 1 porque solo se cambia cuando se incumple
    for i in range(num_relaciones):
        par_nodos = (RELACION[i])
        nodo1 = par_nodos[0]
        nodo2 = par_nodos[1]

        if (str(nodo2), str(nodo1)) in RELACION:
            print("Los nodos:",par_nodos, "son simetricos")
        else:
            print("Los nodos:",par_nodos, "no son simetricos")
            isSimetrico = 0

    if isSimetrico == 1:
        print("El conjunto de nodos son simetricos")
    else:
        print("En el conjunto de nodos 1 o más no son simetricos")
        

    #TRANSITIVOS
    isTransitivo = 1
    for i in range(num_relaciones):
        par_nodos = (RELACION[i])
        nodox = par_nodos[0]
        nodoy = par_nodos[1]
        for j in range(num_relaciones):
            par_2 = (RELACION[j])
            node2_y = par_2[0]
            node1_z = par_2[1]

            if(nodoy == node2_y):
                node_y = node2_y
                if (str(nodox), str(node1_z)) in RELACION:
                    print("Los nodos: x=",nodox, " y=",node_y, " z=", node1_z, "son transitivos")
                else:
                    isTransitivo = 0
                    print("Los nodos: x=",nodox, " y=",node_y, " z=", node1_z, "no son transitivos")
                        
    if isTransitivo:
        print("Los nodos son transitivos")
    else:
        print("Los nodos no llegan a ser transitivos")
        

    #DOMINIO
    dominio=[]
    for i in range(num_relaciones):
        dominio.append(RELACION[i][0]) #primer valor de los pares

    dominio = list(set(dominio))
    dominio.sort()
    print ("DOMINIO: ", dominio)

    #CODOMINIO
    codominio=[]
    for i in range(num_relaciones):
        codominio.append(RELACION[i][1]) #segundo valor de los pares

    codominio = list(set(codominio))
    codominio.sort()
    print ("CODOMINIO: ", codominio)


    #FUNCIÓN
    isFuncion = True;
    for i in range (0, len(RELACION)-1):
        for j in range (0, len(RELACION)-1):
            if (i != j) and (RELACION[i] == RELACION[j]):
                isFuncion = True
            else:
                for k in range (0, len(RELACION)):
                    if (k != i):
                        if len(RELACION[i]) == 1 or len(RELACION[k]) == 1:
                            isFuncion = False
                        elif (RELACION[i][0] == RELACION[k][0]) and (RELACION[i][1] == RELACION[k][1]):
                            isFuncion = True
                        elif RELACION[i][0] == RELACION[k][0]:
                            isFuncion = False

    if isFuncion == True:
        print("Los valores son una función")
    else:
        print("Los valores no son una función")