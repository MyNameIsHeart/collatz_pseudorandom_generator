import struct
from pseudo_random import CollatzLCG

def generate_collatz_data(filename="collatz_output.bin", n=100000):
    """
    Generate n 64-bit random numbers via CollatzLCG and write them to a binary file.
    """
    rng = CollatzLCG(seed=42)  # Change seed here
    with open(filename, "wb") as f:
        for _ in range(n):
            val = rng.next_Collatz_LCG()
            # Pack val as 8 bytes, little-endian
            f.write(struct.pack("<Q", val))

def generate_classic_data(filename="classic_output.bin", n=100000):
    """
    Generate n 64-bit random numbers via classic LCG and write them to a binary file.
    """
    rng = CollatzLCG(seed=42)
    with open(filename, "wb") as f:
        for _ in range(n):
            val = rng.next_classic_LCG()
            f.write(struct.pack("<Q", val))

if __name__ == "__main__":
    # Generate 64-bit values from each approach
    generate_collatz_data("collatz_output.bin", 100000)
    generate_classic_data("classic_output.bin", 100000)

    print("Binary files generated.")
