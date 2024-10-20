
"""
Solutions to module 4
Review date:
"""

student = "Lucas Tunberg"
reviewer = ""

import functools as fts
import math as m
import random as r
import concurrent.futures as future
import time

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


# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
    #using multiprocessor to perform 10 iterations of volume function  
    with future.ProcessPoolExecutor() as ex:
        futures = ex.map(sphere_volume, [n]*np, [d]*np)
    res = sum(futures)/np
    return res

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    with future.ProcessPoolExecutor() as ex:
        futures = ex.map(sphere_volume, [int(n/np)]*np, [d]*np)
    res = sum(futures)/np
    return res

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    np = 10
    
    start = time.perf_counter()
    for y in range (10):
        sphere_volume(n,d)
    end = time.perf_counter()
    print(f'Time for calculating without parallelization: {end-start}')

    start_parallelization = time.perf_counter()
    sphere_volume_parallel1(n,d,np)
    end_parallelization = time.perf_counter()
    print(f'Time for calculating with parallelization: {end_parallelization-start_parallelization}')

    start_parallelization_2 = time.perf_counter()
    sphere_volume_parallel2(n,d,np)
    end_parallelization_2 = time.perf_counter()
    print(f'Time for calculating with parallelization 2: {end_parallelization_2-start_parallelization_2}')
    print(sphere_volume(n,2))
    print(sphere_volume_parallel1(n,2,10))
    print(sphere_volume_parallel2(n,2,10))
if __name__ == '__main__':
	main()
