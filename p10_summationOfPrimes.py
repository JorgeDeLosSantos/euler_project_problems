# -*- coding: utf-8 -*-
#~ Summation of primes
#~ Problem 10
#~ The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#~ 
#~ Find the sum of all the primes below two million.
import math
from tqdm import tqdm

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

limit = int(2e6)
psum = 0
for k in tqdm(xrange(2,limit)):
    if is_prime(k):
        psum += k

print psum
