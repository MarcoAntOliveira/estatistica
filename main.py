import numpy as np
import matplotlib.pyplot as plt


def valor_esperado(X, Px):
    valor_esperado = 0
    for i in range(len(X)):
        valor_esperado += X[i] * Px
    return valor_esperado
    
def variancia(X, Px):
    # Chamamos a função 'valor_esperado' e guardamos o resultado em 'mu'
    mu = valor_esperado(X, Px) 
    
    var = 0
    for i in range(len(X)):
        var += ((X[i] - mu) ** 2) * Px
    return var


Z = [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6],
     [2,1], [2,2], [2,3], [2,4], [2,5], [2,6],
     [3,1], [3,2], [3,3], [3,4], [3,5], [3,6],
     [4,1], [4,2], [4,3], [4,4], [4,5], [4,6],
     [5,1], [5,2], [5,3], [5,4], [5,5], [5,6],
     [6,1], [6,2], [6,3], [6,4], [6,5], [6,6]]

X = np.array([1, 2, 3, 4, 5, 6])

Px = 1/6
Py = Px
Y = X + 2


print("Valor esperado de X:", valor_esperado(X, Px))
print("Variância de X:", variancia(X, Px))
print("Valor esperado de Y:", valor_esperado(Y, Py))
print("Variância de Y:", variancia(Y, Py))

# Criando a matriz X (36 lançamentos, cada um com 2 elementos)
# Usamos o np.indices para gerar as combinações de 1 a 6 rapidamente
# d1, d2 = np.mgrid[1:7, 1:7]
# X = np.stack((d1, d2), axis=-1)

# Aplicando a operação Y = X + 2

print("Primeira linha de Y:")
print(Y[0])

