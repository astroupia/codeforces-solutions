n = int(input())  
matrix = [] 

for _ in range(n):
    matrix.append(list(map(int, input().split())))

mid = n // 2  
pairs = set()

for i in range(n):
    pairs.add((i, i))          
    pairs.add((i, n - 1 - i))  

for i in range(n):
    pairs.add((mid, i)) 
    pairs.add((i, mid))  

result = sum(matrix[i][j] for i, j in pairs)

print(result)
