# SciPy is a scientific computation library that uses NumPy underneath.
# scientific python
from scipy import constants
# How many cubic meters are in one liter:
print(constants.liter)
print(constants.pi)
# list of all constatnt units
print(dir(constants))
# it have a)metric si prefixe like yotta,zotta 
#         b)binary prefix(units in bytes)
#         c)mass related 
#         d)angles related,
#         e)time
#         f)length
#         g)Pressures
#         h)Area
#         i)Volumes
#         j)Speed,Temprature,Energy,Power,Force etc
print(constants.minute)
# It provides more utility functions for optimization, stats and signal processing.
import scipy
print(scipy.__version__)
# NumPy is capable of finding roots for polynomials and linear equations, but it can not find roots for non linear equations, like this one:
# x + cos(x)
# it can be solved using scipy
from scipy.optimize import root
from math import cos

def eqn(x):  #fun=function representing an eqn, x0==>initial guess
    return x+cos(x)

myroot=root(eqn,0)
print(myroot.x)
print()
print(myroot)
# Minimizing a Function

# A function, in this context, represents a curve, curves have high points and low points.
# High points are called maxima.
# Low points are called minima.
# The highest point in the whole curve is called global maxima, whereas the rest of them are called local maxima.
# The lowest point in whole curve is called global minima, whereas the rest of them are called local minima.
# Minimize the function x^2 + x + 2 with BFGS:
print("////////////////////////////////////////")
from scipy.optimize import minimize
def eqn1(x):
    return x**2+x+2
mymin=minimize(eqn1,0,method='BFGS')  #0 is the initial guess
# instead of impoting we can use scipy.optimize.minimize to minimize the function
print(mymin)
# method - name of the method to use. Legal values:
#     'CG'
#     'BFGS'
#     'Newton-CG'
#     'L-BFGS-B'
#     'TNC'
#     'COBYLA'
#     'SLSQP'
# callback - function called after each iteration of optimization.
# options - a dictionary defining extra params:
# {
#      "disp": boolean - print detailed description
#      "gtol": number - the tolerance of the error
#   }