<<<<<<< HEAD
#This code was designed by Michail Gouvalaris on March 25th 2024.
=======
#This code was designed by Michail Gouvalaris on March 24th 2024.
>>>>>>> 7201ed01973e81969359bf59f24f10109e88772a
#It is intended for academic use at the Dept. of Informatics and Telecommunication of University of Ioannina.

#This code was designed and compiled at Python 3.12 .

#The code is a Python implementation of the Mid-Square pseudo-random number generation method. It squares an initial number, extracts the middle digits to form a new number, and repeats this process, printing each step's results. The algorithm aims to showcase how each generated number and its corresponding decimal value within [0,1] are derived, providing a clear demonstration of the Mid-Square technique.

#Last Update March 25th 2024



def mid_square_generator_and_print(Z0, n, steps=10):
    print(f"Initial Z0: {Z0}, n: {n}")
    numbers = [Z0]  # Initial number in the sequence

    for step in range(steps+1):
        Z_square = Z0**2
        Z_str = str(Z_square).zfill(2*n)  # Ensure string is at least 2n characters, padding with zeros if necessary
        middle_start = (len(Z_str) - n) // 2  # Calculate start index to extract middle n digits
        Z_new = int(Z_str[middle_start:middle_start + n])  # Extract middle n digits
        numbers.append(Z_new)
        Z0 = Z_new  # Prepare for next iteration

        # Printing results as per the provided example
        print(f"Z{step}={numbers[step]}, Z{step}^2={Z_square}, Y{step}={Z_square/(10**(2*n)):.8f}")

Z0 = 4153  # Initial Z value
n = 4  # Number of middle digits to consider

mid_square_generator_and_print(Z0, n)

