# - - - #

# [This program regards The Collatz conjecture, also known as the 3n+1 conjecture]      #
#                                                                                       #
# A small program to represent the Hailstone sequence of a given integer using a graph  #
# It also calculates the total stopping time of a given positive integer                #

import matplotlib.pyplot as plt

# naming the X axis
plt.xlabel('x - axis')
# naming the Y axis
plt.ylabel('y - axis')

# titling the graph
plt.title('Hailstone Sequence')

# get input from user
num = input("\nplease enter a positive integer:\n\t")

# verify that the input was a positive integer
try:
    num = int(num)
    if num <= 0:  # input wasn't a positive integer
        print("\nwrong input - input must be a positive integer")
        exit()
except ValueError:  # input wasn't an integer
    print("\nwrong input - input must be an integer")
    exit()

print_hailstone_sequence = input("\nprint hailstone sequence numbers to console? (yes / y / no / n)\n\t")

if print_hailstone_sequence.lower() == "yes" or print_hailstone_sequence.lower() == "y":
    print_hailstone_sequence = True  # print hailstone sequence numbers to console
elif print_hailstone_sequence.lower() == "no" or print_hailstone_sequence.lower() == "n":
    print_hailstone_sequence = False  # don't print hailstone sequence numbers to console
else:
    print("\nwrong input - won't print numbers to console")
    print_hailstone_sequence = False  # wrong input - don't print hailstone sequence numbers to console

hailstone_sequence = []
total_stopping_time = 0

# this program assumes that the collatz conjecture is true (i.e. that every hailstone sequence reaches one)
while True:
    hailstone_sequence.append(int(num))
    if num == 1:
        break
    if num % 2 == 0:  # n is even
        num /= 2  # n/2
    else:  # n is odd
        num = 3 * num + 1  # 3n+1
    total_stopping_time += 1

if print_hailstone_sequence:
    print("\nhailstone sequence:\n\n\t", end='')
    print(*hailstone_sequence, sep="\n\t")

print("\nThe total stopping time was " + str(total_stopping_time) + ".\n")

# show graph
plt.plot(hailstone_sequence)
# plt.plot(hailstone_sequence, marker='o', markersize=9)
plt.show()