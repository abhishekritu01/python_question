
# 
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]


result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

# iterate through rows of X

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] = result[i][j]+A[i][k] * B[k][j]
            print(f"({i},{j},{k}): {A[i][k]} * {B[k][j]} = {result[i][j]}")


for r in result:
    print(r)
