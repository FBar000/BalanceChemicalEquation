import Methods.EqToMatrix
import Methods.MatrixSolver
import Methods.SolutionExtracter
import Methods.EqValidator

# Takes unbalanced chemical equation as a string, returns balanced chemical equation as a string
def BCE(equation):
    
    # Tuple: boolean representing validity, first illegal character detected in equation 
    ctup = Methods.EqValidator.validate(equation)

    if ctup[0]:
        matrix = Methods.EqToMatrix.equationToMatrix(equation)   
        pmatrix = Methods.MatrixSolver.rowEchelonMatrix(matrix)
        lineup = Methods.SolutionExtracter.lineUp(pmatrix)
        solution = Methods.SolutionExtracter.primeSolution(lineup)
        
        return solution

    else:
        print("Illegal character detected")        
        return -1, ctup[1]

equation = input("Input your chemical equation: ")
print(Methods.EqToMatrix.wrapSolution(BCE(equation)))
A = input("Press Key to Exit")
