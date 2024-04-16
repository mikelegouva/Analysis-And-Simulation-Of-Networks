#This code was designed by Michail Gouvalaris on April 13th 2024.
#It is intended for academic use at the Dept. of Informatics and Telecommunication of University of Ioannina.

#This code was designed and compiled at Python 3.12 .

#The Python code implements a linear congruential generator (LCG) function to produce pseudo-random numbers based on specified parameters: modulus \( m \), multiplier \( a \), increment \( c \), and initial seed \( Z_0 \). The function generates numbers until it detects a repeat, establishing the period of the sequence. Parameters for two different scenarios are set up, and the function is run for each, printing the sequences and their periods. This demonstrates how variations in the parameters affect the randomness and period of the generated numbers.

#Last Update April 13th 2024



def linear_congruential_generator(m, a, c, Z0):
    # Initialize variables
    results = []
    Zi = Z0
    seen = set()
    
    while Zi not in seen:
        seen.add(Zi)
        results.append(Zi)
        Zi = (a * Zi + c) % m
    
    return results, len(results)

# Parameters for the task Part A
m_A = 16
a_A = 9
c_A = 5
Z0_A = 21

# Generate pseudo-random numbers and determine the period for Part A
numbers_A, period_A = linear_congruential_generator(m_A, a_A, c_A, Z0_A)
print("Part A: Generated numbers:", numbers_A)
print("Part A: Period of the generator:", period_A)

# Parameters for the task Part B
m_B = 16
a_B = 11
c_B = 0
Z0_B = 21

# Generate pseudo-random numbers and determine the period for Part B
numbers_B, period_B = linear_congruential_generator(m_B, a_B, c_B, Z0_B)
print("Part B: Generated numbers:", numbers_B)
print("Part B: Period of the generator:", period_B)
#