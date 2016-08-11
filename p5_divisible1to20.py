# -*- coding: utf-8 -*-
#~ Smallest multiple
#~ Problem 5
#~ 2520 is the smallest number that can be divided by each of the 
#~ numbers from 1 to 10 without any remainder.
#~ 
#~ What is the smallest positive number that is evenly divisible 
#~ by all of the numbers from 1 to 20?
from numpy import array
from tqdm import tqdm

A = array(range(1,10))
limit = int(1e8) # pseudo-limit
for k in tqdm(xrange(1,limit)):
    if not(any(k%A)) or k > limit:
        print "Finded: ", k
        break

#~ print k

