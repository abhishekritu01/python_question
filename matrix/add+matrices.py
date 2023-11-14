
 
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

result = [[0,0,0],
            [0,0,0],
            [0,0,0]]


# iterate through rows
for i in range(len(X)):
    for j in range(len(Y)):
        result[i][j] = X[i][j] + Y[i][j]
        print(f"({i},{j}): {X[i][j]} + {Y[i][j]} = {result[i][j]}")

for r in result:
    print(r)
        
     

