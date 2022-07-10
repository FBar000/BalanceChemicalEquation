import math


# Given a matrix in reduced form with one free variable, finds the prime integral solution
# I/O: 2d list (n x m) / 1d list (n)
def extractSolution(matrix):
    return primeSolution(lineUp(matrix))


'''
This assumes a matrix of the form

int int int int ...
int int int int ...
... ... ... ...
str str str str ...

'''


# Given a matrix in reduced form with one free variable, returns a list with the coefficients if all
# variables are in an equality chain
# I/O: 2d list / dict (terms : coefficients)
def lineUp(matrix):
    res = {} # Dict ('term' : coefficient)
    og_matrix = matrix.copy()
    # Add x to result where x = ('term' : 0)
    for n in range(len(og_matrix)-1):
        if og_matrix[n][-1] == 0:
            res[og_matrix[-1][n]] = 0
            matrix.remove(og_matrix[n])
    # Find the coefficient of the last term to unify all equivalences
    '''
    Ex:
    An input matrix encodes equations of form:
    
    Na = Kz
    Mb = Ez
    Pc = Cz
    
    For integer {N M P K E C} wher {a b c z} are the coefficients. This step finds {A B C D Z} such that
    
    Aa = Bb = Cc = Zz
    '''
    facs = []
    for n in range(len(matrix)-1):  # Loop over int part of matrix
        facs.append(matrix[n][-1])  # Extract last column's value
    # Find LCM of extracted values
    lcm = facs[0]
    for num in facs[1:]:
        lcm = math.lcm(num, lcm)
    # Add terms' adjusted coefficients to result 
    # (symbolic of an equality chain e.g. Aa = Bb = ... )
    for i in range(len(matrix)-1):
        res[matrix[-1][i]] = int(-lcm/matrix[i][-1] * matrix[i][i])
    res[matrix[-1][-1]] = lcm
    return res

# Given the equality chain, returns a dict with the terms and their coefficients
# I/O: 1d list / 1d list
def primeSolution(lineUp):
    terms = list(lineUp)
    og_terms = terms.copy()
    primeSol = {}
    # Remove zero coefficients from lineup
    for k in range(len(og_terms)):
        if lineUp[og_terms[k]] == 0:
            primeSol[og_terms[k]] = 0
            terms.remove(og_terms[k])
    # Find LCM of coefficients
    lcm = lineUp[terms[0]]
    for key in terms[1:]:
        lcm = math.lcm(lineUp[key], lcm)
    # Each term's coefficient must be the quotient of the LCM and its coefficient in the chain
    for i in range(len(terms)):
        term = terms[i]
        primeSol[term] = int(lcm / lineUp[term])
    return primeSol


'''
Example:

7   0   0   -3
0   11  0   -2
0   0   5   -7

--TO-->

[98, 231, 30, 42]

--TO-->

[165, 70, 539, 385]


'''
