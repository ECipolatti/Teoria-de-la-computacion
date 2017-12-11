# -----
# Implementaciones mas basicas:
def ExisteX(P, X):
    for x in X:
        if P(x):
            return True
    return False

def ParaTodoX(P, X):
    for x in X:
        if not P(x):
            return False
    return True

def ParaTodoX_ParaTodoY(P, X, Y):
    for x in X:
        for y in Y:
            if not P(x, y):
                return False
    return True

def ParaTodoX_ExisteY(P, X, Y):
    for x in X:
        existe_y = False
        for y in Y:
            if P(x, y):
                existe_y = True
                break
        if not existe_y:
            return False
    return True

def ExisteX_ParaTodoY(P, X, Y):
    for x in X:
        paratodo_y = True
        for y in Y:
            if not P(x, y):
                paratodo_y = False
                break
        if paratodo_y:
            return True
    return False

def ExisteX_ExisteY(P, X, Y):
    for x in X:
        for y in Y:
            if P(x, y):
                return True
    return False

# -----
# Implementaciones menos basicas:
def ExisteX_B(P, X):
    return any(P(x) for x in X)

def ParaTodoX_B(P, X):
    return all(P(x) for x in X)

def ParaTodoX_ParaTodoY_B(P, X, Y):
    return all(P(x, y) for x in X for y in Y)

def ParaTodoX_ExisteY_B(P, X, Y):
    for x in X:
        if not any(P(x, y) for y in Y):
            return False
    return True

def ExisteX_ParaTodoY_B(P, X, Y):
    for x in X:
        if all(P(x, y) for y in Y):
            return True
    return False

def ExisteX_ExisteY_B(P, X, Y):
    return any(P(x, y) for x in X for y in Y)

# -----
