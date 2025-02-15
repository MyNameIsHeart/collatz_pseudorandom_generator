import matplotlib.pyplot as plt
import matplotlib.animation as animation
import collatz_algorithm
import utils

def update_graph(frame, x_data, y_data, hailstone_sequence, line, ax):
    """Updates the graph for each step in the sequence."""
    if frame < len(hailstone_sequence):
        x_data.append(frame)
        y_data.append(hailstone_sequence[frame])
        line.set_data(x_data, y_data)
        ax.relim()
        ax.autoscale_view()
    return line,

def plot_hailstone_sequence(num, hailstone_sequence):
    """Sets up and animates the hailstone sequence graph."""
    fig, ax = plt.subplots()
    x_data, y_data = [], []
    line, = ax.plot([], [], marker='o', linestyle='-', color='b')

    ax.set_xlabel('Stopping-time')
    ax.set_ylabel('Value')
    ax.set_title(f'Hailstone Sequence for {num}')
    ax.grid(True)

    ani = animation.FuncAnimation(
        fig, 
        update_graph, 
        frames=len(hailstone_sequence), 
        interval=500, 
        repeat=False,
        fargs=(x_data, y_data, hailstone_sequence, line, ax)
    )

    # Show the graph without blocking execution
    plt.show(block=False)
    return ani

if __name__ == "__main__":

    num = utils.get_positive_integer("Please enter a positive integer:")

    # Use the hailstone_sequence function to get all metrics and the sequence
    max_val, stopping_time, sum_val, hailstone_sequence = collatz_algorithm.hailstone_sequence(num)

    # Animte the graph 
    ani = plot_hailstone_sequence(num, hailstone_sequence)

    # Print out the details (max_val, stopping_time, sum_val)
    print(f"\nMax value reached: {max_val}")
    print(f"Total stopping time: {stopping_time}")
    print(f"Sum of values (including final 1): {sum_val}\n")

    # Keep the plot open until the user closes it
    plt.show()
