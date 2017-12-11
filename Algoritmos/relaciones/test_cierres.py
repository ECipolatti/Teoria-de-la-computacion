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

import cierres

def test_cierrereflexivo (A, C):
    R = cierres.cierre_reflexivo (A)
    assert  R == C

def test_cierresimetrico (A, C):
    R = cierres.cierre_simetrico (A)
    assert  R == C

def test_cierretransitivo (M, C=None):
    C1 = cierres.cierre_transitivo (M)
    C2 = cierres.roywarshall (M)
    if C is None:
        assert C1 == C2
    else:
        assert  C == C1
        assert  C == C2

if __name__ == '__main__':
    #
    M = bitmat([[1,0,1],
                [0,0,0],
                [1,0,0]])
    C = bitmat([[1,0,1],
                [0,1,0],
                [1,0,1]])
    test_cierrereflexivo (M, C)
    #
    M = bitmat([[1,1,0,1],
                [1,0,1,0],
                [0,0,0,0],
                [0,0,1,0]])
    C = bitmat([[1,1,0,1],
                [1,0,1,0],
                [0,1,0,1],
                [1,0,1,0]])
    test_cierresimetrico (M, C)
    #
    M = bitmat([[1,0,1],
                [0,1,0],
                [1,1,0]])
    C = bitmat([[1,1,1],
                [0,1,0],
                [1,1,1]])
    test_cierretransitivo (M, C)
    #
    M = bitmat([[0,0,0,1],
                [1,0,1,0],
                [1,0,0,1],
                [0,0,1,0]])
    C = bitmat([[1,0,1,1],
                [1,0,1,1],
                [1,0,1,1],
                [1,0,1,1]])
    test_cierretransitivo (M, C)

# end
