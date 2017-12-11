def suma_i (n):
    """
    Suma de Gauss hasta el entero n, version iterativa.
    """
    z = 0
    for i in range (n+1):
        z = z + i
    return z

def suma_r (n):
    """
    Suma de Gauss hasta el entero n, version recursiva.
    """
    if (n == 1):
        z = 1
    else:
        z = n + suma_r (n-1)
    return z

def maximo_i (A):
    """
    Encuentra el primer elemento maximo de la lista A,
    version iterativa.
    Entra:   lista A
    Retorna: el primer elemento maximo z de la lista A.
    """
    # basta hacer una unica pasada   
    vmax = A [0]      # toma el 1er valor
    for x in A [1:]:  # recorre desde el 2do valor hasta el final
        if (x > vmax):
            vmax = x
    # define el valor de retorno (escalar)
    return vmax
        
def maximo_r (A):
    """
    Encuentra el primer elemento maximo de la lista A,
    version recursiva.
    Entra:   lista A
    Retorna: el primer elemento maximo z de la lista A.
    """
    n = len (A) 
    if   (n == 1):
        z = A [0]
    else:
        b = maximo_r (A[0:n-1])       # llamada recursiva
        z = maxde2valores (b, A[n-1]) # obtiene el max entre 2 valores 
    return z

def maxde2valores (a,b):
    """
    Auxiliar de la funcion "maximo_r":
    retorna el max entre 2 valores.
    """
    if (a >= b):
        return a
    else:
        return b

def a_n21 (n):
    """
    Rosen, 5ta edicion, E21, pag. 264.
    Calculo del termino enesimo de la sucesion
    a_0 = 1, a_1 = 1, y a_n = a_{n-1} a_{n-2}, 
    para n = 2, 3, 4, ..., version recursiva.
    """
    if   (n == 0):
        z = 1
    elif (n == 1):
        z = 2
    else:   
        z = a_n21 (n-1) * a_n21 (n-2)
    return z

def a_n24 (n):
    """
    Rosen, 5ta edicion, E24, pag. 264.
    Calculo del termino enesimo de la sucesion
    a_0 = 1, a_1 = 2, a_2 = 3, y 
    a_n = a_{n-1} + a_{n-2} + a_{n-3}, 
    para n = 3, 4, 5, ..., version recursiva.
    """
    if   (n == 0):
        z = 1
    elif (n == 1):
        z = 2
    elif (n == 2):
        z = 3
    else:   
        z = a_n24 (n-1) + a_n24 (n-2) + a_n24 (n-3)
    return z

def factorial_i (n):
    """
    Calculo del factorial del entero no-negativo n, 
    version iterativa.
    """
    z = 1
    for  i in range (1,n):
        z = z * i
    return z
    
def factorial_r (n):
    """
    Calculo del factorial del entero no-negativo n, 
    version recursiva.
    """
    if  (n == 0):
        z = 1
    else:
        z = n * factorial_r (n-1)
    return z

def potencia_i (a, n):
    """
    Calculo de la potencia a^n,
    version iterativa.
    """
    assert n >= 0   # se puede omitir
    r = 1
    for i in range (n):
        r = r * a
    return r

def potencia_r (a, n):
    """
    Calculo de la potencia a^n,
    version recursiva.
    """
    assert n >= 0  # se puede omitir
    if  (n == 0):
        z = 1
    else:
        z = a * potencia_r (a, n-1)
    return z

def mcd_i (a, b):
    """
    Maximo Comun Divisor de los enteros a y b, 
    version iterativa
    """
    # control
    assert a >= 0   # se puede omitir
    assert b >= 0   # se puede omitir
    if (a > b):     # intercambio para tener a < b
        t = a
        a = b
        b = t
    #
    (x, y) = (a, b) # copia
    print (x,y)
    while (y != 0):
        r = x % y
        (x, y) = (y, r)
        print (x,y)
    return x

def mcd_r (a, b):
    """
    Maximo Comun Divisor de los enteros a y b, 
    version recursiva
    """
    # control
    assert a >= 0   # se puede omitir
    assert b >= 0   # se puede omitir
    if (a > b):     # intercambio para tener a < b
        t = a
        a = b
        b = t
    #
    if (a == 0):  
       z = b
    else:
       z = mcd_r (b % a, a)
    return z

# begin some tests
def test01 ():
    n = 100
    z = suma_i (n)
    print ('La suma 1 + 2 + ... + n, con n = ', n)
    print ('es igual a ', z, ' (version iterativa) \n')
    return

def test02 ():
    n = 100
    z = suma_r (n)
    print ('La suma 1 + 2 + ... + n, con n = ', n)
    print ('es igual a ', z, ' (version recursiva) \n')
    return

def test03 ():
    A = [ 1, 0, 3, 8, 5, 6, 7, 4, 9, 2 ]
    z = maximo_i (A)
    print ('El maximo de la lista A = ', A)
    print ('es igual a ',  z, ' (version iterativa) \n')
    return

def test04 ():
    A = [ 1, 0, 3, 8, 5, 6, 7, 4, 9, 2 ]
    z = maximo_r (A)
    print ('El maximo de la lista A = ', A)
    print ('es igual a ',  z, ' (version recursiva) \n')
    return

def test05 ():
    a = 48
    b = 12
    z = mcd_i (a,b)
    print ('El mcd de ', a, ' y de ', b)
    print ('es igual a ', z, ' (version iterativa) \n' )
    return

def test06 ():
    a = 48
    b = 12
    z = mcd_r (a,b)
    print ('El mcd de ', a, ' y de ', b)
    print ('es igual a ',  z, ' (version recursiva) \n' )
    return

def test07 ():    
    n = 789
    z = factorial_i (n)
    print ('El factorial de ', n)
    print ('es igual a ', z , ' (version iterativa) \n' )
    return

def test08 ():    
    n = 789
    z = factorial_r (n)
    print ('El factorial de ', n)
    print ('es igual a ', z, ' (version recursiva) \n' )
    return

def test09 ():
    n = 12
    z = a_n21 (n)
    print ('Rosen, 5ta edicion, E21, pag. 264.        ')
    print ('Calculo del termino enesimo de la sucesion')
    print ('a_0 = 1, a_1 = 1, y a_n = a_{n-1} a_{n-2},')
    print ('para n = 2, 3, 4, ..., version recursiva. ')
    print ('Cuando n = ', n, ' es a_n = ', z, '\n')
    return

def test10 ():    
    n = 17
    z = a_n24 (n)
    print ('Rosen, 5ta edicion, E24, pag. 264.        ')
    print ('Calculo del termino enesimo de la sucesion')
    print ('a_0 = 1, a_1 = 2, a_2 = 3, y              ')
    print ('a_n = a_{n-1} + a_{n-2} + a_{n-3}         ')
    print ('para n = 3, 4, 5, ..., version recursiva. ')
    print ('Cuando n = ', n, ' es a_n = ', z, '\n')
    return

if __name__== "__main__":
     test01 ()
     test02 ()
     test03 ()
     test04 ()
     test05 ()
     test06 ()
     test07 ()
     test08 ()
     test09 ()
     test10 ()
#end
