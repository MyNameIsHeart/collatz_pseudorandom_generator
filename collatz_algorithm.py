

def hailstone_sequence(starting_number):
    """
    Generates the hailstone sequence for a given number.

    Compute Collatz-based metrics:
        - stopping_time: total stopping time
        - sum_val: sum of the hailstone sequence values (including the 1 at the end)
        - max_val: maximum value reached in the sequence
        
    Also returns the full sequence for plotting/animation purposes.
    """

    stopping_time = 0
    sum_val = 0
    current_val = starting_number
    max_val = starting_number

    # Handle the edge case if starting value is 0
    if current_val == 0:
        return 0, 0, 0, [0]

    sequence = []
    while current_val != 1:
        stopping_time += 1
        sum_val += current_val
        sequence.append(current_val)

        # Collatz step
        current_val = current_val // 2 if current_val % 2 == 0 else 3 * current_val + 1

        # Track maximum
        if current_val > max_val:
            max_val = current_val

        # Optional safety break (arbitrary large cutoff)
        if stopping_time > 1000000:
            break

    # Add the final '1'
    sum_val += 1
    sequence.append(1)

    return max_val, stopping_time, sum_val, sequence