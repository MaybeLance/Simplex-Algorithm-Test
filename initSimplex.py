def knowPivotColumn(tableu, mode):
    removedRHS = []

    for i in range(0, (len(tableu[0]) - 1)):
        removedRHS.append(tableu[0][i])

    if mode == "max":
        value = removedRHS.index(min(removedRHS)) - 1
    elif mode == "min":
        value = removedRHS.index(max(removedRHS)) - 1
    else:
        print("Wrong mode!")

    return value


# Make function that decide which pivot row should be chosen
# Put the factors in a list (e.g. if element is list[0], then the pRow is tableu[0])   
def knowPivotRow(tableu, pCol):
    removedZ = []

    for i in range(1, len(tableu)):
        removedZ.append(tableu[i])

    lambdaDivision = []

    for i in range(0, len(removedZ)):
        if removedZ[i][pCol] <= 0:
            lambdaDivision.append("N/A")
        else:
            lastElemRow = removedZ[i][len(removedZ[i]) - 1]
            pColElem = removedZ[i][pCol]
            lambdaDivision.append(lastElemRow / pColElem)

    factorIndex = removedZ.index(min(removedZ))

    return factorIndex
        


def simplexIter(tableu, npRow, npCol):
    # Reduce the Pivot Row
    def reducePivotRow(rowElem):
        return rowElem / tableu[npRow][npCol]
    
    tableu[npRow] = list(map(reducePivotRow, tableu[npRow]))

    # Change all the other row
    for i in range(0, len(tableu)):
        if i == npRow:
            print(tableu[i])
        
        else:
            def updateRow(cRow, pRow):
                cRow = cRow - (tableu[i][npCol])*(pRow)
                return cRow
            
            tableu[i] = list(map(updateRow, tableu[i], tableu[npRow]))
            print(tableu[i])

# Sample Calls
# tableu = [
#          [696, 399, -100, 0, 0, 0, 900],
#          [3, 1, 0, 1, 0, 0, 3],
#          [4, 3, -1, 0, 1, 0, 6],
#          [1, 2, 0, 0, 0, 1, 4],
#        ]

# simplexIter(tableu, 1, 0)

# print(knowPivotColumn(tableu, "min"))
# print(knowPivotRow(tableu, knowPivotColumn(tableu, "min")))

# Note: Iteratively call the simplex function until problem is optimized.
