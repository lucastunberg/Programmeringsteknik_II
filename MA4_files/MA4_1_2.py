
"""
Solutions to module 4
Review date:
"""

student = "Lucas Tunberg"
reviewer = ""

import math as m
import random as r
import functools as fts

# n is a list of set of coordinates
# d is the number of dimensions of the sphere 
     
def sphere_volume(n, d):
    counter = 0
    for _ in range(n):
        diff_points = tuple([r.uniform(-1, 1) for n in range(d)])
        if fts.reduce(lambda a, b: a + b, map(lambda a: a**2, diff_points)) <= 1:
            counter += 1
    volume = pow(2,d)*counter/n
    return volume

def hypersphere_exact(n,d):
    return m.pow(m.pi,d/2)*m.pow(1,d)/m.gamma(d/2+1)


def main():
    n = 100000
    d = 2
    sphere_volume(n,d)
    n = 100000
    d = 11
    sphere_volume(n,d)
    
    
if __name__ == '__main__':
	main()
