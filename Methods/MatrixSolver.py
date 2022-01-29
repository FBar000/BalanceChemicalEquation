from Methods.MatrixOperations import *
import math

#TODO
# Convert the matrix into its reduced row echelon form with only integral entries
# I/O: 2d list (n x n) / Void
def rowEchelonMatrix(matrix):

    # Put the matrix into echelon form, ignore row simplifications
    n = len(matrix) - 1
    for it in range(n):

        # Ensure a nonzero pivot
        if matrix[it][it] == 0:

            # Swap with first non-zero entry belwo
            k = it

            while matrix[k][it] == 0:
                k += 1
                # Exit if none exist
                #TODO: When is this valid?
                if k > n - 1:
                    return

            changeRows(matrix, it, k)

        # Kill nonpivots
        for k in range(n):
            if k != it:
                if matrix[k][it] != 0:
                    LCM = math.lcm(matrix[k][it], matrix[it][it])
                    scaleRow(matrix, k, int(LCM / matrix[k][it]))
                    addRows(matrix, k, it, int(-LCM / matrix[it][it]))


    # Simplify rows
    for k in range(n):

        facs = [x for x in matrix[k] if x != 0]
        gcd = facs[0]
        for num in facs[1:]:
            gcd = find_gcd(num, gcd)

        scaleRowInt(matrix, k, 1 / gcd)

    return matrix




# Finds gcd of numbers
# Source: https://stackoverflow.com/questions/45316030/calculating-gcd-how-to-check-every-element-in-list
def find_gcd(x, y):
    while(y):
        x, y = y, x % y

    return x
