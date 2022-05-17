"# BalanceChemicalEquation" 

BCE.py prompts user for a string containing an unbalanced chemical equation, returns a string containing the original equation with coefficients, 
which balance the equation. The "yields" arrow is represented by ":"

Ex: Input: "CH4 + O2 : CO2 + H2O" Output: " CH4 + 2 O2 : CO2 + 4 H2O" 


Methods Module Descriptions:


EqValidator:

Ensures a legal input

MatrixToEq:

Houses the method that converts the original string into a matrix

Houses the method that converts the solution into a string

MatrixOperations:

Houses 3 matrix row operations. Mutates the input list

MatrixSolver:

Performs row reduction on coefficient matrix

SolutionExtracter:

Extracts relatively prime solution from reduced matrix
