
"""
Solutions to module 4
Review date:
"""

student = "Lucas Tunberg"
reviewer = ""


import random as r
import matplotlib.pyplot as plt 
import math

def approximate_pi(i):
    points_x = []
    points_y = []
    outside_points_x = []
    outside_points_y = [] 
    numbers_inside = 0
    for x in range(i):
        point_y = r.uniform(-1,1)
        point_x = r.uniform(-1,1)
        if (point_x**2+point_y**2) <= 1:
             numbers_inside += 1
             points_y.append(point_y)
             points_x.append(point_x)
        else:
            outside_points_y.append(point_y)
            outside_points_x.append(point_x)
    pi_approx = numbers_inside*4/i
    print(f'Approximation of pi: {pi_approx}')
    print(f'Points inside the circle: {numbers_inside}')
    approximate_pi.outside_x = outside_points_x
    approximate_pi.outside_y = outside_points_y
    approximate_pi.inside_x = points_x
    approximate_pi.inside_y = points_y
    return(pi_approx)
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximation_of_pi = approximate_pi(n)
        plt.plot(approximate_pi.outside_x, approximate_pi.outside_y,'o',color = 'm')
        plt.plot(approximate_pi.inside_x, approximate_pi.inside_y,'o',color = 'c')
        plt.title('Monte carlo simulation')
        plt.grid(True)
        plt.show()

    print(f'Real value of pi: {math.pi}')
    


if __name__ == '__main__':
    main()
