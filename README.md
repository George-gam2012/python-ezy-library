ezy_calculator
ezy_calculator is a simple and lightweight Python library designed to perform basic arithmetic operations. It provides functions for addition, subtraction, multiplication, division, floor division, modulus, and exponentiation, making it easy to incorporate these operations in your projects without needing to write repetitive code.
This library is particularly useful for beginners who are learning Python and want a quick and easy way to perform basic mathematical operations.
Features
• Addition: Adds two numbers.
• Subtraction: Subtracts one number from another.
• Multiplication: Multiplies two numbers.
• Division: Divides one number by another, with a check to prevent division by zero.
• Floor Division: Performs division but returns the result as an integer (quotient), with handling for division by zero.
• Modulus: Returns the remainder of division between two numbers, with zero division handling.
• Exponentiation: Raises a number to the power of another number.
Installation
You can install the ezy_calculator library directly from PyPI by running:
bash
pip install ezy_calculator
Usage
Here are some basic examples of how to use the ezy_calculator library:
python
import ezy_calculator as ez

# Addition
result = ez.add(10, 5)
print(result)  # Output: 15

# Subtraction
result = ez.subtract(10, 5)
print(result)  # Output: 5

# Multiplication
result = ez.multiply(10, 5)
print(result)  # Output: 50

# Division
result = ez.divide(10, 2)
print(result)  # Output: 5.0

# Handling division by zero
result = ez.divide(10, 0)
print(result)  # Output: "error can not divide by zero"

# Floor Division
result = ez.floor_division(10, 3)
print(result)  # Output: 3

# Modulus
result = ez.modulus(10, 3)
print(result)  # Output: 1

# Exponentiation
result = ez.power(2, 3)
print(result)  # Output: 8
Error Handling
The library includes error handling for division, floor division, and modulus operations when the divisor is zero. In such cases, the functions will return an error message indicating that division by zero is not allowed.
For example:
python
result = ez.divide(5, 0)
print(result)  # Output: "error can not divide by zero"
Requirements
• Python 3.6 or higher.
Contributing
Feel free to fork the repository and submit pull requests if you wish to contribute to the development of ezy_calculator. All contributions are welcome!
License
This project is licensed under the MIT License - see the LICENSE file for details.
Author
Created by George. If you have any questions, you can reach me at gambroulasgiorgos@gmail.com.