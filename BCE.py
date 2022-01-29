'''

DESCRIPTOR CONVENTION
# [Status]
# [Method Description]
# [IN_TYPE / OUT_TYPE]
'''

import Methods.EqToMatrix
import Methods.MatrixSolver
import Methods.SolutionExtracter
import Methods.EqValidator

equation = input("Input your chemical equation: ")

if Methods.EqValidator.validate(equation):
    
    
    matrix = Methods.EqToMatrix.equationToMatrix(equation)
    print(matrix)
    
    
    pmatrix = Methods.MatrixSolver.rowEchelonMatrix(matrix)
    print(pmatrix)
    
    lineup = Methods.SolutionExtracter.lineUp(pmatrix)
    solution = Methods.SolutionExtracter.primeSolution(lineup)
    print(lineup)
    
    balanced_equation = Methods.EqToMatrix.wrapSolution(solution)
    print(solution)
    print(balanced_equation)

else:
    print("Illegal character detected")

A = input("Press Key to Exit")