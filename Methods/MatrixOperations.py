# Add a multiple of aRow to tRow
def addRows(matrix, tRow_index, aRow_index, constant):

    res = []

    for i in range(len(matrix[0])):
        a = matrix[tRow_index][i] + constant * matrix[aRow_index][i]
        res.append(a)

    matrix[tRow_index] = res

# Interchange two rows in a matrix
def changeRows(matrix, fRow_index, lRow_index):

    tmp = matrix[fRow_index]
    matrix[fRow_index] = matrix[lRow_index]
    matrix[lRow_index] = tmp

# Scale a matrix row by a constant k
def scaleRow(matrix, row_index, constant):

    row = []

    for i in matrix[row_index]:
        row.append(i*constant)

    matrix[row_index] = row



# Scale a matrix row by a constant k, ensure it's an int
def scaleRowInt(matrix, row_index, constant):

    row = []

    for i in matrix[row_index]:
        row.append(int(i*constant))

    matrix[row_index] = row