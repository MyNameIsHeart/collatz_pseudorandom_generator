
#########################################################################
# Collatz Conjecture utilization for a pseudo-random LCG based algorithm
#########################################################################

class CollatzLCG:

    def __init__(self, seed=1, a=6364136223846793005, c=1442695040888963407, m=2**64):
        """
        :seed: The initial seed.
        :a: Multiplier (common 64-bit LCG value).
        :c: Increment (common 64-bit LCG value).
        :m: Modulus, 2^64 (LCG will be 64-bit).
        """

        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

        self.state = seed

    def next_classic_LCG(self):
        """
        A basic 64-bit Linear Congruential Generator (LCG).
        """
        self.state = (self.a * self.state + self.c) % self.m
        return self.state
    
    def next_Collatz_LCG(self):
        """
        Compute Collatz-based pseudo-random metrics to be used with the 64-bit LCG

        Tracks:
            - Max height of the hailstone sequence (to be used as the seed).
            - Sum of the hailstone sequence.
            - Length of the hailstone sequence.

        """

        stopping_time = 0
        sum_val = 0
        current_val = self.state
        max_val = self.state

        if current_val == 0:
            return 0
        
        while current_val != 1:
            stopping_time += 1
            sum_val += current_val
            if current_val % 2 == 0:
                current_val //= 2
            else:
                current_val = 3 * current_val + 1
            if current_val > max_val:
                max_val = current_val
            current_val &= 0xFFFFFFFFFFFFFFFF

            # Safety break if stopping_time gets extremely large
            if stopping_time > 100000:  # Arbitrary large cutoff
                break

        # Add the final '1'
        sum_val += 1

        self.state = (stopping_time * max_val * self.state  + sum_val) % self.m
        return self.state
    
    def next_float(self):
        """
        Generate a floating-point number in [0, 1).
        """
        return self.state / self.m


###############################
# Example usage
###############################

if __name__ == "__main__":
    prng = CollatzLCG(seed=42)

    print("--- Classic LCG 64-bit ---")
    original_val = prng.next_classic_LCG()
    print(original_val)

    print("\n--- LCG + Collatz Metric ---")
    collatz_val = prng.next_Collatz_LCG()
    print(collatz_val)

###############################
# Basic Unit Tests
###############################
import unittest

class TestLCG(unittest.TestCase):
    def test_classic_LCG_reproducibility(self):
        # Test if the LCG is reproducible with the same seed
        prng1 = CollatzLCG(seed=42)
        prng2 = CollatzLCG(seed=42)
        self.assertEqual([prng1.next_classic_LCG() for _ in range(100)],
                         [prng2.next_classic_LCG() for _ in range(100)])
        
    def test_Collatz_LCG_reproducibility(self):
        # Test if the Collatz based LCG is reproducible with the same seed
        prng1 = CollatzLCG(seed=42)
        prng2 = CollatzLCG(seed=42)
        self.assertEqual([prng1.next_Collatz_LCG() for _ in range(100)],
                         [prng2.next_Collatz_LCG() for _ in range(100)])

    def test_collatz_LCG(self):
        # Simple test to ensure collatz_metric runs without errors
        result = CollatzLCG(seed=42).next_Collatz_LCG()
        self.assertGreaterEqual(result, 0)

    def test_next_float(self):
        # Simple test to ensure collatz_metric runs without errors
        result = CollatzLCG(seed=42).next_float()
        self.assertGreaterEqual(result, 0)

if __name__ == "__main__":
    unittest.main(exit=False)
