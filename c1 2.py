print("SJC23MCA-2059 : TOBIN K TOMY")
print("Batch : MCA 2023-25")
X = [[1,2,3],[4,5,6],[7,8,9]]
Y = [[1,2,3,],[4,5,6],[7,8,9]]
result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
for r in result:
    print(r)