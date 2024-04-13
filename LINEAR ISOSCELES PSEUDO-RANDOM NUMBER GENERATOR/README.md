# Linear Congruential Generator

This repository contains a Python implementation of a linear congruential generator (LCG) for generating pseudo-random numbers. The code is designed by Michail Gouvalaris and is intended for academic use at the Department of Informatics and Telecommunications, University of Ioannina.

## Overview

The Python code implements a linear congruential generator (LCG) function to produce pseudo-random numbers. It utilizes specified parameters: modulus (m), multiplier (a), increment (c), and initial seed (Z0). The function generates numbers until it detects a repeat, thus establishing the period of the sequence. This demonstrates how variations in the parameters affect the randomness and period of the generated numbers.

## Installation

To run this code, ensure you have Python 3.12 or later installed. You can download Python from [python.org](https://www.python.org/downloads/).

## Usage

The code can be run directly if saved as a `.py` file. It includes two parts:

- **Part A**: Uses the parameters m = 16, a = 9, c = 5, Z0 = 21
- **Part B**: Uses the parameters m = 16, a = 11, c = 0, Z0 = 21

To execute, simply run the script and it will print out the pseudo-random numbers generated along with the period of the generator for each part.

```bash
python lcg.py
