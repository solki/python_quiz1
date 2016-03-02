# Generates a list of 10 random numbers between 0 and 19 included,
# and determines the length of the longest strictly increasing sequence and
# the smallest most frequent element in the list.
#
# Writtten by *** and Eric Martin for COMP9021


import sys
from random import seed, randint


nb_of_elements = 10

try:
     seed(input('Enter an integer: '))
except TypeError:
    print('Incorrect input, giving up.')
    sys.exit()

L = []
for _ in range(nb_of_elements):
    L.append(randint(0, 20))
print('The generated list is:', L)

length_of_longest_increasing_sequence = 1
current_length = 1

smallest_most_frequent = None
largest_count = 0

# REPLACE THIS COMMENT WITH YOUR CODE

print('The length of the longest strictly increasing sequence is: {}'.format(
                                        length_of_longest_increasing_sequence))
print('The smallest most frequent element in the sequence is: {}'.format(
                                                       smallest_most_frequent))
                
    


    
    
