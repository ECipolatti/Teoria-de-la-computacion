#
# Ejemplos de operaciones simples con matrices booleanas,
# en Python 3.x
#
# Receta basica (usando idle3):
# 1) En idle3 open this file.
# 2) Run Module (F5) of this file.
# 3) Eventualmente en la ventana interactiva ejecutar comandos.
#
from bitmat import bitmat

def test_bitmat():
    A = bitmat([[1,0,0],
                [0,1,0],
                [0,0,1]])

    B = bitmat(3)
    B[0,2] = B[1,1] = B[2,0] = 1

    assert A==A
    assert B==B
    assert A!=B

    print (bitmat(A)); print()
    print (B); print

    print (~A); print()
    print (~B); print()


    C1 = A | B
    print (C1); print()

    C2 = A & B
    print (C2); print()

    C3 = A * B
    print (C3); print()

if __name__ == '__main__':
    test_bitmat()

# end
