from numpy import *
from numpy import sqrt,pi,exp

def h(x):
    return 1 / sqrt(2 * pi) * exp(-0.5 * x * x)




n = 4
dx = 1.0/(n-1)


xlist =[i*dx for i in range(n)]
ylist =[h(x) for x in xlist]
arr = linspace(-4,int(n),41)

print(arr)