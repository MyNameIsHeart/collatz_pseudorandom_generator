# collatz_pseudorandom_generator 🎲
\
This small project is a fun exploration of the **Collatz conjecture**[^1] and its potential applications in computer science - specifically **pseudorandom number generation**.

##
\
It compares a 64-bit Linear Congruential Generator (LCG) against a Collatz-based variant that incorporates hailstone-sequence metrics to add nonlinear scrambling.

##
\
Randomness quality is assessed using Dieharder, and a separate script animates the Collatz (hailstone) sequence for a user-provided integer, providing a clear visualization of the stopping-time, maximum value reached, and total sum.

##
\
Because the project focuses on exploration rather than performance, efficiency wasn't a consideration.  

##
\
[^1] The Collatz conjecture, also known as the 3n+1 conjecture
