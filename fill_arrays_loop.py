from numpy import sqrt ,exp, pi
from matplotlib.pyplot import plot, show, xlabel, ylabel, linspace, zeros



def h(x):
    return 1 / sqrt(2 * pi) * exp(-0.5 * x * x)


xlist = linspace(-4, 4, 41)
hlist = zeros(len(xlist))

for i in range(len(xlist)):
    hlist[i] = h(xlist[i])

plot(xlist, hlist)
xlabel('x')
ylabel('h')
show()