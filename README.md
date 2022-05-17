
# Overview

This program balances simple chemical equations. The main script, BCE.py, prompts users for a string containing an unbalanced chemical equation and returns a string containing the original equation with the coefficients which balance the equation. 
Ex: Input: "CH4 + O2 : CO2 + H2O" Output: " CH4 + 2 O2 : CO2 + 4 H2O" 


## Methods Module Descriptions:


### EqValidator:

* Ensures a legal input

### MatrixToEq:

* Houses the method that converts the original string into a matrix

* Houses the method that converts the solution into a string

### MatrixOperations:

* Houses 3 matrix row operations. Mutates the input list

### MatrixSolver:

* Performs row reduction on coefficient matrix

### SolutionExtracter:

* Extracts relatively prime solution from reduced matrix
