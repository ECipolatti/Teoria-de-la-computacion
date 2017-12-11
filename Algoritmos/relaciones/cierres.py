#
# Ejemplos de cierres de relaciones,
# en Python 3.x
#
# Receta basica (usando idle3):
# 1) En idle3 open this file.
# 2) Run Module (F5) of this file.
# 3) Eventualmente en la ventana interactiva ejecutar comandos.
#
from bitmat import bitmat

def cierre_reflexivo(M):
    A = bitmat (M)
    n = len (A)
    for i in range(n):
        A [i,i] = True
    return A

def cierre_simetrico(M):
    A = bitmat(M)
    n = len (A)
    for i in range (n):
        for j in range (i+1, n):
            if   (A[i,j]):
                  A[j,i] = 1
            elif (A[j,i]):
                  A[i,j] = 1
    return A

def cierre_simetrico_vainilla1 (M):
    A = bitmat (M)
    n = len (A)
    for i in range (n):
        for j in range (n):
            if (A[i,j]): A[j,i] = 1

def cierre_simetrico_vainilla2 (M):
    A = bitmat (M)
    n = len (A)
    for i in range (n):
        for j in range (i+1, n):
            value = (A[i,j] or A[j,i])
            A [i,j] = A[j,i] = value
    return A

def cierre_transitivo (M):
    A = bitmat (M)
    B = A
    n = len(A)
    for i in range(1, n):
        A = A * M  # producto matricial booleano
        B = B | A  # suma   o matricial booleana
    return B
    
def roywarshall (M):
    W = bitmat (M)
    n = len (W)
    for k in range (n):
        for i in range (n):
            for j in range (n):
                W[i,j] = W[i,j] or (W[i,k] and W[k,j])
    return W

# end 
