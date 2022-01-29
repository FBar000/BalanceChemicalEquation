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

def BCE(equation):

    if Methods.EqValidator.validate(equation):
        
        
        matrix = Methods.EqToMatrix.equationToMatrix(equation)
        pmatrix = Methods.MatrixSolver.rowEchelonMatrix(matrix)
        lineup = Methods.SolutionExtracter.lineUp(pmatrix)
        solution = Methods.SolutionExtracter.primeSolution(lineup)
        balanced_equation = Methods.EqToMatrix.wrapSolution(solution)

        print(balanced_equation)
        return solution

    else:
        print("Illegal entry")
        return -1


equation = input("Input your chemical equation: ")
BCE(equation)

A = input("Enter to Exit")