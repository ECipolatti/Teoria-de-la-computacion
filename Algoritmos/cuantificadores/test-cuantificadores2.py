from cuantificadores2 import *

def test1():
    #
    def P(x): return x == 1
    assert ExisteX(P, [1,2,3]) == True
    assert ExisteX(P, [2,3,4]) == False
    #
    def P(x): return x > 0
    assert ParaTodoX(P, [1,2,3]) == True
    assert ParaTodoX(P, [0,1,2]) == False

def test2():
    def P(x, y): return x > y
    #
    X = [4,5,6]
    Y = [1,2,3]
    assert ParaTodoX_ParaTodoY(P, X, Y) == True
    Y = [1,2,9]
    assert ParaTodoX_ParaTodoY(P, X, Y) == False
    Y = [10,20,3]
    assert ParaTodoX_ExisteY(P, X, Y) == True
    Y = [7,8,9]
    assert ParaTodoX_ExisteY(P, X, Y) == False
    #
    #
    X = [4,5,6]
    Y = [3,4,5]
    assert ExisteX_ParaTodoY(P, X, Y) == True
    Y = [6,7,8]
    assert ExisteX_ParaTodoY(P, X, Y) == False
    Y = [10,20,5]
    assert ExisteX_ExisteY(P, X, Y) == True
    Y = [7,8,9]
    assert ExisteX_ExisteY(P, X, Y) == False

def test3():
    def P(x, y): return x > y
    #
    X = [4,5,6]
    Y = [1,2,3]
    assert ParaTodoX_ParaTodoY_B(P, X, Y) == True
    Y = [1,2,9]
    assert ParaTodoX_ParaTodoY_B(P, X, Y) == False
    Y = [10,20,3]
    assert ParaTodoX_ExisteY_B(P, X, Y) == True
    Y = [7,8,9]
    assert ParaTodoX_ExisteY_B(P, X, Y) == False
    #
    #
    X = [4,5,6]
    Y = [3,4,5]
    assert ExisteX_ParaTodoY_B(P, X, Y) == True
    Y = [6,7,8]
    assert ExisteX_ParaTodoY_B(P, X, Y) == False
    Y = [10,20,5]
    assert ExisteX_ExisteY_B(P, X, Y) == True
    Y = [7,8,9]
    assert ExisteX_ExisteY_B(P, X, Y) == False

if __name__== "__main__":
    test1()
    test2()
    test3()

