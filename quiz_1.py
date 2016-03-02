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

LS = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, nb_of_elements):
    tmp_length = []
    for j in range(0, i):
        if L[i] > L[j]:
            tmp_length.append(LS[i] + LS[j])

    if tmp_length:
        LS[i] = max(tmp_length)

length_of_longest_increasing_sequence = max(LS)

for element in list(set(L)):
    if smallest_most_frequent is None:
        smallest_most_frequent = element
        largest_count = L.count(element)
        next

    if (L.count(element) > largest_count) or (L.count(element) == largest_count and element < smallest_most_frequent):
        smallest_most_frequent = element
        largest_count = L.count(element)

print('The length of the longest strictly increasing sequence is: {}'.format(
    length_of_longest_increasing_sequence))
print('The smallest most frequent element in the sequence is: {}'.format(
    smallest_most_frequent))
