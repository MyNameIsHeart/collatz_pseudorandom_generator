# - - - #

# This program regards The Collatz conjecture, also known as the 3n+1 conjecture.

# Paul Erdős once said (about the Collatz conjecture):
# "Mathematics may not be ready for such problems."

# - - - #

# this short program calculates the total stopping time of a given positive integer

# it may also print the hailstone sequence of the given positive integer

# This program assumes that the conjecture is correct and that these sequences always reach 1, no matter which
# positive integer is chosen to start the sequence.

# - - - #

# get input from user
num = input("\nplease enter a positive integer:\n\t")

print()

# verify that input is a positive integer
try:
    num = int(num)
    if num <= 0:  # input isn't a positive integer
        print("wrong input - input must be a positive integer")
        exit()
except ValueError:  # input isn't an integer
    print("wrong input - input must be an integer")
    exit()

print_hailstone_sequence = input("print the hailstone sequence? (yes / y / no / n)\n\t")

if print_hailstone_sequence.lower() == "yes" or print_hailstone_sequence.lower() == "y":
    print_hailstone_sequence = True  # print the hailstone sequence
elif print_hailstone_sequence.lower() == "no" or print_hailstone_sequence.lower() == "n":
    print_hailstone_sequence = False  # don't print the hailstone sequence
else:
    print("\nwrong input - won't print the hailstone sequence")
    print_hailstone_sequence = False  # wrong input - don't print the hailstone sequence

total_stopping_time = 0

if (print_hailstone_sequence):
    print("\nthe hailstone sequence:\n")

while num != 1:
    if (print_hailstone_sequence):
        print("\t" + str(int(num)))
    if num % 2 == 0:  # n is even
        num /= 2  # n / 2
    else:  # n is odd
        num = 3 * num + 1  # 3n+1
    total_stopping_time += 1

if (print_hailstone_sequence):
    print("\t1")

print()

print("The total stopping time of the number you entered is " + str(total_stopping_time) + ".")