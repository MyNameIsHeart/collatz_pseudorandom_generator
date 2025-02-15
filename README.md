# collatz_pseudorandom_generator 🎲
\
This small project is a fun exploration of the **Collatz conjecture[^1]** and its potential applications in computer science - specifically **pseudorandom number generation**.

## Overview
\
It compares a 64-bit Linear Congruential Generator (LCG) against a Collatz-based variant that incorporates hailstone-sequence metrics to add nonlinear scrambling.

##
\
Randomness quality is assessed using Dieharder, and a separate script animates the Collatz (hailstone) sequence for a user-provided integer, providing a clear visualization of the stopping-time, maximum value reached, and total sum.

##
\
Since the project focuses on exploration rather than performance, efficiency wasn't a consideration.  

## Installation & Dependencies
\
Make sure you have **Python 3.x** installed as well as:
```bash
pip install matplotlib
sudo apt-get install dieharder
```

## Usage Guide

| Script                      | Purpose |
|-----------------------------|--------------------------------------------------|
| **`visualize_data.py`** | Animates a graph for the hailstone sequence of a given number and prints the relevant metrics. |
| **`collatz_LCG.py`** | Implements a Collatz-based LCG for pseudo-random number generation. |
| **`randomness_quality_testing.py`** | Generates LCG and Collatz-LCG binary files for testing, runs Dieharder tests and saves the results. |

[^1]: [The Collatz conjecture](https://youtu.be/094y1Z2wpJg), also known as the 3n+1 conjecture
