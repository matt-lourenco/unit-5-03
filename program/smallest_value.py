# Created on 10 Nov 2016
# Created by: Matthew Lourenco
# This is a program that finds the smallest value in an array.

from numpy import random

def find_smallest(array):
    
    smallest_value = array[0]
    for value in array:
        if smallest_value > value:
            smallest_value = value
    
    return smallest_value

my_array = []
for random_generation in range(0, random.randint(1, 11)):
    my_array.append(random.randint(1, 26))
print(my_array)
print(find_smallest(my_array))
