def esprimo (n):
    """ Devuelve True si el entero n es primo sino False. """
    # caso n < 2
    if (n < 2):
        return False
    # caso n > 2, lazo principal
    r = int (math.floor (math.sqrt (n)))
    for d in range (2,r+1):
        h = n % d
        if (h == 0):
            return False
    return True

def test01 ():
    n = 100
    A = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ]
    for n in A:
        b = esprimo (n)
        print ('es primo el numero ', n, "? : ", b)
    return

if __name__== "__main__":
     import math
     test01 ()
#end

