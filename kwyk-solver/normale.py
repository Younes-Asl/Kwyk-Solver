import scipy.stats


# Module d'aproximation d'une répartition, normale d'espérance u
# et d'écart type o (donc la racine de la variance).
class Normale(object):
    def __init__(self, u, o):
        self.norm = scipy.stats.norm(u, o)

    def p_X_inf(self, a):
        return self.norm.cdf(a)

    def p_X_sup(self, a):
        return 1 - self.p_X_inf(a)  # return norm.sf(a)

    def p_X_btw(self, a, b):
        if a > b:
            # si dans le mauvais sens, on les retourne
            return self.p_X_btw(b, a)
        if a == b:
            return 0.0
        return 1 - self.p_X_inf(a) - self.p_X_sup(b)


# EXEMPLE D'UTILISATION
"""
(u, o) = (0, 2)  # esperance et ecart type de la loi normale N(u,o²)
(a, b) = (-4, 4) #

centreeReduite = Normale(u,o)
p = centreeReduite.p_X_inf(a)    #P(X<a)
p = centreeReduite.p_X_sup(b)    #P(X>b)
p = centreeReduite.p_X_btw(a,b)  #P(a<X<b) ou P(b<X<a)
print(p)
"""
