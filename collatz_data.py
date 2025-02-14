import matplotlib.pyplot as plt
import matplotlib.animation as animation

def collatz_sequence(n):
    """
    Generates the Collatz sequence for a given number.

    Track the 
    """

    """
    Compute Collatz-based pseudo-random metrics:
        - steps: total stopping time
        - sum_val: sum of the hailstone sequence values (excluding the final 1 based on snippet logic)
        - max_val: maximum value reached in the sequence
    Also returns the full sequence for plotting/animation purposes.
    """

    stopping_time = 0
    sum_val = 0
    max_val = n

    # Handle the edge case if starting value is 0
    if n == 0:
        return 0, 0, 0, [0]

    sequence = []
    while n != 1:
        stopping_time += 1
        sum_val += n
        sequence.append(n)

        # Collatz step
        n = n // 2 if n % 2 == 0 else 3 * n + 1

        # Track maximum
        if n > max_val:
            max_val = n

        # Optional safety break (arbitrary large cutoff)
        if stopping_time > 100000:
            break

    # Add the final '1'
    sum_val += 1
    sequence.append(1)

    return max_val, stopping_time, sum_val, sequence


def update_graph(frame):
    """Updates the graph for each step in the sequence."""
    if frame < len(hailstone_sequence):
        x_data.append(frame)
        y_data.append(hailstone_sequence[frame])
        line.set_data(x_data, y_data)
        ax.relim()
        ax.autoscale_view()
    return line,


# Get user input
while True:
    try:
        num = int(input("\nPlease enter a positive integer:\n\t"))
        if num > 0:
            break
        print("Invalid input - must be a positive integer.")
    except ValueError:
        print("Invalid input - must be an integer.")


# Use the collatz_sequence function to get all metrics and the sequence
max_val, stopping_time, sum_val, hailstone_sequence = collatz_sequence(num)

# Setup interactive plot
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot([], [], marker='o', linestyle='-', color='b')

ax.set_xlabel('Steps')
ax.set_ylabel('Value')
ax.set_title(f'Hailstone Sequence for {num}')
ax.grid(True)

# Animate graph while calculating sequence
ani = animation.FuncAnimation(
    fig, 
    update_graph, 
    frames=len(hailstone_sequence), 
    interval=500, 
    repeat=False
)

# Show the graph without blocking execution
plt.show(block=False)

# Print out the details (max_val, stopping_time, sum_val)
print(f"\nMax value reached: {max_val}")
print(f"Total stopping time: {stopping_time}")
print(f"Sum of values (including final 1): {sum_val}\n")

# Keep the plot open until the user closes it
plt.show()
