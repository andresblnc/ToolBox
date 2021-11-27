def Reflexividad(R, A):
    for a in A:
        if (a, a) not in R:
            return False
    return True
def Simetria(R):
    for a in R:
        for b in R:
            if (b, a) not in R:
                return False
    return True

def Transitividad(R, A):
    for a in A:
        for b in A:
            if (a, b) in R:
                for c in A:
                    if (b, c) in R and (a, c) not in R:
                        return False
    return True


def relaciones():
    print("Perfecto, has escogido las relaciones!")
    num = int(input("Escriba el número de parejas que desea evaluar:  "))
    print(num)
