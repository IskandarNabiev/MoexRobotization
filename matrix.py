matrix = [[20, 4, 0, 2, 4],
          [6,  3,  9, 1, 2],
          [1,  0, -1, 1, 10],
          [8,  11, 0, 2, 5],
          [9,  1, -1, 2, 18]]

max_col = len(matrix[0])
max_row = len(matrix)

cols = [[] for _ in range(max_col)]
rows = [[] for _ in range(max_row)]
fdiag = [[] for _ in range(max_row + max_col - 1)]
bdiag = [[] for _ in range(len(fdiag))]
min_bdiag = -max_row + 1

for x in range(max_col):
    for y in range(max_row):
        cols[x].append(matrix[y][x])
        rows[y].append(matrix[y][x])
        fdiag[x+y].append(matrix[y][x])
        bdiag[x-y-min_bdiag].append(matrix[y][x])

print(cols)
print(rows)
print(fdiag)
print(bdiag)

min_sum = min(map(sum, fdiag))
print(max(filter(lambda x:sum(x) == min_sum, fdiag), key=len))