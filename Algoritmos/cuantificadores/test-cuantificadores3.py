#
# Cuantificadore simples y anidados.
#
# Test A: implementaciones mas basicas.
#
from cuantificadores3 import *

def test_A():
    #
    # cuantificadores simples
    def P(x): return x == 1
    assert ExisteX_A(P, [1,2,3]) == True
    assert ExisteX_A(P, [2,3,4]) == False
    #
    def P(x): return x > 0
    assert ParaTodoX_A(P, [1,2,3]) == True
    assert ParaTodoX_A(P, [0,1,2]) == False
    #
    # cuantificadores anidados
    def Q(x, y): return x > y
    #
    X = [4,5,6]
    Y = [1,2,3]
    assert ParaTodoX_ParaTodoY_A(Q, X, Y) == True
    Y = [1,2,9]
    assert ParaTodoX_ParaTodoY_A(Q, X, Y) == False
    Y = [10,20,3]
    assert ParaTodoX_ExisteY_A(Q, X, Y) == True
    Y = [7,8,9]
    assert ParaTodoX_ExisteY_A(Q, X, Y) == False
    #
    #
    X = [4,5,6]
    Y = [3,4,5]
    assert ExisteX_ParaTodoY_A(Q, X, Y) == True
    Y = [6,7,8]
    assert ExisteX_ParaTodoY_A(Q, X, Y) == False
    Y = [10,20,5]
    assert ExisteX_ExisteY_A(Q, X, Y) == True
    Y = [7,8,9]
    assert ExisteX_ExisteY_A(Q, X, Y) == False

if __name__== "__main__":
    test_A()
#end
