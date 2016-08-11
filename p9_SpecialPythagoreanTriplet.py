# -*- coding: utf-8 -*-
#~ Special Pythagorean triplet
#~ Problem 9
#~ A Pythagorean triplet is a set of three natural numbers, 
#~ a < b < c, for which,
#~ 
#~ a^2 + b^2 = c^2
#~ For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#~ 
#~ There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#~ Find the product abc.
from math import sqrt

n = 1000
for a in xrange(1,n):
    for b in xrange(1,n):
        c = sqrt(a**2 + b**2)
        if (c).is_integer() and (a+b+c)==1000:
            print a*b*c
