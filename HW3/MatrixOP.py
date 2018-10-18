def tranpose_matrix(m):
    row = len(m);
    col = len(m[0]);
    t = [];
    for i in range(col):
        t.append([m[j][i] for j in range(row)])
        
    return t;

def mul_matrix(a, b):
    row = len(a);
    mid = len(a[0]);
    if (mid != len(b)):
        return None;
    col = len(b[0]);
    r = [];
    for i in range(row):
        r.append([sum([a[i][k] * b[k][j] for k in range(mid)]) for j in range(col)])
    
    return r;

def add_matrix(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise Exception("row col not the same\n ({}, {}) != ({}, {})".format(len(a), len(a[0]), len(b), len(b[0])))
    c = []
    for i in range(len(a)):
        c.append(list(map(lambda x,y:x+y,a[i],b[i])))
    
    return c;

def sub_matrix(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise Exception("row col not the same\n ({}, {}) != ({}, {})".format(len(a), len(a[0]), len(b), len(b[0])))
    c = []
    for i in range(len(a)):
        c.append(list(map(lambda x,y:x-y,a[i],b[i])))
    
    return c;

def mul_matrix_scalar(s, m):
    if type(m) != list:
        raise Exception("type error : " + str(type(m)))

    r = [];
    for i in m:
        r.append([j*s for j in i])
    
    return r;

def add_matrix_scalar(s, m):
    if type(m) != list:
        raise Exception("type error : " + str(type(m)))
    
    r = [];
    for i in m:
        r.append([j+s for j in i])
    
    return r;
        
def unit_matrix(n):
    unit = [];
    for i in range(n):
        unit.append([1 if i == j else 0 for j in range(n)])
    return unit

def solve_X_by_LU(L, U, y):
    x = [0 for _ in range(len(y))];
    Ux = [];
    for i in range(len(y)):
        tmp = y[i]
        for j in range(i):
            tmp = tmp - Ux[j]*L[i][j]
        Ux.append(tmp)
    for i in reversed(range(len(Ux))):
        tmp = Ux[i]
        for j in range(len(Ux) - i - 1):
            j = j + i + 1
            tmp = tmp - x[j]*U[i][j] 
        x[i] = tmp / U[i][i]
        
    return x;
    
def inverse_matrix(m):
    row = len(m)
    col = len(m[0])
    if (row != col):
        return None;
    L = unit_matrix(row);
    U = [list(m[i]) for i in range(row)];
    for i in range(row):
        for j in range(col):
            if j >= i:
                continue;
            L[i][j] = U[i][j]/U[j][j];
            U[i] = list(map(lambda x,y:x - (L[i][j] * y) , U[i], U[j]))
    
    b = unit_matrix(row)
    inverse_m = [];
    for i in b:
        inverse_m.append(solve_X_by_LU(L, U, i))
    inverse_m = tranpose_matrix(inverse_m)
    return inverse_m;