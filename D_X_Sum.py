from collections import Counter

t = int(input())

for _ in range(t):
    m, n = map(int, input().split())

    chess = []

    for i in range(m):
        chess.append(list(map(int, input().split())))

    count_main = Counter()
    count_anti = Counter()

    for i in range(m):
        for j in range(n):
            count_main[i + j] += chess[i][j]
            count_anti[i-j] += chess[i][j]
        
    sum = 0
    for i in range(m):
        for j in range(n):
            main_sum = count_main[i + j] - chess[i][j]
            anti_sum = count_anti[i - j]
            sum = max(sum, main_sum + anti_sum) 
    

    print(sum)