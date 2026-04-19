rows = 4 
columns = 4
matrix = []
for r in range(rows):
    row = []
    for c in range(columns):
        row.append(0)
    matrix.append(row)

for row in matrix:
    print(' '.join(map(str, row)))


for level in range(1, rows+1):
    print(" "*(rows - level)+ "*"*(2*level-1))