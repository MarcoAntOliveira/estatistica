# -*- coding: utf-8 -*: mia
from math import factorial, e, sqrt
from  sympy import integrate

poisson = lambda x, lamb, T: ((e**-lamb*T)*(lamb*T)**x)/factorial(x)
 


def valor_esperado(X, Px):
    valor_esperado = 0
    for i in range(len(X)):
        valor_esperado += X[i] * Px
        print(f"Valor esperado parcial para X[{i}] = {X[i]}: {X[i] * Px}")
    return valor_esperado
    
def variancia(X, Px):
    # Chamamos a função 'valor_esperado' e guardamos o resultado em 'mu'
    mu = valor_esperado(X, Px) 
    
    var = 0
    for i in range(len(X)):
        var += ((X[i] - mu) ** 2) * Px
        print(f"Variância parcial para X[{i}] = {X[i]}: {((X[i] - mu) ** 2) * Px}")
        
    return var

#variaveis aleatorias discretas
def perm_rep (x , n):
    return (factorial(n)/(factorial(n-x)*factorial(x)))

def function_density(f , *args, intervalo):
    x = integrate(f(*args), intervalo)
    return x

def dist_bin(x , n, p):
    return perm_rep(x, n)*(p**x)*((1-p)**(n-x))

def med_dis_bin(n, p):
    return n*p

def var_dist_bin(n, p):
    return n*p*(1 - p)

def desv_dist_bin(n, p):
    return sqrt(n*p*(1 - p))
"""
def dist_hip(x, n, M, N ):
    return (perm_rep(M, x)*perm_rep((N - M) , (n - x)))/perm_rep(N, n)
"""
#Estimação de parametros
def des_pad_main (desv_pad, n):
    return desv_pad/sqrt(n)

print(dist_bin(3, 6, 0.5))
#print(dist_hip(2, 5, 12,20))
w = 0
for i  in range (0, 5):
   w = w + dist_bin(i, 25, 0.05)
   
print (w)
"""
print(dist_bin(2, 5, 0.4))
w = 0
for i in range (0, 4):
    w = w + dist_bin(i, 5, 0.4)

print(w)
 
w = 1 - w
print(w) 
"""  