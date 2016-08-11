# -*- coding: utf-8 -*-
#~ 10001st prime
#~ Problem 7
#~ By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we 
#~ can see that the 6th prime is 13.
#~ 
#~ What is the 10 001st prime number?
import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

limit = int(1e6) 
goal = 10001
np = 0
for k in xrange(2,limit):
    if is_prime(k):
        np += 1
    if np==goal:
        print np, k
        break
