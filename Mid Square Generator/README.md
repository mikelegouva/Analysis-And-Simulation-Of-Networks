# Mid-Square Pseudo-Random Number Generator

This Python script implements the Mid-Square method for generating pseudo-random numbers, designed by Michail Gouvalaris on January 24th, 2024. The method involves squaring an initial number, extracting the middle digits to form a new number, and repeating this process to generate a sequence of numbers. This implementation not only generates these numbers but also prints each step's result, showcasing the generated number along with its corresponding decimal value within the range [0,1].

## Background

The Mid-Square method is a simple yet fascinating approach to generating pseudo-random numbers, often used for academic purposes to demonstrate the concept of random number generation in computational studies. This code was developed for use at the Department of Informatics and Telecommunication, University of Ioannina, and is intended for academic use.

## Features

- Generates a sequence of pseudo-random numbers using the Mid-Square method.
- Prints detailed step-by-step results, including the squared value, the extracted middle digits, and the decimal representation of the squared value.

## Requirements

- Python 3.12

## Usage

To use this script, simply run the `mid_square_generator_and_print` function with your initial number (`Z0`), the number of middle digits to consider (`n`), and optionally, the number of steps (`steps`) you want the generator to perform. Here is an example:

```python
Z0 = 4153  # Initial Z value
n = 4  # Number of middle digits to consider
mid_square_generator_and_print(Z0, n)
```
## Contributing
Contributions to this project are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License
This project is intended for academic use and is available under the MIT License.

## Last Updated
March 25th, 2024.