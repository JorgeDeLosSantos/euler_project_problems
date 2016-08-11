# -*- coding: utf-8 -*-
#~ Sum square difference
#~ Problem 6
#~ The sum of the squares of the first ten natural numbers is,
#~ 
#~ 1^2 + 2^2 + ... + 10^2 = 385
#~ 
#~ The square of the sum of the first ten natural numbers is,
#~ 
#~ (1 + 2 + ... + 10)^2 = 55^2 = 3025
#~ 
#~ Hence the difference between the sum of the squares of the first 
#~ ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#~ 
#~ Find the difference between the sum of the squares of the first 
#~ one hundred natural numbers and the square of the sum.


def sum_of_squares(N):
    x = range(1,N+1)
    xs = [k**2 for k in x]
    ssq = sum(xs)
    return ssq

def square_of_sum(N):
    x = range(1,N+1)
    sx = sum(x)
    sxsq = sx**2
    return sxsq

N = 100
print square_of_sum(N)-sum_of_squares(N)
