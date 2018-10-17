def polynomial_basis(x, n):
    return x**n;

class polynomial_equation():
    def __init__(self, w_v):
        if type(w_v[0]) != list:
            self.w_vector = [[w] for w in w_v]
        else:
            self.w_vector = w_v
        self.f = lambda x:sum([basis(x, i)*self.w_vector[i][0] for i in range(len(self.w_vector))]);
    
    def __str__(self):
        r = "$$"
        r = r + "y = "
        for n in reversed(range(len(self.w_vector))):
            w = self.w_vector[n][0]
            if (w == 0):
                continue;
            
            r = r + '{:+.2f}'.format(w)
            if (n != 0):
                r = r + 'x^{}'.format(n)
        r = r + "$$"
        return r;
    
    def rLSE(self, x, y, Lambda=1.0):
        loss = 0;
        for i in range(len(x)):
            loss = loss + (self.f(x[i]) - y[i])**2
        for i in range(len(self.w_vector)):
            loss = loss + Lambda*self.w_vector[i][0]**2
        return loss;

basis = polynomial_basis;