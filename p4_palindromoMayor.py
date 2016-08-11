# -*- coding: utf-8 -*-
#~ Largest palindrome product
#~ Problem 4
#~ A palindromic number reads the same both ways. The largest palindrome 
#~ made from the product of two 2-digit numbers is 9009 = 91 × 99.
#~ 
#~ Find the largest palindrome made from the product of two 3-digit numbers.
#~ 
def espalindromo(num):
    cad=str(num)
    if cad==cad[-1::-1]:
        return True
    else:
        return False

for i in range(900,1000):
    for j in range(900,1000):
        if espalindromo(i*j):
            print i,j
            print i*j

