def sucesiones():
    print("Muy bien empecemos con las suceciones!")
    print("Escribe la formula que quieres trabajar en terminos de k.")

    formula = input("Fórmula(k): ")
    m = int(input("Limite inferior: "))
    n = int(input("Limite superior: "))
    print("")

    suma = 0
    mult = 1

    print("Desarrollo de la sucesión de m a n:")

    for i in range(m, n+1):
        k = i
        print("k", i, " = ", round(eval(formula), 5), sep='')
        suma += eval(formula)
        mult *= eval(formula)

    print("Suma de elementos:", suma)
    print("Multiplicación total:", mult)
