# Created on 10 Nov 2016
# Created by: Matthew Lourenco
# This is a program that finds the smallest value in an array.

def find_smallest(array):
    
    smallest_value = array[0]
    for value in array:
        if smallest_value > value:
            smallest_value = value
    
    return smallest_value

my_array = [13, 17, 5 , 23, 9]
print(find_smallest(my_array))
