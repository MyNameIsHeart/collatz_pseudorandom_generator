
import matplotlib.pyplot as plt

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to graph
plt.title('a graph')


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

hailstone_sequence = []

while num != 1:
    if (print_hailstone_sequence):
        print("\t" + str(int(num)))
    hailstone_sequence.append(num)
    if num % 2 == 0:  # n is even
        num /= 2  # n / 2
    else:  # n is odd
        num = 3 * num + 1  # 3n+1
    total_stopping_time += 1

if (print_hailstone_sequence):
    print("\t1")

print()

print("The total stopping time of the number you entered is " + str(total_stopping_time) + ".")

# plt.plot(hailstone_sequence, color='green', linestyle='dashed', linewidth = 3,
#           marker='o', markerfacecolor='blue', markersize=12)

plt.plot(hailstone_sequence)

# function to show the plot
plt.show()