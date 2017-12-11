from bitmat import bitmat

def es_reflexiva (A):
    n = len(A)
    for i in range (n):
        if not A[i,i]:
            return False
    return True

def es_simetrica_vainilla (A):
    n = len (A)
    for i in range (n):
        for j in range (n):
            if (A[i,j] and not A[j,i]):
                return False
    return True
   
def es_simetrica(A):
    n = len (A)
    for i in range (n):
        for j in range (i+1,n):
            if (A[i,j] and not A[j,i]):
                return False
            if (A[j,i] and not A[i,j]):
                return False
    return True

def es_antisimetrica (A):
    n = len (A)
    for i in range (n):
        for j in range (i+1,n):
            if (A[i,j] and A[j,i]):
                return False
    return True

def es_transitiva (A):
    n = len (A)
    for k in range (n):
        for i in range (n):
            for j in range (n):
                if ((A[i,k] and A[k,j]) and not A[i,j]):
                    return False
    return True

def es_relacion_de_equivalencia (A):
    return (es_reflexiva (A) and
            es_simetrica (A) and
            es_transitiva(A))

def es_relacion_de_orden (A):
    return (es_reflexiva    (A) and
            es_antisimetrica(A) and
            es_transitiva   (A))

# end
