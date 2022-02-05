import numpy as np
def moltiplicazione(x, y):
    assert isinstance(y, np.ndarray)
    assert isinstance(x, np.ndarray)
    return np.matmul(x,y)
if __name__=='__main__':
    a = np.random.rand(3,2)
    b = np.random.rand(2,3)
    print('la matrice a: \n', a)
    print('la matrice b: \n', b)
    print('Il prodotto tra le matrici: \n', moltiplicazione(a,b))
