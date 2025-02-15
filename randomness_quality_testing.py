import os
import multiprocessing
import re
import struct
import subprocess
from collatz_LCG import CollatzLCG
import utils

# ANSI color codes for clearer labeling
COLOR_RESET = "\033[0m"
COLOR_GREEN = "\033[92m"    # For classic LCG
COLOR_BLUE = "\033[94m"   # For collatz LCG
COLOR_RED = "\033[91m"      # For errors

def generate_LCG_data(filename,
                        n=1000000, seed_input=42, method="collatz"):
    """
    Generates n 64-bit random numbers via either Collatz modified or classic LCG and writes them to a binary file.

    Parameters:
        filename (str): The output binary file.
        n (int): Number of random numbers to generate.
        seed_input (int): Seed for the random number generator.
        method (str): "collatz" or "classic" for the generation method.
    """

    rng = CollatzLCG(seed=seed_input)

    if method not in {"collatz", "classic"}:
        raise ValueError("Method must be either 'collatz' or 'classic'.")

    with open(filename, "wb") as f:
        for _ in range(n):
            val = rng.next_Collatz_LCG() if method == "collatz" else rng.next_classic_LCG()
            # Pack val as 8 bytes, little-endian
            f.write(struct.pack("<Q", val))

def parse_dieharder_results(filename):
    """
    Parses Dieharder results: summarizes PASSED, WEAK, and FAILED tests.
    W.I.P
    """

    return

def dieharder_testing(cmd, label, label_color, output_list):
    """
    Runs 'dieharder' sequentially (blocking until it finishes).
    Reads its stdout line by line, color-codes each line with 'label_color'.
    Also reads stderr after stdout completes, labeling those lines too.
    Appends all lines to 'output_list' for further usage.
    """

    process = subprocess.Popen(cmd, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    
    # Read stdout
    for line in iter(process.stdout.readline, ''):
        print(f"{label_color}[{label}]{COLOR_RESET} {line}", end='')  # line already has newline
        output_list.append(line)

    # Read stderr
    err_output = process.stderr.read()
    if err_output:
        for e_line in err_output.splitlines(True):
            print(f"{COLOR_RED}[{label} ERROR]{COLOR_RESET} {e_line}", end='')
            output_list.append(e_line)

    process.stdout.close()
    process.stderr.close()
    process.wait()

if __name__ == "__main__":

    # Get number of samples from user, default 1000000
    n = utils.get_positive_integer("\nEnter the number of random numbers to generate", 1000000)

    # Get seed from user, default 42
    seed = utils.get_positive_integer("Enter the seed value", 42)

    # Create output directory and paths
    output_dir = "randomness_quality_testing_results"
    os.makedirs(output_dir, exist_ok=True)
    classic_bin = os.path.join(output_dir, "classic_output.bin")
    collatz_bin = os.path.join(output_dir, "collatz_output.bin")
    classic_results = os.path.join(output_dir, "classic_dieharder_results.txt")
    collatz_results = os.path.join(output_dir, "collatz_dieharder_results.txt")

    # Delete existing test result files if they exist
    for file in [classic_bin, collatz_bin, classic_results, collatz_results]:
        if os.path.exists(file):
            os.remove(file)

    print("\nGenerating both Classic and Collatz LCG data in parallel...")

    # Create the two processes for data generation
    process1 = multiprocessing.Process(target=generate_LCG_data, args=(classic_bin, n, seed, "classic"))
    process2 = multiprocessing.Process(target=generate_LCG_data, args=(collatz_bin, n, seed, "collatz"))

    # Start both
    process1.start()
    process2.start()

    # Wait for both to finish
    process1.join()
    process2.join()

    print("\nBinary files are ready.")
    print("\nRunning Dieharder...\n")

    # Prepare lists to store the dieharder output for each
    classic_output_lines = []
    collatz_output_lines = []

    # dieharder test for classic LCG
    classic_cmd = f"dieharder -a -f {classic_bin}"
    print("=== Starting Classic LCG Dieharder Test ===\n")
    dieharder_testing(classic_cmd, "CLASSIC", COLOR_GREEN, classic_output_lines)
    print("\n=== Classic LCG test completed ===\n")

    # dieharder test for collatz LCG
    collatz_cmd = f"dieharder -a -f {classic_bin}"
    print("=== Starting Collatz LCG Dieharder Test ===\n")
    dieharder_testing(collatz_cmd, "COLLATZ", COLOR_BLUE, collatz_output_lines)
    print("\n=== Collatz LCG test completed ===\n")

    print(f"\nThe full results are saved in {output_dir}.\n")

    # Save the outputs to their respective text files
    with open(classic_results, "w") as f:
        f.writelines(classic_output_lines)
    with open(collatz_results, "w") as f:
        f.writelines(collatz_output_lines)

    # print("\nPrinting comparison...\n")
