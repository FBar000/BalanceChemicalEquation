
# Overview

This program balances simple chemical equations. The main script, BCE.py, prompts users for a string containing an unbalanced chemical equation and returns a string containing the original equation with the coefficients which balance the equation. 
Ex: Input: "CH4 + O2 : CO2 + H2O" Output: " CH4 + 2 O2 : CO2 + 4 H2O" 


## Methods:

The methods used in the main file are stored in the `Methods` folder.

### EqValidator:

* Ensures a valid input

### MatrixToEq:

* Houses the method that converts the original string into a matrix

* Houses the method that converts the solution into a string

### MatrixOperations:

* Houses 3 matrix row operations. Mutates the input list

### MatrixSolver:

* Performs row reduction on coefficient matrix

### SolutionExtracter:

* Extracts relatively prime solution from reduced matrix


## Data 

The classes and constants used in the main file are stored in the `DataStruct` folder. 


### BCEClasses / Unit

This object consists of a pair of numbers which represent the start and the end of a substring. It is used by the methods that translate users' equations into matrices for the algorithm.

### BCEConstants / NULL_UNIT

This represents the null Unit; if a substring doesn't exist in a string, its Unit is the null Unit.

### BCEConstants / UNACCEPT

This is a list of the characters (as their ascii equivalent integer) that are unacceptable in equations.
